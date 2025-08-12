
import re
from typing import List
from .base import Detector
from .models import Detection

class JailbreakDetector(Detector):
    """Detecta intentos de jailbreak en prompts"""
    def __init__(self):
        super().__init__()
        self.patterns = [
            r"ignore\s+(?:all\s+)?(?:previous\s+)?instructions",
            r"forget\s+(?:all\s+)?(?:previous\s+)?instructions",
            r"disregard\s+(?:all\s+)?(?:previous\s+)?instructions",
            r"you\s+are\s+now\s+(?:a\s+)?(?:different|new)",
            r"pretend\s+(?:that\s+)?you\s+are",
            r"act\s+(?:as|like)\s+(?:if\s+)?you\s+are",
        ]

    def detect(self, prompt: str) -> List[Detection]:
        detections = []
        for pattern in self.patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                detections.append(Detection(
                    vulnerability_type="Jailbreak Attempt",
                    confidence=0.9,
                    severity="HIGH",
                    description=f"Detected a potential jailbreak attempt using pattern: {pattern}",
                    evidence=pattern,
                    recommendations=[
                        "Review the prompt for security vulnerabilities.",
                        "Implement input validation to prevent such attempts."
                    ]
                ))
        return detections