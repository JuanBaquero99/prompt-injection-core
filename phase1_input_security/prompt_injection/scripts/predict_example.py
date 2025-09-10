"""
Script para probar la predicción del modelo entrenado de prompt injection.

Uso:
- Modifica la variable 'prompt' para probar diferentes ejemplos.
- Ejecuta: python scripts/predict_example.py

"""
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rf_model.pkl')

# Cargar modelo y vectorizador
try:
    vectorizer, clf = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit(1)

# Prompt de prueba (puedes cambiarlo)
prompt = input("Enter a message to test: ")

# Vectorizar y predecir
X_vec = vectorizer.transform([prompt])
pred = clf.predict(X_vec)
proba = clf.predict_proba(X_vec)

print(f"Prompt: {prompt}")
print(f"Predicción: {pred[0]}")
print(f"Probabilidades: {dict(zip(clf.classes_, proba[0]))}")
