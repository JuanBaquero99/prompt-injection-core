"""
Prompt Injection Core - Library for detecting prompt injection vulnerabilities in LLMs
"""

__version__ = "0.1.0"
__author__ = "Juan Pablo Baquero"
__email__ = "baquerojuan99@gmail.com"

# Import main classes
from .scanner.scanner import PromptScanner, ScanResult
from .detectors import Detection, Detector, JailbreakDetector, SystemLeakDetector

__all__ = [
    "PromptScanner",      # Main scanner class
    "ScanResult",         # Scan result data class
    "Detection",          # Individual detection result
    "Detector",           # Base detector class
    "JailbreakDetector",  # Jailbreak detection
    "SystemLeakDetector", # System prompt leak detection
]

