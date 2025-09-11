"""
Attack Generators Module
========================

Módulo que contiene generadores de ataques adversariales para investigación ética
en seguridad de modelos multimodales.

Generadores disponibles:
- OCRInjectionGenerator: Ataques de inyección de texto oculto vía OCR
- VisualConfusionGenerator: Ataques de confusión visual (próximamente)
- PerturbationGenerator: Perturbaciones adversariales (próximamente)  
- MultimodalJailbreakGenerator: Jailbreaks multimodales (próximamente)

Author: Juan Pablo Baquero
Purpose: Ethical AI security research
"""

from .ocr_injection import OCRInjectionGenerator

__version__ = "0.1.0"
__author__ = "Juan Pablo Baquero"

__all__ = [
    "OCRInjectionGenerator",
    # "VisualConfusionGenerator",    # Semana 2
    # "PerturbationGenerator",       # Semana 3  
    # "MultimodalJailbreakGenerator" # Semana 4
]

# Configuración por defecto para todos los generadores
DEFAULT_CONFIG = {
    "base_image_size": (512, 512),
    "output_dir": "test_cases/generated_attacks", 
    "ethical_mode": True,
    "save_metadata": True
}

def list_available_generators():
    """
    Lista todos los generadores de ataques disponibles.
    
    Returns:
        dict: Diccionario con generadores y sus descripciones
    """
    generators = {
        "OCRInjectionGenerator": {
            "description": "Genera ataques de inyección de texto oculto",
            "techniques": [
                "Invisible text (colores sutiles)",
                "Transparent overlays",
                "Steganographic injection", 
                "Microscopic text"
            ],
            "status": "Implementado",
            "week": 1
        },
        "VisualConfusionGenerator": {
            "description": "Genera ataques de confusión visual",
            "techniques": [
                "Contradictory images",
                "Context hijacking",
                "Optical illusions",
                "Ambiguous visual elements"
            ],
            "status": "Planificado",
            "week": 2
        },
        "PerturbationGenerator": {
            "description": "Genera perturbaciones adversariales imperceptibles",
            "techniques": [
                "FGSM adaptado",
                "PGD multimodal",
                "Semantic perturbations",
                "Transferable attacks"
            ],
            "status": "Planificado", 
            "week": 3
        },
        "MultimodalJailbreakGenerator": {
            "description": "Genera jailbreaks combinando imagen y texto",
            "techniques": [
                "Cross-modal instruction splitting",
                "Visual context hijacking",
                "Modal confusion attacks",
                "Context pollution"
            ],
            "status": "Planificado",
            "week": 4
        }
    }
    
    return generators

def create_attack_suite():
    """
    Crea una suite completa de generadores de ataques.
    
    Returns:
        dict: Diccionario con todos los generadores inicializados
    """
    suite = {}
    
    # OCR Injection Generator (disponible)
    suite['ocr_injection'] = OCRInjectionGenerator()
    
    # Otros generadores se agregarán cuando estén implementados
    # suite['visual_confusion'] = VisualConfusionGenerator()
    # suite['perturbation'] = PerturbationGenerator()  
    # suite['multimodal_jailbreak'] = MultimodalJailbreakGenerator()
    
    return suite

# Metadata del módulo
ETHICAL_DISCLAIMER = """
AVISO ÉTICO Y LEGAL:
===================

Este módulo está diseñado exclusivamente para:
- Investigación académica en seguridad de IA
- Testing ético de vulnerabilidades
- Mejora de sistemas de defensa
- Educación en ciberseguridad

USO PROHIBIDO:
- Testing no autorizado en sistemas de producción
- Ataques maliciosos reales
- Violación de términos de servicio
- Cualquier uso que cause daño

RESPONSABILIDAD:
El usuario es completamente responsable del uso ético y legal
de estas herramientas. Todos los hallazgos deben ser reportados
siguiendo protocolos de responsible disclosure.

CONTACTO: baquerojuan99@gmail.com
"""

def print_ethical_disclaimer():
    """Muestra el aviso ético al importar el módulo."""
    print(ETHICAL_DISCLAIMER)
