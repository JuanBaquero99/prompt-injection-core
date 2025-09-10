"""
Module: leak.py
---------------

This module defines the `SystemLeakDetector` class, which specializes in detecting
attempts to reveal the system prompt, hidden configurations, or internal instructions
of the AI model.

A system prompt leak attempt occurs when a prompt is crafted to extract sensitive
information about the model's operational setup, configuration, or instructions,
potentially compromising system security.

Classes:
- SystemLeakDetector: Inherits from `Detector` and implements detection logic
  using predefined regular expression patterns.

Detection process:
1. The detector scans the input prompt against a set of regex patterns that match
   common system prompt leak attempts.
2. If a match is found, a `Detection` object is created with:
   - Vulnerability type ("System Prompt Leak").
   - Confidence score of 0.85.
   - Severity marked as "HIGH".
   - A generic description of the potential leak attempt.
   - Recommendations to sanitize inputs and prevent exposing internal details.

Usage:
- Instantiate `SystemLeakDetector` and call `.detect(prompt)` to return a list of
  `Detection` objects containing any matches for system prompt leak attempts.
"""

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