from typing import List
from dataclasses import dataclass
from prompt_injection_core.detectors.models import Detection

from prompt_injection_core.detectors.jailbreak import JailbreakDetector
from prompt_injection_core.detectors.leak import SystemLeakDetector

@dataclass
class ScanResult:
    """Resultado global del escaneo"""
    prompt: str
    detections: List[Detection]
    risk_score: int
    vulnerabilities_found: int
    summary: str

class PromptScanner:
    """Escáner principal que ejecuta todos los detectores"""
    def __init__(self):
        self.detectors: List = [
            JailbreakDetector(),
            SystemLeakDetector(),
        ]

    def scan(self, prompt: str) -> ScanResult:
        all_detections = []
        for detector in self.detectors:
            try:
                detections = detector.detect(prompt)
                all_detections.extend(detections)
            except Exception as e:
                print(f"Error en el detector {detector.name}: {e}")
        risk_score = self._calculate_risk_score(all_detections)
        summary = self._generate_summary(all_detections, risk_score)
        return ScanResult(
            prompt=prompt[:100] + "..." if len(prompt) > 100 else prompt,
            detections=all_detections,
            risk_score=risk_score,
            vulnerabilities_found=len(all_detections),
            summary=summary
        )

    def _calculate_risk_score(self, detections: List[Detection]) -> int:
        if not detections:
            return 0
        total_score = 0
        for detection in detections:
            if detection.severity == "HIGH":
                total_score += 50
            elif detection.severity == "MEDIUM":
                total_score += 30
            elif detection.severity == "LOW":
                total_score += 10
        return min(100, total_score)

    def _generate_summary(self, detections: List[Detection], risk_score: int) -> str:
        if not detections:
            return "No vulnerabilities detected. Prompt appears safe."
        severity_counts = {}
        for detection in detections:
            severity_counts[detection.severity] = severity_counts.get(detection.severity, 0) + 1
        if risk_score >= 75:
            risk_level = "CRITICAL"
        elif risk_score >= 50:
            risk_level = "HIGH"
        elif risk_score >= 25:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        summary_parts = [f"{risk_level} risk (Score: {risk_score}/100)"]
        severity_details = []
        for severity in ["HIGH", "MEDIUM", "LOW"]:
            count = severity_counts.get(severity, 0)
            if count > 0:
                severity_details.append(f"{count} {severity}")
        if severity_details:
            summary_parts.append(f"Detections: {', '.join(severity_details)}")
        return " | ".join(summary_parts)
