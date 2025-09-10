"""
scanner.py
----------
Main scanner module for running all prompt injection detectors.
Provides unified scanning, risk scoring, and summary generation for prompts.
"""

from typing import List
from dataclasses import dataclass
from detectors.models import Detection
from detectors.jailbreak import JailbreakDetector
from detectors.leak import SystemLeakDetector
from detectors.roleplay import RolePlayDetector

@dataclass
class ScanResult:
    """
    Global scan result for a prompt, including detections, risk score, and summary.
    """
    prompt: str
    detections: List[Detection]
    risk_score: int
    vulnerabilities_found: int
    summary: str

class PromptScanner:
    """
    Main scanner that runs all enabled detectors on a prompt.
    """
    def __init__(self, enabled_detectors=None, confidence_threshold=0.0):
        from detectors.ml_detector import MLDetector
        all_detectors = [
            JailbreakDetector(),
            SystemLeakDetector(),
            RolePlayDetector(),
            MLDetector(),  # ML detector with default threshold 0.7
        ]
        if enabled_detectors is not None:
            self.detectors = [d for d in all_detectors if d.__class__.__name__ in enabled_detectors]
        else:
            self.detectors = all_detectors
        self.confidence_threshold = confidence_threshold

    def scan(self, prompt: str) -> ScanResult:
        """
        Run all detectors on the given prompt and return a ScanResult.
        Filters detections by minimum confidence threshold.
        """
        all_detections = []
        for detector in self.detectors:
            try:
                detections = detector.detect(prompt)
                detections = [d for d in detections if d.confidence >= self.confidence_threshold]
                all_detections.extend(detections)
            except Exception as e:
                print(f"Error in detector {detector.name}: {e}")
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
        """
        Calculate a global risk score based on all detections.
        """
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
