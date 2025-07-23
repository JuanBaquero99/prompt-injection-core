from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Detection:
    """Represents a single vulnerability detection"""
    vulnerability_type: str  # e.g., "Jailbreak Attempt"
    confidence: float        # 0.0 - 1.0
    severity: str           # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    description: str        # Human-readable description
    evidence: str          # What triggered the detection
    recommendations: List[str]  # How to fix it

class Detector(ABC):
    """Abstract base class for all detectors"""
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.version = "1.0.0"
    
    @abstractmethod
    def detect(self, prompt: str) -> List[Detection]:
        """Detect vulnerabilities in the given prompt"""
        pass
