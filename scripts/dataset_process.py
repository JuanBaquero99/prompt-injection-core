"""
dataset_process.py
------------------
Processes, normalizes, and unifies prompt injection datasets from Hugging Face and local files.
Removes duplicates, balances classes, and exports a final CSV for model training.
Output columns: ['prompt', 'label', 'type', 'source', 'lang']
Dependencies: pandas, datasets, scikit-learn
"""

import os
import pandas as pd
from datasets import load_dataset
from sklearn.utils import resample

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
FINAL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_final.csv')


ds_deepset = load_dataset("deepset/prompt-injections")
df_deepset = ds_deepset["train"].to_pandas()

ds_xtram = load_dataset("xTRam1/safe-guard-prompt-injection")
df_xtram = ds_xtram["train"].to_pandas()

ds_yanis = load_dataset("yanismiraoui/prompt_injections")
df_yanis = ds_yanis["train"].to_pandas()

# Nuevo dataset recomendado
print("Downloading public datasets...")
ds_deepset = load_dataset("deepset/prompt-injections")
df_deepset = ds_deepset["train"].to_pandas()

ds_xtram = load_dataset("xTRam1/safe-guard-prompt-injection")
df_xtram = ds_xtram["train"].to_pandas()

ds_yanis = load_dataset("yanismiraoui/prompt_injections")
df_yanis = ds_yanis["train"].to_pandas()

print("Downloading qualifire/prompt-injections-benchmark (requires Hugging Face login)...")
try:
    ds_qualifire = load_dataset("qualifire/prompt-injections-benchmark")
    df_qualifire = ds_qualifire["train"].to_pandas()
except Exception as e:
    print(f"Could not download qualifire/prompt-injections-benchmark: {e}")
    df_qualifire = pd.DataFrame(columns=["prompt", "label", "type", "source", "lang"])


print("Normalizing format...")

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
# Concatenated DataFrames

df = pd.concat([df_deepset_norm, df_xtram_norm, df_yanis_norm, df_qualifire_norm], ignore_index=True)

# 3️⃣ Limpieza y etiquetado

print("Eliminando duplicados...")
# Eliminar todas las ocurrencias duplicadas, dejando solo una por prompt
# Search for duplicate prompts and eliminates
# Sample() select aleatorily one of the duplicates balancing the dataset
# Random_state set to ensure reproducibility
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
