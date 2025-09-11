#!/usr/bin/env python3
"""
Simplified Attack Testing
=========================

Testing simplificado usando análisis directo de imágenes.
Mientras configuramos LLaVA, podemos hacer análisis básico de nuestros ataques.

Autor: PERSONA Framework Team
"""

import os
import json
from typing import Dict, List, Any
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pytesseract
import cv2
import numpy as np

class SimplifiedAttackAnalyzer:
    """Analizador simplificado de ataques."""
    
    def __init__(self, attack_dir: str = "real_testing_results"):
        """
        Inicializa el analizador.
        
        Args:
            attack_dir: Directorio con ataques generados
        """
        self.attack_dir = attack_dir
        
        print("🔍 Simplified Attack Analyzer inicializado")
        print(f"📁 Directorio de ataques: {attack_dir}")
    
    def analyze_ocr_readability(self, image_path: str) -> Dict[str, Any]:
        """
        Analiza qué tan bien se puede leer el texto oculto con OCR básico.
        
        Args:
            image_path: Path a la imagen
            
        Returns:
            Análisis de legibilidad OCR
        """
        try:
            # Cargar imagen
            image = Image.open(image_path)
            
            # Convertir a numpy para análisis
            img_array = np.array(image)
            
            # Análisis con pytesseract (si está disponible)
            try:
                # OCR básico
                text_detected = pytesseract.image_to_string(image)
                confidence = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
                avg_confidence = np.mean([int(conf) for conf in confidence['conf'] if int(conf) > 0])
                
                ocr_analysis = {
                    "text_detected": text_detected.strip(),
                    "avg_confidence": avg_confidence,
                    "has_text": len(text_detected.strip()) > 0
                }
                
            except Exception as e:
                # Fallback sin pytesseract
                ocr_analysis = {
                    "text_detected": "OCR_NOT_AVAILABLE",
                    "avg_confidence": 0,
                    "has_text": False,
                    "ocr_error": str(e)
                }
            
            # Análisis de propiedades de imagen
            image_properties = {
                "size": image.size,
                "mode": image.mode,
                "format": image.format,
                "has_transparency": image.mode in ('RGBA', 'LA'),
                "colors_detected": len(set(img_array.flatten())) if len(img_array.shape) == 2 else "RGB_IMAGE"
            }
            
            return {
                "image_path": image_path,
                "ocr_analysis": ocr_analysis,
                "image_properties": image_properties,
                "analysis_successful": True
            }
            
        except Exception as e:
            return {
                "image_path": image_path,
                "error": str(e),
                "analysis_successful": False
            }
    
    def analyze_attack_sophistication(self, image_path: str) -> Dict[str, Any]:
        """
        Analiza la sofisticación del ataque basado en el nombre y propiedades.
        
        Args:
            image_path: Path a la imagen
            
        Returns:
            Análisis de sofisticación
        """
        filename = os.path.basename(image_path)
        
        # Determinar tipo de ataque
        if 'ocr_' in filename:
            attack_category = "OCR"
            
            if 'invisible_text' in filename:
                technique = "invisible_text"
                sophistication_score = 0.3
                expected_behavior = "Text with same color as background"
                
            elif 'steganographic' in filename:
                technique = "steganographic"
                sophistication_score = 0.9
                expected_behavior = "Data hidden in LSB of pixels"
                
            elif 'transparent_overlay' in filename:
                technique = "transparent_overlay"
                sophistication_score = 0.5
                expected_behavior = "Transparent layers with text"
                
            elif 'microscopic_text' in filename:
                technique = "microscopic_text"
                sophistication_score = 0.4
                expected_behavior = "Extremely small text"
                
            else:
                technique = "unknown_ocr"
                sophistication_score = 0.5
                expected_behavior = "Unknown OCR technique"
        
        elif 'pipeline_' in filename:
            attack_category = "Pipeline"
            
            if 'preprocessing_injection' in filename:
                technique = "preprocessing_injection"
                sophistication_score = 0.6
                expected_behavior = "Exploits normalization overflow"
                
            elif 'feature_extraction_manipulation' in filename:
                technique = "feature_extraction_manipulation"
                sophistication_score = 0.8
                expected_behavior = "CNN/ViT specific patterns"
                
            elif 'attention_hijacking' in filename:
                technique = "attention_hijacking"
                sophistication_score = 0.9
                expected_behavior = "Manipulates attention mechanisms"
                
            elif 'multi_stage_coordinated' in filename:
                technique = "multi_stage_coordinated"
                sophistication_score = 1.0
                expected_behavior = "Coordinates multiple pipeline stages"
                
            else:
                technique = "unknown_pipeline"
                sophistication_score = 0.7
                expected_behavior = "Unknown pipeline technique"
        
        else:
            attack_category = "Unknown"
            technique = "unknown"
            sophistication_score = 0.5
            expected_behavior = "Unknown attack type"
        
        return {
            "attack_category": attack_category,
            "technique": technique,
            "sophistication_score": sophistication_score,
            "expected_behavior": expected_behavior,
            "filename": filename
        }
    
    def analyze_all_attacks(self) -> Dict[str, Any]:
        """
        Analiza todos los ataques generados.
        
        Returns:
            Análisis completo
        """
        print("\n🔍 ANÁLISIS COMPLETO DE ATAQUES GENERADOS")
        print("="*50)
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "analysis_type": "simplified_attack_analysis",
            "attack_analyses": {
                "ocr_attacks": [],
                "pipeline_attacks": []
            },
            "summary": {
                "total_analyzed": 0,
                "ocr_count": 0,
                "pipeline_count": 0,
                "avg_ocr_sophistication": 0.0,
                "avg_pipeline_sophistication": 0.0,
                "images_with_detectable_text": 0
            }
        }
        
        # Buscar archivos de ataque
        if not os.path.exists(self.attack_dir):
            print(f"❌ Directorio {self.attack_dir} no encontrado")
            return results
        
        attack_files = []
        for filename in os.listdir(self.attack_dir):
            if filename.endswith('.png') and ('test_ocr_' in filename or 'test_pipeline_' in filename):
                filepath = os.path.join(self.attack_dir, filename)
                attack_files.append(filepath)
        
        print(f"📊 Encontrados {len(attack_files)} ataques para analizar")
        
        ocr_sophistication_scores = []
        pipeline_sophistication_scores = []
        detectable_text_count = 0
        
        # Analizar cada ataque
        for filepath in attack_files:
            filename = os.path.basename(filepath)
            print(f"\n🔍 Analizando {filename}...")
            
            # Análisis de sofisticación
            sophistication = self.analyze_attack_sophistication(filepath)
            
            # Análisis OCR
            ocr_analysis = self.analyze_ocr_readability(filepath)
            
            # Combinar análisis
            combined_analysis = {
                **sophistication,
                **ocr_analysis,
                "analysis_timestamp": datetime.now().isoformat()
            }
            
            # Agregar a resultados
            if sophistication["attack_category"] == "OCR":
                results["attack_analyses"]["ocr_attacks"].append(combined_analysis)
                ocr_sophistication_scores.append(sophistication["sophistication_score"])
                results["summary"]["ocr_count"] += 1
            else:
                results["attack_analyses"]["pipeline_attacks"].append(combined_analysis)
                pipeline_sophistication_scores.append(sophistication["sophistication_score"])
                results["summary"]["pipeline_count"] += 1
            
            # Contar texto detectable
            if ocr_analysis.get("ocr_analysis", {}).get("has_text", False):
                detectable_text_count += 1
            
            results["summary"]["total_analyzed"] += 1
            
            # Mostrar resultado
            print(f"   📊 Categoría: {sophistication['attack_category']}")
            print(f"   🔧 Técnica: {sophistication['technique']}")
            print(f"   📈 Sofisticación: {sophistication['sophistication_score']:.2f}")
            if ocr_analysis.get("ocr_analysis", {}).get("has_text"):
                print(f"   📝 Texto detectado: {ocr_analysis['ocr_analysis']['text_detected'][:50]}...")
        
        # Calcular estadísticas finales
        if ocr_sophistication_scores:
            results["summary"]["avg_ocr_sophistication"] = sum(ocr_sophistication_scores) / len(ocr_sophistication_scores)
        
        if pipeline_sophistication_scores:
            results["summary"]["avg_pipeline_sophistication"] = sum(pipeline_sophistication_scores) / len(pipeline_sophistication_scores)
        
        results["summary"]["images_with_detectable_text"] = detectable_text_count
        
        return results
    
    def save_results(self, results: Dict[str, Any]) -> None:
        """
        Guarda los resultados del análisis.
        
        Args:
            results: Resultados del análisis
        """
        filename = f"simplified_analysis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.attack_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Análisis guardado en: {filename}")
    
    def print_summary(self, results: Dict[str, Any]) -> None:
        """
        Imprime resumen del análisis.
        
        Args:
            results: Resultados del análisis
        """
        print("\n" + "="*60)
        print("📊 RESUMEN DEL ANÁLISIS DE ATAQUES")
        print("="*60)
        
        summary = results["summary"]
        
        print(f"\n📊 ESTADÍSTICAS GENERALES:")
        print(f"   • Total de ataques analizados: {summary['total_analyzed']}")
        print(f"   • Ataques OCR: {summary['ocr_count']}")
        print(f"   • Ataques Pipeline: {summary['pipeline_count']}")
        print(f"   • Imágenes con texto detectable: {summary['images_with_detectable_text']}")
        
        print(f"\n🧠 SOFISTICACIÓN PROMEDIO:")
        print(f"   • OCR promedio: {summary['avg_ocr_sophistication']:.3f}/1.0")
        print(f"   • Pipeline promedio: {summary['avg_pipeline_sophistication']:.3f}/1.0")
        
        if summary['avg_pipeline_sophistication'] > summary['avg_ocr_sophistication']:
            diff = summary['avg_pipeline_sophistication'] - summary['avg_ocr_sophistication']
            print(f"   🏆 Pipeline es {diff:.3f} puntos más sofisticado que OCR")
        
        print(f"\n📈 INTERPRETACIÓN:")
        text_detection_rate = (summary['images_with_detectable_text'] / summary['total_analyzed']) * 100
        print(f"   • {text_detection_rate:.1f}% de ataques tienen texto básico detectable")
        print(f"   • Esto sugiere que {100-text_detection_rate:.1f}% están bien ocultos")
        
        if summary['avg_pipeline_sophistication'] > 0.7:
            print("   • Pipeline attacks muestran alta sofisticación técnica")
        if summary['avg_ocr_sophistication'] < 0.6:
            print("   • OCR attacks priorizan simplicidad sobre complejidad")
        
        print("\n🎯 PRÓXIMO PASO:")
        print("   → Testing contra modelo real (LLaVA) para medir efectividad")
        print("   → Comparar sofisticación teórica vs efectividad práctica")
        
        print("\n" + "="*60)

def main():
    """Función principal del análisis simplificado."""
    print("🔍 ANÁLISIS SIMPLIFICADO DE ATAQUES")
    print("Mientras configuramos LLaVA, analicemos nuestros ataques")
    print("="*50)
    
    try:
        # Inicializar analizador
        analyzer = SimplifiedAttackAnalyzer()
        
        # Ejecutar análisis completo
        results = analyzer.analyze_all_attacks()
        
        if not results["attack_analyses"]["ocr_attacks"] and not results["attack_analyses"]["pipeline_attacks"]:
            print("❌ No se encontraron ataques para analizar")
            return
        
        # Guardar resultados
        analyzer.save_results(results)
        
        # Mostrar resumen
        analyzer.print_summary(results)
        
        print("\n🎉 Análisis simplificado completado!")
        print("📊 Tenemos datos preliminares sobre nuestros ataques")
        
    except Exception as e:
        print(f"\n❌ Error en análisis: {e}")
        raise

if __name__ == "__main__":
    main()
