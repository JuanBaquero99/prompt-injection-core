"""
Script para procesar, normalizar y unificar datasets de prompt injection.

Flujo:
1️⃣ Recolección: Lee archivos de data/raw/ y datasets de Hugging Face
2️⃣ Normalización: Unifica formato en un DataFrame
3️⃣ Limpieza y etiquetado: Elimina duplicados, corrige errores, balancea clases
4️⃣ Exporta dataset final a data/dataset_final.csv
"""

import os
import pandas as pd
from datasets import load_dataset
from sklearn.utils import resample

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
FINAL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_final.csv')


# 1️⃣ Recolección
print("Descargando datasets públicos...")

ds_deepset = load_dataset("deepset/prompt-injections")
df_deepset = ds_deepset["train"].to_pandas()

ds_xtram = load_dataset("xTRam1/safe-guard-prompt-injection")
df_xtram = ds_xtram["train"].to_pandas()

ds_yanis = load_dataset("yanismiraoui/prompt_injections")
df_yanis = ds_yanis["train"].to_pandas()

# Nuevo dataset recomendado
print("Descargando qualifire/prompt-injections-benchmark (requiere login en Hugging Face)...")
try:
    ds_qualifire = load_dataset("qualifire/prompt-injections-benchmark")
    df_qualifire = ds_qualifire["train"].to_pandas()
except Exception as e:
    print(f"No se pudo descargar qualifire/prompt-injections-benchmark: {e}")
    df_qualifire = pd.DataFrame(columns=["prompt", "label", "type", "source", "lang"])


# 2️⃣ Normalización
print("Normalizando formato...")

def normalize_deepset(df):
    df = df.copy()
    df['prompt'] = df['text']
    df['label'] = df['label'].map(lambda x: 'malicious' if x == 1 else 'benign')
    df['type'] = 'mixed'
    df['source'] = 'deepset/prompt-injections'
    df['lang'] = 'multi'
    return df[['prompt', 'label', 'type', 'source', 'lang']]

def normalize_xtram(df):
    df = df.copy()
    df['prompt'] = df['text']
    df['label'] = df['label'].map(lambda x: 'malicious' if x == 1 else 'benign')
    df['type'] = 'mixed'
    df['source'] = 'xTRam1/safe-guard-prompt-injection'
    df['lang'] = 'en'
    return df[['prompt', 'label', 'type', 'source', 'lang']]

def normalize_yanis(df):
    df = df.copy()
    df['prompt'] = df['prompt_injections']
    df['label'] = 'malicious'
    df['type'] = 'injection'
    df['source'] = 'yanismiraoui/prompt_injections'
    df['lang'] = 'multi'
    return df[['prompt', 'label', 'type', 'source', 'lang']]

def normalize_qualifire(df):
    df = df.copy()
    if 'text' in df.columns:
        df['prompt'] = df['text']
        df['label'] = df['label'].map(lambda x: 'malicious' if x == 'jailbreak' else 'benign')
        df['type'] = 'mixed'
        df['source'] = 'qualifire/prompt-injections-benchmark'
        df['lang'] = 'en'
        return df[['prompt', 'label', 'type', 'source', 'lang']]
    else:
        # DataFrame vacío, devolver columnas vacías
        return df

df_deepset_norm = normalize_deepset(df_deepset)
df_xtram_norm = normalize_xtram(df_xtram)
df_yanis_norm = normalize_yanis(df_yanis)
df_qualifire_norm = normalize_qualifire(df_qualifire)

# Unificación

df = pd.concat([df_deepset_norm, df_xtram_norm, df_yanis_norm, df_qualifire_norm], ignore_index=True)

# 3️⃣ Limpieza y etiquetado

print("Eliminando duplicados...")
# Eliminar todas las ocurrencias duplicadas, dejando solo una por prompt
df = df.drop_duplicates(subset=["prompt"], keep="first")

print("Balanceando clases solo con ejemplos únicos...")
unique_df = df.drop_duplicates(subset=["prompt"])
min_count = min(unique_df['label'].value_counts().values)
df_balanced = pd.concat([
    unique_df[unique_df['label'] == label].sample(n=min_count, random_state=42)
    for label in unique_df['label'].unique()
])

# 4️⃣ Exportar dataset final
print(f"Guardando dataset final en {FINAL_PATH}")
df_balanced.to_csv(FINAL_PATH, index=False)
print("¡Listo!")
