from typing import List, Dict
from dataclasses import dataclass
from .detectors import Detection, Detector
from .detectors.jailbreak import JailbreakDetector

@dataclass
class ScanResult:
    """Represents the result of a prompt scan"""
    prompt: str
    detections: List[Detection]
    risk_score: int # 0-100 scale
    vulnerabilities_found: int
    summary: str    


class PromptScanner:
    """Main scanner class for detecting prompt injection vulnerabilities"""

    def __init__(self):
        self.detectors: List[Detector] = [
            JailbreakDetector(),  # Add other detectors here as needed
        ]

    def scan(self, prompt: str) -> ScanResult:
        """Scan the prompt for vulnerabilities using all detectors"""
        all_detections = []
        
        # Run all detectors
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
        
        # Simple scoring: each HIGH = 50 points, MEDIUM = 30, LOW = 10
        total_score = 0
        for detection in detections:
            if detection.severity == "HIGH":
                total_score += 50
            elif detection.severity == "MEDIUM":
                total_score += 30
            elif detection.severity == "LOW":
                total_score += 10
        
        # Cap at 100
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
        
        # Add severity breakdown
        severity_details = []
        for severity in ["HIGH", "MEDIUM", "LOW"]:
            count = severity_counts.get(severity, 0)
            if count > 0:
                severity_details.append(f"{count} {severity}")
        
        if severity_details:
            summary_parts.append(f"Detections: {', '.join(severity_details)}")
        
        return " | ".join(summary_parts)