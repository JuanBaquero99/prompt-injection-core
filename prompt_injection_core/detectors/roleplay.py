"""
RolePlayDetector - Detects role manipulation attempts in prompts.

This detector identifies instructions that attempt to change the model's role,
persona, or behavior by using specific patterns. Such prompts can be used to
bypass safety mechanisms or alter the intended functioning of the model.

Detection logic:
- Uses predefined regular expressions to match phrases like:
  - "act as a hacker"
  - "pretend to be a developer"
  - "you are now an admin"
  - "from now on, you are a teacher"
  - "assume the role of a doctor"

Attributes:
    patterns (List[str]): List of regex patterns representing role manipulation attempts.

Methods:
    detect(prompt: str) -> List[Detection]:
        Scans the given prompt for role manipulation patterns and returns
        a list of Detection objects when matches are found.

Returns:
    List[Detection]: A list of detections containing vulnerability details,
    evidence, and recommendations.

Severity:
    MEDIUM — Role manipulation can be used as a stepping stone for jailbreaks
    or to bypass content filters, but may not always pose an immediate high-risk.

Recommendations:
    - Review prompts that attempt to alter the model's role.
    - Implement strict separation and validation between system and user instructions.
"""

import re
from typing import List
from .base import Detector
from .models import Detection

class RolePlayDetector(Detector):
    """Detecta intentos de manipulación de rol en prompts"""
    def __init__(self):
        super().__init__()
        self.patterns = [
            r"act\s+as\s+(?:an?|the)?\s*(hacker|admin|developer|doctor|teacher|bot|assistant)",
            r"pretend\s+to\s+be\s+(?:an?|the)?\s*(hacker|admin|developer|doctor|teacher|bot|assistant)",
            r"you\s+are\s+now\s+(?:an?|the)?\s*(hacker|admin|developer|doctor|teacher|bot|assistant)",
            r"from\s+now\s+on,\s*you\s+are\s+(?:an?|the)?\s*(hacker|admin|developer|doctor|teacher|bot|assistant)",
            r"assume\s+the\s+role\s+of\s+(?:an?|the)?\s*(hacker|admin|developer|doctor|teacher|bot|assistant)",
            r"impersonate\s+(?:an?|the)?\s*(hacker|admin|developer|doctor|teacher|bot|assistant)",
        ]
        self.ignore_patterns = [
            r"i am a chatbot",
            r"i am an assistant",
            r"i am a bot",
            r"i am an ai",
            r"what is the weather",
        ]

    def detect(self, prompt: str) -> List[Detection]:
        # Ignorar patrones benignos
        for ignore_pattern in self.ignore_patterns:
            if re.search(ignore_pattern, prompt, re.IGNORECASE):
                return []
        detections = []
        for pattern in self.patterns:
            match = re.search(pattern, prompt, re.IGNORECASE)
            if match:
                rol = match.group(1).lower() if match.lastindex else ""
                # Severidad y confianza según el rol
                if rol in ["hacker", "admin", "developer"]:
                    severity = "HIGH"
                    confidence = 0.95
                elif rol in ["doctor", "teacher", "bot", "assistant"]:
                    severity = "MEDIUM"
                    confidence = 0.8
                else:
                    severity = "LOW"
                    confidence = 0.6
                detections.append(Detection(
                    vulnerability_type="Role Manipulation",
                    confidence=confidence,
                    severity=severity,
                    description=f"Role manipulation attempt detected for role: {rol}",
                    evidence=pattern,
                    recommendations=[
                        "Revisar prompts que intentan cambiar el rol del modelo.",
                        "Implementar validación y separación estricta entre instrucciones del sistema y del usuario."
                    ],
                    detector=self
                ))
        return detections