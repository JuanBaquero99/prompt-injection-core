"""
`detectors` package - Entry point.

This module exposes the main classes and detectors of the package for use
in other components of the project, preventing client code from importing
directly from internal files.

Public elements:
- Detector: Base class for all detectors.
- Detection: Data model representing a finding.
- JailbreakDetector: Detector specialized in identifying jailbreak attempts.
- SystemLeakDetector: Detector specialized in detecting system prompt leaks.
"""

from .base import Detector
from .models import Detection
from .jailbreak import JailbreakDetector
from .leak import SystemLeakDetector

__all__ = [
    "Detector",
    "Detection",
    "JailbreakDetector",
    "SystemLeakDetector",
]
