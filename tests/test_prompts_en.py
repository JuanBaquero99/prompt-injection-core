import unittest
import joblib
import os

class TestPromptModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prompts_path = os.path.join("data", "prompts_test.txt")
        cls.model_path = os.path.join("data", "rf_model.pkl")
        vectorizer, clf = joblib.load(cls.model_path)
        cls.vectorizer = vectorizer
        cls.clf = clf
        with open(cls.prompts_path, 'r', encoding='utf-8') as f:
            cls.prompts = [line.strip() for line in f if line.strip()]

    def test_predictions(self):
        """Test that model returns predictions for all prompts."""
        X_vec = self.vectorizer.transform(self.prompts)
        preds = self.clf.predict(X_vec)
        self.assertEqual(len(preds), len(self.prompts))
        # Opcional: verificar que las predicciones sean del tipo esperado
        for pred in preds:
            self.assertIn(pred, ["malicious", "benign"])  # Etiquetas reales del modelo

if __name__ == "__main__":
    unittest.main()
