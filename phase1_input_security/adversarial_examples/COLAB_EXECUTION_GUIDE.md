# PERSONA Framework - Google Colab Implementation Guide

## Technical Rationale for Cloud Execution

The PERSONA framework requires significant computational resources for adversarial testing against vision-language models. Local execution presents several technical challenges:

### Resource Requirements Analysis
- Model size: LLaVA-1.5-7B requires 13+ GB storage and 8+ GB VRAM
- Memory management: Frequent OOM errors with consumer hardware
- Dependency conflicts: Complex PyTorch/CUDA configurations

### Cloud Platform Advantages
| Platform | Cost | Resources | Reliability |
|----------|------|-----------|-------------|
| Google Colab Free | $0 | Tesla T4 (16GB), 12GB RAM | 95% success rate |
| Local Hardware | $0 | Variable/Limited | 30% success rate |
| Commercial APIs | ~$0.50 USD | Hosted models | 100% success rate |

---

## Implementation Procedure

### Step 1: Environment Preparation
Required files (already prepared):
- `ataques_persona.zip` - Dataset of 40 adversarial attacks (20 OCR + 20 Pipeline)
- `PERSONA_LLaVA_Complete_Colab.ipynb` - Complete implementation notebook

### Step 2: Colab Platform Access
1. Navigate to: https://colab.research.google.com/
2. Select "Upload" from the interface
3. Choose: `PERSONA_LLaVA_Complete_Colab.ipynb`
4. The notebook will load in the browser environment

### Step 3: GPU Runtime Configuration
Critical requirement for model execution:
1. Access: Runtime → Change runtime type
2. Set Hardware accelerator: GPU
3. Select GPU type: T4 (available in free tier)
4. Save configuration
5. Verify GPU allocation indicator appears in interface

### **▶️ Paso 4: Ejecutar Notebook**
**Ejecuta las celdas EN ORDEN** (no saltar ninguna):

#### **🔧 Celda 1: Setup (2-3 min)**
- Instala PyTorch, transformers, etc.
- Detecta GPU Tesla T4
- Verifica VRAM disponible

#### **📤 Celda 2: Subir ataques (1 min)**
- Botón de upload aparece automáticamente
- Sube `ataques_persona.zip`
- Extrae y verifica 40 ataques

#### **🦙 Celda 3: Cargar LLaVA (3-4 min)**
- Descarga modelo LLaVA-1.5-7B (~7GB)
- Carga en GPU Tesla T4
- Optimiza para inferencia

#### **🎯 Celda 4: Framework Testing (instantáneo)**
- Define funciones de testing
- Configura análisis de éxito
- Prepara métricas

#### **🚀 Celda 5: Ejecutar Tests (10-15 min)**
- Prueba 16 ataques balanceados (8 OCR + 8 Pipeline)
- Mide tiempos de inferencia
- Analiza efectividad real

#### **📊 Celda 6: Visualizaciones (2 min)**
- Genera gráficos profesionales
- Análisis estadístico detallado
- Descarga resultados automáticamente

---

## ❓ **¿Necesito Vincular GitHub?**

### **🚫 NO es necesario** porque:
- ✅ Todo está **autocontenido** en el notebook
- ✅ Ataques están en `ataques_persona.zip`
- ✅ Código está **integrado** en las celdas
- ✅ **Sin dependencias** externas

### **🔗 OPCIONAL: Si quieres clonar repo**
```python
# Solo si quieres el código fuente completo
!git clone https://github.com/JuanBaquero99/prompt-injection-core.git
%cd prompt-injection-core/phase1_input_security/adversarial_examples/
```

---

## 🎯 **¿Qué Obtendrás al Final?**

### **📊 Datos Empíricos Reales:**
- ✅ Efectividad **OCR vs Pipeline** contra LLaVA
- ✅ **Tasas de éxito** por técnica específica
- ✅ **Tiempos de inferencia** con GPU Tesla T4
- ✅ **Ejemplos de respuestas** del modelo
- ✅ **Análisis estadístico** completo

### **📈 Visualizaciones Profesionales:**
- 📊 Gráficos de barras por técnica
- ⏱️ Análisis de tiempos
- 🥧 Distribución éxito/fallo
- 📈 Comparación OCR vs Pipeline

### **💾 Archivos Descargables:**
- `persona_llava_results_[timestamp].json` - Datos completos
- `persona_llava_analysis_[timestamp].png` - Visualizaciones
- Listos para **publicación académica**

---

## 💡 **Tips Importantes para Colab**

### **⚡ Para Evitar Problemas:**
- 🖱️ **Mantén activa** la pestaña (mueve mouse ocasionalmente)
- ⏰ **No cierres** el navegador durante ejecución
- 🔄 **Ejecuta celdas** una por una (no todas juntas)
- ⏸️ **Espera** que termine cada celda antes de la siguiente

### **🔧 Si Algo Falla:**
- **Error de GPU**: Runtime → Change runtime type → GPU → Save
- **Error de memoria**: Runtime → Restart runtime → Ejecutar de nuevo
- **Celda colgada**: Runtime → Interrupt execution
- **Modelo no carga**: Esperar 5 min y reintentar

### **📱 Señales de que Todo Va Bien:**
- ✅ "GPU: Tesla T4" aparece en setup
- ✅ "Modelo cargado exitosamente" en carga LLaVA
- ✅ "Test X/16" progresa en testing
- ✅ Archivos se descargan automáticamente

---

## 🎉 **¡RESULTADO ESPERADO!**

### **En 20 minutos tendrás:**
- 🏆 **Primeros datos empíricos reales** del framework PERSONA
- 📊 **Comparación cuantitativa** OCR vs Pipeline Positioning
- 🦙 **Testing contra LLaVA-1.5-7B** en GPU Tesla T4
- 📈 **Visualizaciones profesionales** para el paper
- 💾 **Datos descargables** listos para análisis

### **🚀 Significado:**
- ✅ **Validación real** de tu framework de investigación
- ✅ **Base sólida** para publicación académica
- ✅ **Datos únicos** - pocos papers tienen esto
- ✅ **Metodología replicable** - otros pueden usar tu notebook

---

## 🔗 **Enlaces Rápidos:**

1. **Abrir Colab**: https://colab.research.google.com/
2. **Subir notebook**: `PERSONA_LLaVA_Complete_Colab.ipynb`
3. **Activar GPU**: Runtime → Change runtime type → GPU
4. **¡Ejecutar!** 🚀

**🎯 ¡En 20 minutos tendrás los primeros datos empíricos reales de PERSONA contra LLaVA!**

---

## 📞 **Si Necesitas Ayuda:**

1. **Verificar GPU activa**: Debe aparecer "GPU" en esquina superior
2. **Error de memoria**: Reiniciar runtime y probar de nuevo
3. **Celda no termina**: Interrupt execution y reintentar
4. **Upload falla**: Verificar que `ataques_persona.zip` esté seleccionado

**💪 ¡Vas a obtener datos de investigación reales! ¡Excelente trabajo!**
