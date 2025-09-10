"""
Base detector class para todos los detectores de PERSONA
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from .types import SecurityResult

class BaseDetector(ABC):
    """Base class para todos los detectores de seguridad"""
    
    def __init__(self, name: str):
        self.name = name
        self.enabled = True
    
    @abstractmethod
    def detect(self, input_data: Any) -> SecurityResult:
        """Detectar amenazas en el input"""
        pass
    
    def enable(self):
        """Habilitar detector"""
        self.enabled = True
    
    def disable(self):
        """Deshabilitar detector"""
        self.enabled = False
