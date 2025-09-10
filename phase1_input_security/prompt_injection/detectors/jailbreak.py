"""
Module: jailbreak.py
---------------------

This module defines the `JailbreakDetector` class, which specializes in detecting
prompt injection attempts that aim to bypass model restrictions, known as "jailbreaks."

A jailbreak attempt is typically an instruction designed to override, ignore, or replace
the model's existing system prompt or rules, enabling unauthorized or unsafe behavior.

Classes:
- JailbreakDetector: Inherits from `Detector` and implements detection logic
  using predefined regular expression patterns.

Detection process:
1. The detector scans the given prompt against a set of known jailbreak patterns.
2. If a match is found, a `Detection` object is created with:
   - Vulnerability type ("Jailbreak Attempt").
   - High confidence score (0.9).
   - Severity marked as "HIGH".
   - Description including the matched pattern.
   - Recommendations for mitigation.

Usage:
- Instantiate `JailbreakDetector` and call `.detect(prompt)` to receive a list of
  `Detection` objects for any suspicious jailbreak attempts found in the text.
"""

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