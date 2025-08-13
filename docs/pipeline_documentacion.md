# Documentación del pipeline de procesamiento de datasets para detección de prompt injection

## 1. Recolección de datos
- Se descargaron datasets públicos desde Hugging Face:
  - deepset/prompt-injections
  - xTRam1/safe-guard-prompt-injection
  - yanismiraoui/prompt_injections
  - (opcional) qualifire/prompt-injections-benchmark (requiere autenticación)
- Los datos se guardan en formato pandas DataFrame.

## 2. Normalización
- Se creó una función de normalización para cada dataset, unificando los campos:
  - prompt
  - label (benign/malicious)
  - type
  - source
  - lang

## 3. Unificación y limpieza
- Se concatenaron todos los datasets normalizados en un solo DataFrame.
- Se eliminaron los prompts duplicados, dejando solo ejemplos únicos.

## 4. Balanceo de clases
- Se balancearon las clases (benign/malicious) usando solo ejemplos únicos.
- El tamaño final del dataset es igual al grupo minoritario.

## 5. Exportación
- El dataset final se exportó a `data/dataset_final.csv`.

## 6. Validación
- Se creó un script para validar el dataset:
  - Conteo por fuente y label
  - Verificación de duplicados reales
  - Verificación de prompts vacíos
  - Ejemplos por fuente

## 7. Recomendación para el siguiente paso
- Dividir el dataset en entrenamiento/validación.
- Entrenar y evaluar modelos de detección de prompt injection.

---

Este pipeline garantiza un dataset limpio, balanceado y listo para experimentación y entrenamiento de modelos.
