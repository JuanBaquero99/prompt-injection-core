from abc import ABC, abstractmethod
from .models import Detection
from typing import List

class Detector(ABC):
    """Clase base para todos los detectores"""
    def __init__(self):
        self.name = self.__class__.__name__
        self.version = "1.0.0"

    @abstractmethod
    def detect(self, prompt: str) -> List[Detection]:
        pass
