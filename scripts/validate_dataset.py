"""
Script para validar el dataset final generado por process_datasets.py
- Muestra conteo por fuente y label
- Verifica duplicados y prompts vacíos
- Muestra ejemplos por fuente
"""

import pandas as pd
import os

FINAL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_final.csv')

df = pd.read_csv(FINAL_PATH)

print("\n--- Conteo por fuente ---")
print(df['source'].value_counts())

print("\n--- Conteo por label ---")
print(df['label'].value_counts())

print("\n--- Duplicados ---")

# Duplicados reales: prompts que aparecen más de una vez
dups = df['prompt'].value_counts()
real_dups = dups[dups > 1]
print(f"Prompts duplicados reales: {real_dups.sum()} (de {len(real_dups)} prompts únicos)")
if not real_dups.empty:
    print("Ejemplos de prompts duplicados:")
    print(real_dups.head())

print("\n--- Prompts vacíos ---")
empty_count = (df['prompt'].str.strip() == '').sum()
print(f"Prompts vacíos: {empty_count}")

print("\n--- Ejemplos por fuente ---")
for src in df['source'].unique():
    print(f"\nFuente: {src}")
    print(df[df['source'] == src].head(2))

print("\n--- Ejemplo de filas ---")
print(df.head())
