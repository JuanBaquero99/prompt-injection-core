"""
Module: base
Defines the abstract base class for all detectors in the package.

This class provides a common interface and shared attributes
(name, version) for any specific vulnerability detectors, such as
JailbreakDetector or SystemLeakDetector.

Classes:
- Detector: Abstract base class that all detectors must inherit from.
            It enforces the implementation of the `detect` method.

Usage:
- Inherit from `Detector` to create a custom detection module.
- Implement the `detect` method to analyze a given prompt and return
  a list of `Detection` objects.

Example:
    class MyCustomDetector(Detector):
        def detect(self, prompt: str) -> List[Detection]:
            # Your detection logic here
            return []
"""
from abc import ABC, abstractmethod
from .models import Detection
from typing import List

class Detector(ABC):
    """Clase base para todos los detectores"""
    def __init__(self, name=None):
        self.name = name or self.__class__.__name__
        self.version = "1.0.0"

    @abstractmethod
    def detect(self, prompt: str) -> List[Detection]:
        pass
