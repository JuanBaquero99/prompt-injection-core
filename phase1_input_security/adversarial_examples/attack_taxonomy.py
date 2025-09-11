"""
TAXONOMÍA COMPLETA DE ATAQUES ADVERSARIALES MULTIMODALES
========================================================

Clasificación exhaustiva de técnicas de ataque contra modelos de visión y lenguaje.
Esta taxonomía guía el desarrollo completo del framework PERSONA.

Autor: PERSONA Research Team
Fecha: Septiembre 2025
"""

from enum import Enum
from typing import Dict, List, Any
from dataclasses import dataclass

class AttackCategory(Enum):
    """Categorías principales de ataques adversariales"""
    OCR_INJECTION = "ocr_injection"
    VISUAL_CONFUSION = "visual_confusion" 
    SEMANTIC_MANIPULATION = "semantic_manipulation"
    ADVERSARIAL_PERTURBATIONS = "adversarial_perturbations"
    MULTIMODAL_JAILBREAKING = "multimodal_jailbreaking"
    PROMPT_INJECTION_VISUAL = "prompt_injection_visual"
    STEGANOGRAPHIC_COMMANDS = "steganographic_commands"
    CONTEXT_POISONING = "context_poisoning"

@dataclass
class AttackTechnique:
    """Descripción de una técnica de ataque específica"""
    name: str
    category: AttackCategory
    description: str
    difficulty: str  # "basic", "intermediate", "advanced", "expert"
    detectability: str  # "low", "medium", "high"
    effectiveness: str  # "theoretical", "proven", "weaponized"
    target_models: List[str]
    implementation_complexity: int  # 1-10 scale

# =============================================================================
# CATEGORÍA 1: OCR INJECTION (YA IMPLEMENTADA)
# =============================================================================
OCR_TECHNIQUES = [
    AttackTechnique(
        name="Steganographic Text Embedding",
        category=AttackCategory.OCR_INJECTION,
        description="Oculta texto en metadatos o LSB de imágenes",
        difficulty="intermediate",
        detectability="low", 
        effectiveness="proven",
        target_models=["LLaVA", "GPT-4V", "Claude-3"],
        implementation_complexity=6
    ),
    AttackTechnique(
        name="Invisible Text Overlay",
        category=AttackCategory.OCR_INJECTION,
        description="Texto con color casi idéntico al fondo",
        difficulty="basic",
        detectability="medium",
        effectiveness="proven", 
        target_models=["Most Vision-Language Models"],
        implementation_complexity=3
    ),
    AttackTechnique(
        name="Microscopic Text Injection",
        category=AttackCategory.OCR_INJECTION,
        description="Texto extremadamente pequeño pero legible para OCR",
        difficulty="basic",
        detectability="medium",
        effectiveness="proven",
        target_models=["OCR-based models"],
        implementation_complexity=4
    ),
    AttackTechnique(
        name="Transparent Text Layers",
        category=AttackCategory.OCR_INJECTION,
        description="Capas de texto con alta transparencia",
        difficulty="basic", 
        detectability="medium",
        effectiveness="proven",
        target_models=["Most Vision Models"],
        implementation_complexity=3
    )
]

# =============================================================================
# CATEGORÍA 2: VISUAL CONFUSION ATTACKS
# =============================================================================
VISUAL_CONFUSION_TECHNIQUES = [
    AttackTechnique(
        name="Optical Illusion Exploitation",
        category=AttackCategory.VISUAL_CONFUSION,
        description="Usa ilusiones ópticas para confundir interpretación",
        difficulty="intermediate",
        detectability="low",
        effectiveness="theoretical",
        target_models=["Vision models with object detection"],
        implementation_complexity=7
    ),
    AttackTechnique(
        name="Ambiguous Object Presentation", 
        category=AttackCategory.VISUAL_CONFUSION,
        description="Objetos que pueden interpretarse de múltiples formas",
        difficulty="intermediate",
        detectability="low",
        effectiveness="theoretical",
        target_models=["Object classification models"],
        implementation_complexity=6
    ),
    AttackTechnique(
        name="Perspective Manipulation",
        category=AttackCategory.VISUAL_CONFUSION,
        description="Cambia perspectiva para ocultar o revelar elementos",
        difficulty="advanced",
        detectability="low", 
        effectiveness="theoretical",
        target_models=["3D-aware vision models"],
        implementation_complexity=8
    ),
    AttackTechnique(
        name="Color Space Exploitation",
        category=AttackCategory.VISUAL_CONFUSION,
        description="Aprovecha diferencias en interpretación de colores",
        difficulty="intermediate",
        detectability="medium",
        effectiveness="theoretical",
        target_models=["Color-sensitive models"],
        implementation_complexity=5
    )
]

# =============================================================================
# CATEGORÍA 3: SEMANTIC MANIPULATION
# =============================================================================
SEMANTIC_MANIPULATION_TECHNIQUES = [
    AttackTechnique(
        name="Context Reframing Attack",
        category=AttackCategory.SEMANTIC_MANIPULATION,
        description="Cambia contexto semántico sin alterar contenido visual",
        difficulty="advanced",
        detectability="low",
        effectiveness="theoretical", 
        target_models=["Context-aware models"],
        implementation_complexity=7
    ),
    AttackTechnique(
        name="Cultural Context Exploitation",
        category=AttackCategory.SEMANTIC_MANIPULATION,
        description="Aprovecha diferencias culturales en interpretación", 
        difficulty="expert",
        detectability="low",
        effectiveness="theoretical",
        target_models=["Culturally-trained models"],
        implementation_complexity=9
    ),
    AttackTechnique(
        name="Metaphorical Misdirection",
        category=AttackCategory.SEMANTIC_MANIPULATION,
        description="Usa metáforas visuales para cambiar interpretación",
        difficulty="advanced",
        detectability="low",
        effectiveness="theoretical",
        target_models=["Language-vision models"],
        implementation_complexity=8
    )
]

# =============================================================================
# CATEGORÍA 4: ADVERSARIAL PERTURBATIONS
# =============================================================================
ADVERSARIAL_PERTURBATIONS_TECHNIQUES = [
    AttackTechnique(
        name="Pixel-level Noise Injection",
        category=AttackCategory.ADVERSARIAL_PERTURBATIONS,
        description="Ruido imperceptible que altera clasificación",
        difficulty="advanced",
        detectability="low",
        effectiveness="proven",
        target_models=["CNN-based vision models"],
        implementation_complexity=8
    ),
    AttackTechnique(
        name="Frequency Domain Attacks",
        category=AttackCategory.ADVERSARIAL_PERTURBATIONS,
        description="Manipulación en dominio de frecuencia",
        difficulty="expert",
        detectability="low",
        effectiveness="proven",
        target_models=["Deep vision networks"], 
        implementation_complexity=9
    ),
    AttackTechnique(
        name="Patch-based Adversarial Examples",
        category=AttackCategory.ADVERSARIAL_PERTURBATIONS,
        description="Pequeños parches que causan misclasificación",
        difficulty="intermediate",
        detectability="medium",
        effectiveness="proven",
        target_models=["Object detection models"],
        implementation_complexity=6
    )
]

# =============================================================================
# CATEGORÍA 5: MULTIMODAL JAILBREAKING
# =============================================================================
MULTIMODAL_JAILBREAKING_TECHNIQUES = [
    AttackTechnique(
        name="Cross-Modal Prompt Injection",
        category=AttackCategory.MULTIMODAL_JAILBREAKING,
        description="Inyecta prompts maliciosos a través de imagen",
        difficulty="advanced",
        detectability="medium",
        effectiveness="proven",
        target_models=["GPT-4V", "Claude-3", "Gemini"],
        implementation_complexity=7
    ),
    AttackTechnique(
        name="Visual Roleplay Induction", 
        category=AttackCategory.MULTIMODAL_JAILBREAKING,
        description="Usa imágenes para inducir roleplay malicioso",
        difficulty="intermediate",
        detectability="medium",
        effectiveness="proven",
        target_models=["Chat-based VLMs"],
        implementation_complexity=5
    ),
    AttackTechnique(
        name="System Message Visualization",
        category=AttackCategory.MULTIMODAL_JAILBREAKING,
        description="Convierte system prompts en elementos visuales",
        difficulty="advanced",
        detectability="high",
        effectiveness="theoretical",
        target_models=["Instruction-following VLMs"],
        implementation_complexity=8
    )
]

# =============================================================================
# ROADMAP DE IMPLEMENTACIÓN SUGERIDO
# =============================================================================
IMPLEMENTATION_ROADMAP = {
    "Week 1": {
        "focus": "OCR Injection Optimization",
        "tasks": [
            "Optimize invisible_text technique (50% → 75%+)",
            "Test against real LLaVA model",
            "Document effective parameter ranges"
        ]
    },
    "Week 2": {
        "focus": "Visual Confusion Development", 
        "tasks": [
            "Implement optical illusion attacks",
            "Develop ambiguous object techniques",
            "Create color space exploitation methods"
        ]
    },
    "Week 3": {
        "focus": "Adversarial Perturbations",
        "tasks": [
            "Implement FGSM-based attacks",
            "Develop frequency domain techniques", 
            "Test patch-based approaches"
        ]
    },
    "Week 4": {
        "focus": "Multimodal Jailbreaking",
        "tasks": [
            "Cross-modal prompt injection",
            "Visual roleplay techniques",
            "System message visualization"
        ]
    },
    "Month 2": {
        "focus": "Advanced Techniques",
        "tasks": [
            "Semantic manipulation methods",
            "Context poisoning attacks",
            "Steganographic command injection"
        ]
    }
}

# =============================================================================
# MATRIZ DE PRIORIDADES
# =============================================================================
def calculate_priority_score(technique: AttackTechnique) -> float:
    """Calcula score de prioridad basado en múltiples factores"""
    
    # Factores de scoring
    effectiveness_scores = {"theoretical": 1, "proven": 3, "weaponized": 5}
    detectability_scores = {"high": 1, "medium": 2, "low": 3} 
    difficulty_scores = {"basic": 3, "intermediate": 2, "advanced": 1, "expert": 0.5}
    
    effectiveness = effectiveness_scores.get(technique.effectiveness, 1)
    detectability = detectability_scores.get(technique.detectability, 1)
    difficulty = difficulty_scores.get(technique.difficulty, 1)
    
    # Complejidad inversa (menos complejo = más prioritario)
    complexity_factor = (11 - technique.implementation_complexity) / 10
    
    # Score final
    priority_score = (effectiveness * detectability * difficulty * complexity_factor)
    
    return round(priority_score, 2)

def get_prioritized_techniques() -> List[tuple]:
    """Retorna todas las técnicas ordenadas por prioridad"""
    
    all_techniques = (OCR_TECHNIQUES + VISUAL_CONFUSION_TECHNIQUES + 
                     SEMANTIC_MANIPULATION_TECHNIQUES + 
                     ADVERSARIAL_PERTURBATIONS_TECHNIQUES +
                     MULTIMODAL_JAILBREAKING_TECHNIQUES)
    
    # Calcular scores y ordenar
    technique_scores = [(tech, calculate_priority_score(tech)) for tech in all_techniques]
    technique_scores.sort(key=lambda x: x[1], reverse=True)
    
    return technique_scores

def print_attack_taxonomy():
    """Imprime taxonomía completa con prioridades"""
    
    print("🎯 TAXONOMÍA DE ATAQUES ADVERSARIALES MULTIMODALES")
    print("=" * 60)
    
    prioritized = get_prioritized_techniques()
    
    print(f"\n📊 TOP 10 TÉCNICAS POR PRIORIDAD:")
    print("-" * 40)
    
    for i, (technique, score) in enumerate(prioritized[:10], 1):
        print(f"{i:2}. {technique.name}")
        print(f"    Categoría: {technique.category.value}")
        print(f"    Score: {score} | Dificultad: {technique.difficulty}")
        print(f"    Efectividad: {technique.effectiveness} | Detectabilidad: {technique.detectability}")
        print()
    
    print(f"\n🗺️ ROADMAP DE IMPLEMENTACIÓN:")
    print("-" * 40)
    
    for period, details in IMPLEMENTATION_ROADMAP.items():
        print(f"\n{period}: {details['focus']}")
        for task in details['tasks']:
            print(f"  • {task}")

if __name__ == "__main__":
    print_attack_taxonomy()
