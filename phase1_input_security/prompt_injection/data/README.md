# Estructura de datos para entrenamiento

- `raw/` : Datasets originales descargados de fuentes públicas (Hugging Face, GitHub, arXiv, etc.)
- `dataset_final.csv` : Dataset unificado, limpio y balanceado para entrenamiento.
- `augment/` : Ejemplos generados sintéticamente (opcional).

## Flujo recomendado

1. Guardar los archivos originales en `raw/`.
2. Procesar y normalizar los datos con scripts/notebooks.
3. Guardar el dataset final en la raíz de `data/`.
4. (Opcional) Guardar ejemplos sintéticos en `augment/`.

## Ejemplo de uso

- `data/raw/mitre_atlas.csv`
- `data/raw/owasp_examples.json`
- `data/raw/arxiv_prompts.txt`
- `data/dataset_final.csv`
- `data/augment/synthetic_examples.csv`

---

**Puedes agregar scripts de procesamiento en la raíz del proyecto o en una carpeta `scripts/`.**
