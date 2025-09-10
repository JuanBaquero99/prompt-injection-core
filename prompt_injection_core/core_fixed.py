from typing import List
from dataclasses import dataclass
from .detectors import Detection, Detector
from .detectors.jailbreak import JailbreakDetector
from .detectors.ml_detector import MLDetector

@dataclass
class ScanResult:
    """Represents the result of a prompt scan"""
    prompt: str
    detections: List[Detection]
    risk_score: int  # 0-100 scale
    vulnerabilities_found: int
    summary: str    

class MLDetectorAdapter(Detector):
    """Adapter to integrate MLDetector into the same interface as rule-based detectors."""
    def __init__(self):
        super().__init__(name="MLDetector")
        self.model = MLDetector()

    def detect(self, prompt: str) -> List[Detection]:
        result = self.model.predict(prompt)
        detections = []
        if result['prediction'] == 'malicious':
            prob = result['prob_malicious']
            severity = None
            if prob >= 0.9:
                severity = "HIGH"
            elif prob >= 0.8:
                severity = "MEDIUM"
            # Solo se genera detección si la probabilidad es >= 0.8
            if severity:
                detections.append(Detection(
                    vulnerability_type="ML Prompt Injection",
                    confidence=prob,
                    severity=severity,
                    description="ML model detected possible prompt injection",
                    evidence=prompt,
                    recommendations=["Revisar el prompt", "Aplicar filtros adicionales"],
                    detector=self.name
                ))
        return detections

class PromptScanner:
    """Main scanner class for detecting prompt injection vulnerabilities"""
    def __init__(self, use_ml=False):
        self.detectors: List[Detector] = [JailbreakDetector()]
        if use_ml:
            self.detectors.append(MLDetectorAdapter())

    def scan(self, prompt: str) -> ScanResult:
        """Scan the prompt for vulnerabilities using all detectors"""
        all_detections = []
        for detector in self.detectors:
            try:
                detections = detector.detect(prompt)
                all_detections.extend(detections)
            except Exception as e:
                print(f"Error in detector {detector.name}: {e}")

        # Calculate metrics
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
        """Calculate risk score from 0-100 based on detections"""
        if not detections:
            return 0

        total_score = sum(
            50 if d.severity == "HIGH" else
            30 if d.severity == "MEDIUM" else
            10 for d in detections
        )
        return min(100, total_score)

    def _generate_summary(self, detections: List[Detection], risk_score: int) -> str:
        """Generate a summary of the scan results"""
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

        severity_details = [
            f"{count} {severity}"
            for severity, count in severity_counts.items()
            if count > 0
        ]
        if severity_details:
            summary_parts.append(f"Detections: {', '.join(severity_details)}")

        return " | ".join(summary_parts)
