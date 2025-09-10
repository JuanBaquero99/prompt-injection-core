"""
Detector Experimental: Educational Disguise Detector
===================================================
Detecta ataques de prompt injection camuflados como solicitudes educativas.

Patrones comunes:
- "Para un proyecto de [materia], necesito..."
- "Con fines educativos, ¿puedes mostrar...?"
- "Estoy investigando sobre [tema de seguridad]..."
- "Para entender mejor los riesgos..."
"""

from typing import List, Dict, Any
import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from prompt_injection_core.detectors import Detector, Detection

class EducationalDisguiseDetector(Detector):
    """Detecta ataques camuflados como solicitudes educativas"""
    
    def __init__(self):
        super().__init__(name="EducationalDisguiseDetector")
        
        # Patrones de camuflaje educativo
        self.educational_phrases = [
            r"para\s+(?:un\s+)?proyecto\s+(?:de\s+)?(?:ciberseguridad|seguridad|hacking)",
            r"con\s+fines\s+educativos",
            r"estoy\s+(?:investigando|estudiando)\s+(?:sobre\s+)?(?:vulnerabilidades|ataques|exploits)",
            r"para\s+(?:entender|comprender)\s+(?:mejor\s+)?(?:los\s+)?(?:riesgos|vulnerabilidades)",
            r"(?:como\s+)?ejemplo\s+(?:de\s+)?(?:ataque|vulnerabilidad|exploit)",
            r"para\s+(?:documentar|analizar)\s+vulnerabilidades",
            r"en\s+un\s+entorno\s+controlado",
            r"solo\s+(?:para\s+)?(?:pruebas|testing|investigación)",
        ]
        
        # Patrones de solicitudes sospechosas post-educativo
        self.suspicious_requests = [
            r"(?:muestra|enseña|proporciona)\s+(?:me\s+)?ejemplos?\s+de",
            r"¿?(?:cómo|como)\s+(?:podría|puedo)\s+(?:evadir|burlar|saltear)",
            r"¿?(?:cuáles|que)\s+(?:son\s+)?(?:las\s+)?(?:técnicas|métodos|formas)",
            r"genera(?:r)?\s+(?:un\s+)?(?:prompt|código|script)\s+(?:que|para)",
            r"explica\s+(?:el\s+)?(?:proceso|método)\s+(?:de|para)",
            r"¿?qué\s+(?:tipo\s+de\s+)?(?:vulnerabilidades|exploits|ataques)",
        ]
        
        # Términos técnicos sospechosos en contexto educativo
        self.technical_terms = [
            r"prompt\s+injection",
            r"system\s+prompt",
            r"bypass\s+(?:security|filters)",
            r"jailbreak(?:ing)?",
            r"escape\s+(?:sequences|characters)",
            r"privilege\s+escalation",
            r"buffer\s+overflow",
            r"sql\s+injection",
            r"xss\s+(?:attack)?",
            r"reverse\s+shell",
        ]
    
    def detect(self, prompt: str) -> List[Detection]:
        """Detecta patrones de camuflaje educativo con intención maliciosa"""
        detections = []
        prompt_lower = prompt.lower()
        
        # Buscar patrones educativos
        educational_matches = []
        for pattern in self.educational_phrases:
            matches = re.findall(pattern, prompt_lower, re.IGNORECASE)
            educational_matches.extend(matches)
        
        # Si no hay camuflaje educativo, no es relevante para este detector
        if not educational_matches:
            return detections
        
        # Buscar solicitudes sospechosas
        suspicious_matches = []
        for pattern in self.suspicious_requests:
            matches = re.findall(pattern, prompt_lower, re.IGNORECASE)
            suspicious_matches.extend(matches)
        
        # Buscar términos técnicos
        technical_matches = []
        for pattern in self.technical_terms:
            matches = re.findall(pattern, prompt_lower, re.IGNORECASE)
            technical_matches.extend(matches)
        
        # Calcular score de sospecha
        suspicion_score = 0
        evidence_parts = []
        
        # Peso por camuflaje educativo
        if educational_matches:
            suspicion_score += 0.3
            evidence_parts.append(f"Camuflaje educativo: {educational_matches[0]}")
        
        # Peso por solicitudes sospechosas  
        suspicion_score += len(suspicious_matches) * 0.2
        if suspicious_matches:
            evidence_parts.append(f"Solicitud sospechosa: {suspicious_matches[0]}")
        
        # Peso por términos técnicos
        suspicion_score += len(technical_matches) * 0.15
        if technical_matches:
            evidence_parts.append(f"Términos técnicos: {', '.join(technical_matches[:2])}")
        
        # Determinar severidad basada en score
        if suspicion_score >= 0.7:
            severity = "HIGH"
            confidence = min(0.95, suspicion_score)
        elif suspicion_score >= 0.5:
            severity = "MEDIUM"  
            confidence = min(0.80, suspicion_score)
        elif suspicion_score >= 0.35:
            severity = "LOW"
            confidence = min(0.65, suspicion_score)
        else:
            return detections  # No suficiente evidencia
        
        # Crear detección
        detection = Detection(
            vulnerability_type="Educational Disguise Attack",
            confidence=confidence,
            severity=severity,
            description=f"Posible ataque camuflado como solicitud educativa (score: {suspicion_score:.2f})",
            evidence=" | ".join(evidence_parts),
            recommendations=[
                "Verificar la legitimidad de la solicitud educativa",
                "Evaluar si la información solicitada es apropiada",
                "Considerar proporcionar información general en lugar de específica",
                "Documentar el caso para análisis posterior"
            ],
            detector=self.name
        )
        
        detections.append(detection)
        return detections
    
    def analyze_intent_discrepancy(self, prompt: str) -> Dict[str, Any]:
        """Análisis experimental de discrepancia entre intención aparente y real"""
        prompt_lower = prompt.lower()
        
        # Contar indicadores educativos vs maliciosos
        educational_indicators = sum(1 for pattern in self.educational_phrases 
                                   if re.search(pattern, prompt_lower))
        
        malicious_indicators = sum(1 for pattern in self.suspicious_requests + self.technical_terms
                                 if re.search(pattern, prompt_lower))
        
        # Ratio de discrepancia
        total_indicators = educational_indicators + malicious_indicators
        if total_indicators == 0:
            discrepancy_ratio = 0
        else:
            discrepancy_ratio = malicious_indicators / total_indicators
        
        return {
            "educational_signals": educational_indicators,
            "malicious_signals": malicious_indicators,
            "discrepancy_ratio": discrepancy_ratio,
            "interpretation": self._interpret_discrepancy(discrepancy_ratio)
        }
    
    def _interpret_discrepancy(self, ratio: float) -> str:
        """Interpreta el ratio de discrepancia"""
        if ratio >= 0.7:
            return "Alto riesgo: Camuflaje probable"
        elif ratio >= 0.5:
            return "Riesgo medio: Evaluar contexto"
        elif ratio >= 0.3:
            return "Riesgo bajo: Posible solicitud legítima"
        else:
            return "Solicitud aparentemente legítima"
