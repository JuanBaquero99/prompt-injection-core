"""
MLDetector: Model-based input classification component
------------------------------------------------------
Loads a pre-trained model and TF-IDF vectorizer from disk and exposes
a `predict(input_text)` method for integration into a text-processing pipeline.

Features:
- Load a serialized model (vectorizer + classifier) using joblib.
- Transform text inputs into feature vectors.
- Predict the category and return probabilities.

Usage:
- Create an MLDetector instance.
- Call `predict(input_text)` with a string or a list of strings to classify.
- Use this class as part of a larger system for automated text screening.
"""
from __future__ import annotations

import os
from typing import List, Union, Dict, Any, Tuple
from .base import Detector
from .models import Detection
import joblib
import numpy as np
from scipy import sparse

# Keep the real labels to preserve compatibility with the rest of the system,
# but avoid writing the words directly in docstrings/examples.
BENIGN_LABEL = "benign"
MALICIOUS_LABEL = "malicious"
DEFAULT_LABELS: Tuple[str, str] = (BENIGN_LABEL, MALICIOUS_LABEL)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "rf_model.pkl"
)

class MLDetector(Detector):
    def __init__(self, model_path: str = MODEL_PATH, threshold: float = 0.7) -> None:
        super().__init__(name="MLDetector")
        try:
            loaded = joblib.load(model_path)
            if isinstance(loaded, tuple) and len(loaded) == 2:
                self.vectorizer, self.clf = loaded
            else:
                self.vectorizer = loaded.get("vectorizer")
                self.clf = loaded.get("clf") or loaded.get("classifier")
            if self.vectorizer is None or self.clf is None:
                raise ValueError("Missing vectorizer or classifier in the artifact.")
        except Exception as e:
            raise RuntimeError(f"Error loading ML model: {e}")
        self._benign_col, self._malicious_col = self._resolve_class_indices()
        self.threshold = threshold
    def detect(self, prompt: str) -> List[Detection]:
        """
        Detecta si el prompt es malicioso usando el umbral configurado.
        Devuelve una lista con un Detection si se detecta como malicioso, vacío si es benigno.
        """
        result = self.predict(prompt)
        # Usar la predicción por umbral
        if result['prediction_by_threshold'] == MALICIOUS_LABEL:
            detection = Detection(
                vulnerability_type="ML Malicious Prompt",
                confidence=result['prob_malicious'],
                severity="HIGH" if result['prob_malicious'] > 0.9 else "MEDIUM",
                description=f"Prompt detectado como malicioso por el modelo ML (umbral={self.threshold})",
                evidence=f"Probabilidad malicioso: {result['prob_malicious']:.3f}",
                recommendations=["Revisar el prompt y bloquear si es necesario."],
                detector=self
            )
            return [detection]
        else:
            return []

    def _resolve_class_indices(self) -> Tuple[int, int]:
        """
        Determine which columns of predict_proba correspond to benign/malicious.
        Tries multiple conventions to be robust (string labels or 0/1).
        """
        # Default columns (0: benign, 1: malicious)
        benign_idx, malicious_idx = 0, 1

        classes = getattr(self.clf, "classes_", None)
        if classes is None:
            return benign_idx, malicious_idx

        # Convert numpy arrays to list for searching
        classes_list = list(classes)

        # Case A: Trained with string labels
        if BENIGN_LABEL in classes_list and MALICIOUS_LABEL in classes_list:
            benign_idx = classes_list.index(BENIGN_LABEL)
            malicious_idx = classes_list.index(MALICIOUS_LABEL)
            return benign_idx, malicious_idx

        # Case B: Trained with numeric labels (0/1)
        if 0 in classes_list and 1 in classes_list:
            benign_idx = classes_list.index(0)
            malicious_idx = classes_list.index(1)
            return benign_idx, malicious_idx

        # Fallback: if there are exactly two classes, assume index order
        if len(classes_list) == 2:
            return 0, 1

        # Last resort
        return benign_idx, malicious_idx

    def _ensure_iterable(self, input_text: Union[str, List[str]]) -> List[str]:
        if isinstance(input_text, str):
            return [input_text]
        if isinstance(input_text, list) and all(isinstance(p, str) for p in input_text):
            return input_text
        raise ValueError("Input must be a string or a list of strings.")

    def predict(self, input_text: Union[str, List[str]]) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Predict category and probabilities for one or many inputs.

        Parameters
        ----------
        input_text : str | list[str]
            Text to classify.

        Returns
        -------
        dict | list[dict]
            For each input, returns:
            {
              'text': <original input>,
              'prediction': 'benign' | 'malicious',  # estándar del modelo
              'prediction_by_threshold': 'benign' | 'malicious',  # usando el umbral
              'prob_benign': float,
              'prob_malicious': float,
              'threshold': float
            }
        """
        texts = self._ensure_iterable(input_text)

        vec = self.vectorizer.transform(texts)
        probs = self.clf.predict_proba(vec)
        preds = self.clf.predict(vec)

        results = []
        for i, text in enumerate(texts):
            benign_prob = probs[i][self._benign_col]
            malicious_prob = probs[i][self._malicious_col]
            label = BENIGN_LABEL if preds[i] == BENIGN_LABEL else MALICIOUS_LABEL
            # Predicción usando el umbral
            label_by_threshold = MALICIOUS_LABEL if malicious_prob >= self.threshold else BENIGN_LABEL
            results.append({
                'text': text,
                'prediction': label,
                'prediction_by_threshold': label_by_threshold,
                'prob_benign': float(benign_prob),
                'prob_malicious': float(malicious_prob),
                'threshold': self.threshold
            })
        return results[0] if isinstance(input_text, str) else results
