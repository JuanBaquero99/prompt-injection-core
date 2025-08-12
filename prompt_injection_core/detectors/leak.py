import re
from typing import List
from .base import Detector
from .models import Detection

class SystemLeakDetector(Detector):
    def __init__(self):
        super().__init__()
        self.patterns = [
            r"(system prompt|internal instructions|your config|show.*instructions|reveal.*prompt)",
            r"(what.*are.*your.*instructions)",
            r"(print.*system.*prompt)",
        ]

    def detect(self, prompt: str) -> List[Detection]:
        detections = []
        for pattern in self.patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                detections.append(Detection(
                    vulnerability_type="System Prompt Leak",
                    confidence=0.85,
                    severity="HIGH",
                    description="Possible attempt to leak system prompt or internal instructions.",
                    evidence=pattern,
                    recommendations=[
                        "Sanitize user input.",
                        "Avoid exposing internal instructions in responses."
                    ]
                ))
        return detections