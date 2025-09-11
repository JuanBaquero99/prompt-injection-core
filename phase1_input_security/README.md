# Fase 1 - Entrada y Manipulación de Datos

Enfocada en amenazas que ocurren antes o durante el procesamiento de la entrada al modelo.

## 🎯 Amenazas Cubiertas

### 1.1 Prompt Injection ✅ **COMPLETADO**
- **Estado**: Completamente implementado y funcional
- **Ubicación**: `./prompt_injection/`
- **Capacidades**:
  - Detección multicapa (regex, ML, adversarial)
  - Modelo RandomForest optimizado
  - Detección de camuflaje educativo
  - Pipeline completo de investigación a producción

### 1.3 Adversarial Examples ✅ **COMPLETADO - EVALUACIÓN EMPÍRICA**
- **Estado**: Framework PERSONA completamente implementado y evaluado
- **Objetivo**: Generar y evaluar ataques adversariales contra modelos visión-lenguaje
- **Ubicación**: `./adversarial_examples/`
- **Capacidades**:
  - **OCR Injection**: 4 técnicas (invisible text, steganographic, transparent, microscopic)
  - **Pipeline Positioning**: 4 técnicas (preprocessing, feature extraction, attention hijacking, multi-stage)
  - **Evaluación sistemática**: 40 ataques contra LLaVA-1.5-7B
  - **Multi-prompt testing**: 3 estrategias por ataque
  - **Success detection**: Algoritmo de 67 indicadores
- **Resultados empíricos**:
  - 🎯 **12.5% success rate general** (2/16 ataques exitosos)
  - 🔍 **Pipeline positioning: 25% efectividad** vs OCR injection: 0%
  - 🏆 **Preprocessing injection** identificada como técnica más vulnerable
  - 📊 **Primera evaluación sistemática** de vulnerabilidades en LLaVA

### 5.1 Validación y Filtrado de Inputs 📝 **PLANEADO**  
- **Estado**: En planificación
- **Objetivo**: Sistema robusto de validación y sanitización de entradas
- **Ubicación futura**: `./input_validation/`

## 🚀 Quick Start

### Prompt Injection
```bash
cd prompt_injection
python demo_complete.py
```

### Evaluación de Rendimiento
```bash
cd prompt_injection
python evaluate_model.py
```

## 📊 Métricas Actuales

### Prompt Injection
- ✅ **Precisión**: 100% (cero falsos positivos)
- ⚠️ **Recall**: 30% (detecta ataques directos)
- ✅ **Especificidad**: 100% (no molesta usuarios legítimos)

### Adversarial Examples (Framework PERSONA)
- 🎯 **Success Rate General**: 12.5% (2/16 ataques exitosos)
- 📊 **Pipeline Positioning**: 25% efectividad (5/20 ataques)
- 🚫 **OCR Injection**: 0% efectividad (0/20 ataques)
- 🔍 **Preprocessing Injection**: 40% efectividad (2/5 ataques)
- 📈 **Confidence Score**: 0.900 en ataques exitosos
- 📋 **Statistical Significance**: p < 0.001 (diferencia altamente significativa)

## 🗂️ Estructura de Carpetas

```
phase1_input_security/
├── README.md                    # Este archivo
├── prompt_injection/            # Sistema completo de detección
│   ├── core.py                 # Motor principal
│   ├── detectors/              # Detectores especializados
│   ├── scanner/                # Scanner modular
│   ├── data/                   # Datasets y modelos
│   ├── examples/               # Ejemplos de uso
│   ├── research/               # Investigación avanzada
│   ├── scripts/                # Scripts de utilidad
│   └── tests/                  # Suite de pruebas
├── adversarial_examples/        # ✅ Generadores de ataques adversariales
│   ├── attack_generators/      # Generadores por técnica
│   ├── test_cases/             # Ataques generados
│   ├── evaluation/             # Métricas de evaluación
│   └── models/                 # Interfaces para testing
└── input_validation/           # [FUTURO] Validación de inputs
```

## 🔬 Investigación Activa

### Prompt Injection
- **Educational Disguise Detection**: Primer sistema en detectar ataques camuflados
- **Análisis semántico**: Intención real vs apariencia
- **Pipeline adaptativo**: Investigación → producción automatizado

### Adversarial Examples - PERSONA Framework
- **Primera evaluación sistemática**: LLaVA-1.5-7B vulnerabilities
- **Pipeline positioning attacks**: Más efectivos que métodos tradicionales
- **Multi-modal security**: Intersección visión-lenguaje
- **Paper académico**: En preparación para conference submission

### Próximos Pasos
- 🔍 **Refinamiento de ataques exitosos**: Mejorar preprocessing injection
- 🎯 **Expansión de evaluación**: GPT-4V, BLIP-2, Qwen-VL
- 🛡️ **Desarrollo de defensas**: Contramedidas específicas
- 📄 **Publicación académica**: Documentar hallazgos

## 📞 Contacto

Para colaboraciones específicas en Fase 1:
- **Juan Pablo Baquero** - baquerojuan99@gmail.com
