# This file has been moved to docs/controles_avanzados.md
# Medidas y controles avanzados para seguridad en LLMs

## Medidas priorizadas para desarrollo futuro

1. **Aislar instrucciones del sistema y marcar fuentes no confiables**
   - Separar contexto del sistema y usuario. Registrar procedencia para trazabilidad.
2. **Obligar a formatos estructurados (y validarlos)**
   - Usar JSON, YAML o esquemas validados para evitar ambigüedad y facilitar análisis.
3. **Filtrado y “content firewall” de entrada/salida**
   - Reglas y detectores para bloquear/alertar sobre contenido malicioso antes y después del modelo.
4. **Menor privilegio y “tool-use” controlado**
   - Limitar capacidades y uso de herramientas. Listas blancas/negras y monitoreo.
5. **Navegación/ingesta segura (RAG/Agentes)**
   - Controlar fuentes externas y validar todo lo que se ingesta.
6. **Verificación externa (“LLM-as-a-Judge”/reglas)**
   - Segundo modelo o reglas para revisar respuestas antes de ejecutarlas o mostrarlas.
7. **Reforzar prompts (pero asumiendo que pueden fallar)**
   - Técnicas de robustecimiento, pero siempre defensa en profundidad.
8. **Observabilidad y pruebas adversarias**
   - Registro de interacciones y pruebas de penetración/adversarias periódicas.
9. **Fail-closed para acciones peligrosas**
   - Bloquear por defecto ante duda o error.
10. **Arquitectura recomendada (resumen)**
    - Sistema en capas: validación, filtrado, control de privilegios, monitoreo, verificación externa.

## Controles adicionales

1. **Separación de roles en LLMs**
   - Definir y aislar roles (usuario, sistema, agente, herramienta).
2. **Tamaño de contexto controlado**
   - Limitar información en el contexto para evitar overflow y manipulación.
3. **Randomización defensiva**
   - Variabilidad en respuestas/instrucciones para dificultar ataques predictivos.
4. **Análisis semántico adversarial**
   - Detectores de manipulación semántica, no solo palabras clave.
5. **Listas negras y blancas de acciones**
   - Control explícito de acciones permitidas/prohibidas en prompts y herramientas.
6. **Escaneo de secretos en tiempo real**
   - Analizar contexto y respuestas para evitar filtración de datos sensibles.
7. **Tiempo y frecuencia de ejecución**
   - Limitar frecuencia de acciones para evitar abusos.
8. **Respuesta degradada controlada**
   - Ante riesgo, responder con información limitada en vez de bloquear completamente.

---


## Ruta recomendada para avanzar en el proyecto

1. **Preparar y organizar el dataset real**
   - Recopila ejemplos maliciosos y benignos, con etiquetas y tipo de ataque.
   - Formato sugerido: CSV o JSON con campos: prompt, label, type, source.

2. **Entrenamiento y validación de detectores**
   - Ajusta reglas, patrones y umbrales usando el dataset.
   - Si usas ML, entrena y evalúa el modelo con métricas (precisión, recall, F1-score).

3. **Integración en el sistema**
   - Actualiza los detectores para usar los nuevos patrones, reglas o modelo entrenado.
   - Añade tests con ejemplos del dataset.

4. **Implementación de controles avanzados**
   - Prioriza los controles según los resultados del entrenamiento y necesidades detectadas.
   - Documenta cada control y su función en el sistema.

**Resumen:**
Primero entrena y valida con datos reales para obtener métricas y ajustar la detección. Luego, implementa los controles avanzados priorizados según el impacto y facilidad de integración. Mantén la documentación actualizada para guiar el desarrollo.
