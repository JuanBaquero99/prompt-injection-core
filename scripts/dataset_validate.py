"""
Validation script for the final dataset produced by process_datasets.py.

Purpose:
- Provide quick sanity checks on the consolidated dataset used for prompt injection research.

What it does:
1) Loads the final CSV (data/dataset_final.csv).
2) Prints distribution by source (`source`) and by class label (`label`).
3) Detects duplicate prompts and reports counts and examples.
4) Counts empty prompts (strings that are blank after trimming whitespace).
5) Shows a small sample of rows per source and a quick dataset preview.

Key concepts:
- value_counts(): frequency table per category (e.g., per source or label).
- Duplicate detection via value_counts() on the 'prompt' text to find repeated content,
  not just identical rows.
- Empty prompt detection uses str.strip() == '' to catch whitespace-only strings.

Notes:
- If you also want to count NaN prompts as empty, combine `isna()` with the blank-string check:
    empty_or_na = df['prompt'].isna() | (df['prompt'].astype(str).str.strip() == '')
- To count only the "extra" duplicates beyond the first occurrence:
    extras = (dups[dups > 1] - 1).sum()

Expected columns in the CSV:
- 'prompt' (text), 'label' (e.g., 'malicious'/'benign'), 'source' (origin dataset),
  plus any additional metadata columns.

Dependencies:
- pandas
- CSV file located at data/dataset_final.csv (path resolved relative to this script).
"""

import pandas as pd
import os
from datasets import load_dataset

# Cargar Qualifire local

# Intentar cargar Qualifire local, si existe
qualifire_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'qualifire.csv')
if os.path.exists(qualifire_path):
    df_qualifire = pd.read_csv(qualifire_path)
    df_qualifire['source'] = 'qualifire'
    qualifire_ok = True
else:
    print("Advertencia: qualifire.csv no encontrado, se omitirá.")
    qualifire_ok = False

# Cargar Jayavibhav
ds_jayavibhav = load_dataset("jayavibhav/prompt-injection-safety")
df_jayavibhav = pd.DataFrame({
    'prompt': ds_jayavibhav['train']['text'],
    'label': ds_jayavibhav['train']['label'],
    'source': ['jayavibhav']*len(ds_jayavibhav['train']['text'])
})

# Cargar Yanismiraoui
ds_yanismiraoui = load_dataset("yanismiraoui/prompt_injections")
df_yanismiraoui = pd.DataFrame({
    'prompt': ds_yanismiraoui['train']['prompt_injections'],
    'label': [1]*len(ds_yanismiraoui['train']['prompt_injections']),
    'source': ['yanismiraoui']*len(ds_yanismiraoui['train']['prompt_injections'])
})


# Normaliza columna label en Qualifire si es necesario
if qualifire_ok:
    if 'label' not in df_qualifire.columns and 'benign' in df_qualifire.columns:
        df_qualifire['label'] = df_qualifire['benign'].apply(lambda x: 0 if x else 1)


# Cargar dataset en español generado
dataset_es_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_es.csv')
df_es = pd.read_csv(dataset_es_path)
df_es['source'] = 'generated_es'


# Unifica todos los datasets disponibles
datasets_to_concat = [
    df_jayavibhav[['prompt', 'label', 'source']],
    df_yanismiraoui[['prompt', 'label', 'source']],
    df_es[['prompt', 'label', 'source']]
]
if qualifire_ok:
    datasets_to_concat.insert(0, df_qualifire[['prompt', 'label', 'source']])
df_total = pd.concat(datasets_to_concat, ignore_index=True)


# Normaliza etiquetas: solo 'benign' y 'malicious'
def normalize_label(val):
    if str(val).lower() in ['benign', '0']:
        return 'benign'
    if str(val).lower() in ['malicious', '1', '2']:
        return 'malicious'
    return 'benign'  # Por defecto, para casos raros
df_total['label'] = df_total['label'].apply(normalize_label)

# Limpia duplicados y datos vacíos
df_total = df_total.drop_duplicates().dropna(subset=['prompt', 'label'])

# Guarda el dataset combinado
final_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_final.csv')
df_total.to_csv(final_path, index=False)
print(f"Dataset combinado guardado como {final_path}")

df = df_total

# Basic sanity checks
# Check value counts and how they compare
print("\n--- Conteo por fuente ---")
print(df['source'].value_counts())

print("\n--- Conteo por label ---")
print(df['label'].value_counts())

print("\n--- Duplicados ---")

# Duplicados reales: prompts que aparecen más de una vez
# Count how many prompts are duplicated
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
