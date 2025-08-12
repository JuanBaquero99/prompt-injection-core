from dataclasses import dataclass
from typing import List

@dataclass
class Detection:
    """Representa un hallazgo individual de vulnerabilidad"""
    vulnerability_type: str
    confidence: float
    severity: str
    description: str
    evidence: str
    recommendations: List[str]
