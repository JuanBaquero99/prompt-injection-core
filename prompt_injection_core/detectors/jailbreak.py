import re 
from typing import List
from . import Detector, Detection

class JailbreakDetector(Detector):
    """Detects jailbreak attempts in prompts"""
    
    def __init__(self):
        super().__init__()
        # Common jailbreak patterns
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
        
        # Check for common jailbreak patterns
        for pattern in self.patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                # Found a match!
                detection = Detection(
                    vulnerability_type="Jailbreak Attempt",
                    confidence=0.9,  # High confidence for known patterns
                    severity="HIGH",
                    description=f"Detected a potential jailbreak attempt using pattern: {pattern}",
                    evidence=pattern,
                    recommendations=[
                        "Review the prompt for security vulnerabilities.",
                        "Implement input validation to prevent such attempts."
                    ]
                )
                detections.append(detection)
        
        return detections