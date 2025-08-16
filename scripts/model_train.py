"""
model_train.py
--------------
Trains a Random Forest model for prompt injection detection using TF-IDF features.
Loads, splits, vectorizes, trains, evaluates, and saves the model and vectorizer.
Dependencies: pandas, scikit-learn, joblib, os
Author: Juan Pablo Baquero
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_final_combinado.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rf_model.pkl')

try:
    df = pd.read_csv(DATA_PATH)
    if df.empty:
        print(f"File {DATA_PATH} is empty.")
        exit(1)
except Exception as e:
    print(f"Error reading dataset: {e}")
    exit(1)

X = df['texto']
y = df['etiqueta']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Vectorize text using TF-IDF (limit to 5000 features)
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

# Train Random Forest model
clf = RandomForestClassifier(n_estimators=50, random_state=42, min_samples_leaf=10, max_features='sqrt', max_depth=10)
clf.fit(X_train_vec, y_train)

# 5. Evaluación+

# Ajuste de umbral de decisión
umbral = 0.5  # Umbral ajustado para priorizar detección de ataques
y_proba = clf.predict_proba(X_val_vec)
# Detectar automáticamente el valor de la clase 'malicioso'
malicioso_label = None
for label in clf.classes_:
    if str(label).lower() in ["malicious", "malicioso", "1"]:
        malicioso_label = label
        break
if malicioso_label is None:
    malicioso_label = clf.classes_[1]  # fallback: segunda clase
idx_malicioso = list(clf.classes_).index(malicioso_label)
y_pred_umbral = (y_proba[:, idx_malicioso] >= umbral).astype(int)
# Mapear 0/1 a etiquetas originales
etiquetas = list(clf.classes_)
if len(etiquetas) == 2:
    benign_label = etiquetas[0]
    malicioso_label = etiquetas[1]
else:
    benign_label = "benign"
    malicioso_label = "malicious"
y_pred_labels = [malicioso_label if p == 1 else benign_label for p in y_pred_umbral]

print(f"\n--- Métricas de validación (umbral={umbral}) ---")
print(classification_report(y_val, y_pred_labels))
print("\nMatriz de confusión:")
cm = confusion_matrix(y_val, y_pred_labels, labels=[benign_label, malicioso_label])
print(cm)
fp = cm[0,1]
fn = cm[1,0]
print(f"\nFalsos positivos: {fp}")
print(f"Falsos negativos: {fn}")

# 6. Guardar modelo
joblib.dump((vectorizer, clf), MODEL_PATH)
print(f"\nModelo guardado en {MODEL_PATH}")
