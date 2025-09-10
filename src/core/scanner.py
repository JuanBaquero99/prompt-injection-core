"""
PERSONA Unified Scanner - Orquestador principal
"""
from typing import Any, Dict, List, Optional
import time
from .types import PersonaAnalysisResult, PhaseResult, ThreatLevel
from .base_detector import BaseDetector

class UnifiedScanner:
    """Scanner unificado para todas las fases de PERSONA"""
    
    def __init__(self):
        self.phases: Dict[str, List[BaseDetector]] = {
            "phase1_input_security": [],
            "phase2_data_security": [],
            "phase3_extraction": [],
            "phase4_infrastructure": [],
            "phase5_ethics": []
        }
        self.enabled_phases = set(self.phases.keys())
    
    def register_detector(self, phase: str, detector: BaseDetector):
        """Registrar un detector en una fase"""
        if phase in self.phases:
            self.phases[phase].append(detector)
        else:
            raise ValueError(f"Phase {phase} not recognized")
    
    def enable_phase(self, phase: str):
        """Habilitar una fase específica"""
        self.enabled_phases.add(phase)
    
    def disable_phase(self, phase: str):
        """Deshabilitar una fase específica"""
        self.enabled_phases.discard(phase)
    
    def scan(self, input_data: Any, phases: Optional[List[str]] = None) -> PersonaAnalysisResult:
        """
        Realizar análisis completo de seguridad
        
        Args:
            input_data: Datos a analizar
            phases: Fases específicas a ejecutar (None = todas las habilitadas)
        """
        start_time = time.time()
        
        target_phases = phases or list(self.enabled_phases)
        phase_results = {}
        
        for phase_name in target_phases:
            if phase_name not in self.phases:
                continue
                
            detectors = self.phases[phase_name]
            detections = []
            
            for detector in detectors:
                if detector.enabled:
                    try:
                        result = detector.detect(input_data)
                        detections.append(result)
                    except Exception as e:
                        # Log error but continue
                        print(f"Error in detector {detector.name}: {e}")
            
            # Calcular risk score de la fase
            phase_risk = self._calculate_phase_risk(detections)
            phase_summary = self._generate_phase_summary(detections)
            
            phase_results[phase_name] = PhaseResult(
                phase_name=phase_name,
                detections=detections,
                overall_risk_score=phase_risk,
                summary=phase_summary
            )
        
        execution_time = time.time() - start_time
        overall_risk = self._calculate_overall_risk(phase_results)
        recommendations = self._generate_recommendations(phase_results)
        
        return PersonaAnalysisResult(
            input_data=input_data,
            phase_results=phase_results,
            overall_risk_score=overall_risk,
            execution_time=execution_time,
            recommendations=recommendations
        )
    
    def _calculate_phase_risk(self, detections: List) -> int:
        """Calcular risk score de una fase"""
        if not detections:
            return 0
        
        max_risk = max(d.risk_score for d in detections)
        avg_risk = sum(d.risk_score for d in detections) / len(detections)
        
        # Combinar max y promedio
        return int(max_risk * 0.7 + avg_risk * 0.3)
    
    def _calculate_overall_risk(self, phase_results: Dict) -> int:
        """Calcular risk score general"""
        if not phase_results:
            return 0
        
        phase_risks = [pr.overall_risk_score for pr in phase_results.values()]
        return max(phase_risks) if phase_risks else 0
    
    def _generate_phase_summary(self, detections: List) -> str:
        """Generar resumen de fase"""
        if not detections:
            return "No threats detected"
        
        threat_count = sum(1 for d in detections if d.threat_detected)
        if threat_count == 0:
            return "No threats detected"
        
        return f"{threat_count} threat(s) detected"
    
    def _generate_recommendations(self, phase_results: Dict) -> List[str]:
        """Generar recomendaciones generales"""
        recommendations = []
        
        for phase_result in phase_results.values():
            for detection in phase_result.detections:
                if detection.threat_detected:
                    recommendations.extend(detection.recommendations)
        
        # Eliminar duplicados preservando orden
        seen = set()
        unique_recs = []
        for rec in recommendations:
            if rec not in seen:
                seen.add(rec)
                unique_recs.append(rec)
        
        return unique_recs[:10]  # Máximo 10 recomendaciones
