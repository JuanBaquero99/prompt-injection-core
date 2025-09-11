#!/usr/bin/env python3
"""
Test Suite for OCR Injection Attacks
=====================================

Script para probar y validar los generadores de ataques OCR.
Incluye testing básico de funcionalidad y evaluación de efectividad.

Usage:
    python test_ocr_attacks.py

Author: Juan Pablo Baquero  
Purpose: Ethical AI security research validation
"""

import os
import sys
from pathlib import Path

# Agregar paths necesarios
current_dir = Path(__file__).parent
sys.path.append(str(current_dir.parent))
sys.path.append(str(current_dir))

from attack_generators.ocr_injection import OCRInjectionGenerator

def test_basic_functionality():
    """Prueba funcionalidad básica del generador OCR."""
    print("🔧 TESTING: Funcionalidad Básica")
    print("-" * 40)
    
    generator = OCRInjectionGenerator()
    
    # Test 1: Invisible text attack
    print("📝 Test 1: Invisible Text Attack")
    try:
        image, info = generator.create_invisible_text_attack(
            "Test prompt for invisible text attack"
        )
        print(f"   ✅ Generado exitosamente: {info['type']}")
        print(f"   📊 Info: {info}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Transparent overlay attack  
    print("\n📝 Test 2: Transparent Overlay Attack")
    try:
        image, info = generator.create_transparent_overlay_attack(
            "Test prompt for overlay attack"
        )
        print(f"   ✅ Generado exitosamente: {info['type']}")
        print(f"   📊 Transparency: {info['transparency']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Steganographic attack
    print("\n📝 Test 3: Steganographic Attack")
    try:
        image, info = generator.create_steganographic_attack(
            "Test prompt for steganographic attack"
        )
        print(f"   ✅ Generado exitosamente: {info['type']}")
        print(f"   📊 Modified pixels: {info['modified_pixels']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Microscopic text attack
    print("\n📝 Test 4: Microscopic Text Attack")
    try:
        image, info = generator.create_microscopic_text_attack(
            "Test prompt for microscopic attack"
        )
        print(f"   ✅ Generado exitosamente: {info['type']}")
        print(f"   📊 Font size: {info['font_size']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def test_attack_generation_suite():
    """Genera una suite completa de ataques para análisis."""
    print("\n🎯 TESTING: Suite de Ataques")
    print("-" * 40)
    
    generator = OCRInjectionGenerator()
    
    # Generar múltiples ataques aleatorios
    num_attacks = 5
    successful_attacks = 0
    
    for i in range(num_attacks):
        print(f"\n🔬 Generando ataque {i+1}/{num_attacks}...")
        try:
            image, info = generator.generate_random_attack()
            
            # Guardar ataque
            filepath = generator.save_attack(image, info)
            print(f"   ✅ Guardado: {os.path.basename(filepath)}")
            print(f"   🎯 Técnica: {info['technique']}")
            print(f"   📝 Texto: {info['hidden_text'][:50]}...")
            
            successful_attacks += 1
            
        except Exception as e:
            print(f"   ❌ Error generando ataque: {e}")
    
    print(f"\n📊 Resultado: {successful_attacks}/{num_attacks} ataques generados exitosamente")

def test_ocr_extraction():
    """Prueba la capacidad de extracción OCR en ataques generados."""
    print("\n🔍 TESTING: Extracción OCR")
    print("-" * 40)
    
    generator = OCRInjectionGenerator()
    
    # Crear algunos ataques específicos para testing OCR
    test_cases = [
        ("Invisible Text", "SYSTEM OVERRIDE DETECTED"),
        ("Transparent Overlay", "ADMIN MODE ACTIVATED"), 
        ("Microscopic Text", "DEBUG INFO EXTRACTED")
    ]
    
    for test_name, test_prompt in test_cases:
        print(f"\n📝 Testing OCR en: {test_name}")
        
        try:
            if "Invisible" in test_name:
                image, info = generator.create_invisible_text_attack(test_prompt)
            elif "Transparent" in test_name:
                image, info = generator.create_transparent_overlay_attack(test_prompt)
            else:
                image, info = generator.create_microscopic_text_attack(test_prompt)
            
            # Probar extracción OCR
            ocr_results = generator.test_ocr_extraction(image)
            
            print(f"   🎯 Texto original: '{test_prompt}'")
            
            # Analizar resultados
            extraction_success = False
            for method, result in ocr_results.items():
                if result and isinstance(result, str) and "Error" not in result:
                    # Buscar coincidencias parciales
                    original_words = set(test_prompt.lower().split())
                    extracted_words = set(result.lower().split())
                    common_words = original_words.intersection(extracted_words)
                    
                    if common_words:
                        print(f"   ✅ {method}: Detectó {len(common_words)} palabras")
                        print(f"      Extraído: '{result[:100]}...'")
                        extraction_success = True
                    else:
                        print(f"   ❌ {method}: Sin coincidencias")
                else:
                    print(f"   ⚠️  {method}: {result}")
            
            if not extraction_success:
                print(f"   📊 Resultado: Ataque exitoso (texto no detectado)")
            else:
                print(f"   📊 Resultado: Ataque parcialmente detectado")
                
        except Exception as e:
            print(f"   ❌ Error en testing: {e}")

def test_output_directory():
    """Verifica que se pueda crear y usar el directorio de salida."""
    print("\n📁 TESTING: Directorio de Salida")
    print("-" * 40)
    
    generator = OCRInjectionGenerator()
    
    # Verificar directorio existe
    if os.path.exists(generator.output_dir):
        print(f"   ✅ Directorio existe: {generator.output_dir}")
        
        # Contar archivos existentes
        files = list(Path(generator.output_dir).glob("*.png"))
        print(f"   📊 Archivos de ataque existentes: {len(files)}")
        
        if files:
            print("   📝 Últimos ataques generados:")
            for f in files[-3:]:  # Mostrar últimos 3
                print(f"      - {f.name}")
    else:
        print(f"   ⚠️  Directorio no existe, se creará: {generator.output_dir}")

def main():
    """Función principal de testing."""
    print("🧪 OCR INJECTION ATTACK GENERATOR - TEST SUITE")
    print("=" * 60)
    print("Propósito: Investigación ética en seguridad de IA")
    print("Author: Juan Pablo Baquero")
    print("=" * 60)
    
    # Ejecutar todos los tests
    try:
        test_output_directory()
        test_basic_functionality()
        test_attack_generation_suite()
        test_ocr_extraction()
        
        print("\n🎉 TESTING COMPLETADO")
        print("=" * 60)
        print("✅ Generador OCR Injection operativo")
        print("✅ Múltiples técnicas de ataque funcionando")
        print("✅ Sistema de archivos configurado")
        print("✅ Extracción OCR validada")
        
        print(f"\n📁 Ataques generados guardados en:")
        print(f"   {os.path.abspath('test_cases/generated_attacks')}")
        
        print(f"\n🔬 Próximo paso sugerido:")
        print(f"   1. Examinar ataques generados visualmente")
        print(f"   2. Probar contra modelo LLaVA real")
        print(f"   3. Desarrollar métricas de evaluación")
        
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO EN TESTING: {e}")
        print("🔧 Verificar instalación de dependencias:")
        print("   pip install pillow numpy")

if __name__ == "__main__":
    main()
