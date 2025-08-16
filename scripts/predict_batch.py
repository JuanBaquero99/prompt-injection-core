"""
Script para pruebas automáticas del modelo de detección de prompt injection
-------------------------------------------------------------
Lee una lista de prompts desde un archivo, clasifica cada uno y guarda los resultados en un CSV.

Uso:
- Coloca los prompts a probar en 'data/prompts_test.txt', uno por línea.
- Ejecuta el script y revisa 'data/predictions_test.csv' para ver los resultados.
"""
import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rf_model.pkl') #Model Location
PROMPTS_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prompts_test.txt')# Prompts Location
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'predictions_test.csv')# Output save Location

# --- Cargar modelo ---
try:
    vectorizer, clf = joblib.load(MODEL_PATH)
    print(f"✅ Modelo cargado de {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error al cargar el modelo: {e}")
    exit(1)

# --- Leer prompts ---
try:
    with open(PROMPTS_PATH, 'r', encoding='utf-8') as f:
        prompts = [line.strip() for line in f if line.strip()]
    if not prompts:
        print(f"⚠️ El archivo {PROMPTS_PATH} está vacío.")
        exit(1)
except Exception as e:
    print(f"❌ Error al leer los prompts: {e}")
    exit(1)

# --- Clasificar y guardar resultados ---
results = []
for prompt in prompts:
    vec = vectorizer.transform([prompt])
    pred = clf.predict(vec)[0]
    proba = clf.predict_proba(vec)[0]
    results.append({
        'prompt': prompt,
        'prediction': pred,
        'prob_benign': round(proba[0], 4),
        'prob_malicious': round(proba[1], 4)
    })

# Guardar en CSV
pd.DataFrame(results).to_csv(OUTPUT_PATH, index=False)
print(f"✅ Resultados guardados en {OUTPUT_PATH}")
