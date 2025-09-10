"""
Types y estructuras de datos para PERSONA
"""
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any, Optional

class ThreatLevel(Enum):
    """Niveles de amenaza"""
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class ThreatCategory(Enum):
    """Categorías de amenazas por fase"""
    # Fase 1: Input Security
    PROMPT_INJECTION = "prompt_injection"
    ADVERSARIAL_EXAMPLES = "adversarial_examples"
    MULTIMODAL_ATTACKS = "multimodal_attacks"
    
    # Fase 2: Data Security
    DATA_POISONING = "data_poisoning"
    BACKDOOR_ATTACKS = "backdoor_attacks"
    
    # Fase 3: Model Extraction
    MODEL_THEFT = "model_theft"
    MODEL_INVERSION = "model_inversion"
    DATA_LEAKAGE = "data_leakage"
    
    # Fase 4: Infrastructure
    SUPPLY_CHAIN = "supply_chain"
    DOS_ATTACKS = "dos_attacks"
    
    # Fase 5: Ethics & Compliance
    BIAS_DETECTION = "bias_detection"
    DEEPFAKES = "deepfakes"

@dataclass
class SecurityResult:
    """Resultado de una detección de seguridad"""
    threat_detected: bool
    threat_level: ThreatLevel
    threat_category: ThreatCategory
    confidence: float
    details: Dict[str, Any]
    recommendations: List[str]
    detector_name: str
    
    @property
    def risk_score(self) -> int:
        """Score de riesgo 0-100"""
        base_score = self.threat_level.value * 20
        confidence_multiplier = self.confidence
        return int(base_score * confidence_multiplier)

@dataclass
class PhaseResult:
    """Resultado de análisis de una fase completa"""
    phase_name: str
    detections: List[SecurityResult]
    overall_risk_score: int
    summary: str
    
    @property
    def has_threats(self) -> bool:
        return any(d.threat_detected for d in self.detections)
    
    @property
    def max_threat_level(self) -> ThreatLevel:
        if not self.detections:
            return ThreatLevel.NONE
        return max(d.threat_level for d in self.detections)

@dataclass
class PersonaAnalysisResult:
    """Resultado completo del análisis PERSONA"""
    input_data: Any
    phase_results: Dict[str, PhaseResult]
    overall_risk_score: int
    execution_time: float
    recommendations: List[str]
    
    @property
    def has_any_threats(self) -> bool:
        return any(pr.has_threats for pr in self.phase_results.values())
    
    @property
    def critical_threats(self) -> List[SecurityResult]:
        """Amenazas críticas encontradas"""
        critical = []
        for phase_result in self.phase_results.values():
            critical.extend([
                d for d in phase_result.detections 
                if d.threat_level == ThreatLevel.CRITICAL
            ])
        return critical
