# 🦙 PERSONA Framework - Google Colab Guide

## 🎯 **¿Qué es Google Colab?**

**Google Colab** es una plataforma **GRATUITA** de Google que te permite ejecutar código Python en la nube con:
- ✅ **GPU Tesla T4 gratis** (16GB VRAM)
- ✅ **12GB RAM** garantizada 
- ✅ **Sin instalación** - funciona en el navegador
- ✅ **Tiempo ilimitado** con límites razonables
- ✅ **Compartible** - envías notebooks fácilmente

## 🚀 **Cómo usar PERSONA en Google Colab**

### **📋 PASO 1: Preparar archivos**
Ya tienes todo listo:
- ✅ `ataques_persona.zip` - 40 ataques generados
- ✅ `PERSONA_LLaVA_Testing_Colab.ipynb` - Notebook completo

### **🔗 PASO 2: Abrir Google Colab**
1. Ve a: https://colab.research.google.com/
2. Haz clic en "**Upload**" (subir)
3. Selecciona `PERSONA_LLaVA_Testing_Colab.ipynb`

### **🎮 PASO 3: Activar GPU (IMPORTANTE)**
1. En Colab, ve a: **Runtime** → **Change runtime type**
2. Selecciona: **Hardware accelerator: GPU**
3. Elige: **GPU type: T4** (gratis)
4. Haz clic: **Save**

### **▶️ PASO 4: Ejecutar el notebook**
1. **Celda 1**: Instalación (2-3 minutos)
2. **Celda 2**: Subir `ataques_persona.zip`
3. **Celda 3**: Cargar LLaVA (3-4 minutos)
4. **Celda 4**: Definir framework de testing
5. **Celda 5**: Ejecutar tests (10-15 minutos)
6. **Celda 6**: Análisis y visualizaciones

### **📊 PASO 5: Obtener resultados**
- ✅ **JSON con datos**: Se descarga automáticamente
- ✅ **Gráficos**: Visualizaciones profesionales
- ✅ **Análisis completo**: OCR vs Pipeline efectividad

---

## ❓ **¿Necesito vincular mi repositorio GitHub?**

### **🚫 NO es necesario** porque:
- ✅ **Archivos incluidos**: Todo está en el notebook
- ✅ **Datos listos**: `ataques_persona.zip` contiene todo
- ✅ **Código integrado**: Framework completo incluido
- ✅ **Sin dependencias**: Funciona standalone

### **🔗 OPCIONAL: Si quieres vincular repo**
```python
# En una celda de Colab:
!git clone https://github.com/JuanBaquero99/prompt-injection-core.git
%cd prompt-injection-core/phase1_input_security/adversarial_examples/
```

---

## 🎯 **¿Qué obtendrás?**

### **📊 Datos empíricos reales:**
- Efectividad OCR vs Pipeline contra LLaVA
- Tiempos de inferencia con GPU
- Ejemplos de respuestas del modelo
- Tasas de éxito por técnica

### **📈 Visualizaciones:**
- Gráficos de barras por técnica
- Análisis de tiempo de inferencia
- Distribución de éxitos/fallos
- Comparación visual OCR vs Pipeline

### **💾 Archivos de salida:**
- `llava_colab_results_YYYYMMDD_HHMMSS.json`
- `llava_results_analysis.png`
- Datos listos para publicación académica

---

## 🔥 **Ventajas de Colab vs Local**

| Aspecto | Local | Google Colab |
|---------|-------|--------------|
| **GPU** | ❌ CPU lento | ✅ Tesla T4 gratis |
| **RAM** | ❌ Limitada | ✅ 12GB garantizada |
| **Instalación** | ❌ 13GB+ | ✅ Sin instalación |
| **Tiempo setup** | ❌ Horas | ✅ 5 minutos |
| **Errores** | ❌ Memoria/deps | ✅ Funciona siempre |
| **Costo** | ❌ Recursos locales | ✅ Completamente gratis |

---

## 💡 **Tips para usar Colab**

### **⚡ Optimización:**
- Ejecuta celdas **una por una** para ver progreso
- **No cierres** el navegador durante ejecución
- **Mantén activa** la pestaña (mueve mouse ocasionalmente)

### **💾 Backup:**
- Los resultados se **descargan automáticamente**
- También se guardan en **session storage** de Colab
- Puedes **re-ejecutar** cualquier celda si necesitas

### **🔄 Si algo falla:**
- **Runtime** → **Restart runtime** → Ejecutar de nuevo
- Cambiar GPU si la actual está ocupada
- El notebook está diseñado para ser **robusto**

---

## 🎯 **¿Listo para empezar?**

1. **Abre**: https://colab.research.google.com/
2. **Sube**: `PERSONA_LLaVA_Testing_Colab.ipynb`
3. **Activa GPU**: Runtime → Change runtime type → GPU
4. **Ejecuta**: Todas las celdas una por una
5. **Obtén**: Primeros datos empíricos reales! 🚀

**🎉 En 20 minutos tendrás datos reales de efectividad contra LLaVA!**
