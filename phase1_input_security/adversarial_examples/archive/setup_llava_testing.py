#!/usr/bin/env python3
"""
LLaVA Local Setup & Testing
==========================

Configuración y testing de ataques adversariales contra LLaVA local.
Este es nuestro primer testing REAL contra un modelo funcional.

Pasos:
1. Instalar LLaVA
2. Cargar modelo localmente  
3. Probar nuestros 40 ataques generados
4. Medir efectividad real OCR vs Pipeline

Autor: PERSONA Framework Team
"""

import os
import sys
import json
import subprocess
from typing import Dict, List, Any, Optional
from datetime import datetime
from PIL import Image

class LLaVALocalTester:
    """Tester para LLaVA local."""
    
    def __init__(self, results_dir: str = "real_testing_results"):
        """
        Inicializa el tester de LLaVA.
        
        Args:
            results_dir: Directorio con ataques generados
        """
        self.results_dir = results_dir
        self.llava_installed = False
        
        print("🦙 LLaVA Local Tester inicializado")
        print(f"📁 Buscando ataques en: {results_dir}")
    
    def check_llava_installation(self) -> bool:
        """
        Verifica si LLaVA está instalado.
        
        Returns:
            True si está instalado, False si no
        """
        print("\n🔍 Verificando instalación de LLaVA...")
        
        try:
            # Intentar importar LLaVA
            import llava
            print("   ✅ LLaVA encontrado en el sistema")
            self.llava_installed = True
            return True
            
        except ImportError:
            print("   ❌ LLaVA no encontrado")
            print("   📝 Necesita instalación manual")
            self.llava_installed = False
            return False
    
    def install_llava_requirements(self) -> None:
        """Instala los requisitos básicos para LLaVA."""
        print("\n📦 Instalando requisitos básicos para LLaVA...")
        
        requirements = [
            "torch",
            "torchvision", 
            "transformers",
            "tokenizers",
            "sentencepiece",
            "shortuuid",
            "accelerate",
            "peft",
            "bitsandbytes",
            "pydantic",
            "markdown2[all]",
            "numpy",
            "scikit-learn",
            "gradio",
            "requests",
            "httpx",
            "uvicorn",
            "fastapi",
            "einops",
            "flash-attn --no-build-isolation"
        ]
        
        print("⚠️  NOTA: Instalación de LLaVA requiere pasos manuales")
        print("📝 Creando script de instalación...")
        
        install_script = """
# Script de instalación de LLaVA
# Ejecutar manualmente paso a paso

# 1. Clonar repositorio LLaVA
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA

# 2. Instalar en entorno actual
pip install --upgrade pip
pip install -e .

# 3. Instalar dependencias adicionales
pip install -e ".[train]"
pip install flash-attn --no-build-isolation

# 4. Descargar modelo (ejemplo: LLaVA-1.5-7B)
# Se descarga automáticamente en primer uso
"""
        
        with open("install_llava.sh", "w") as f:
            f.write(install_script)
        
        print("   ✅ Script creado: install_llava.sh")
        print("   📋 Ejecutar manualmente para instalar LLaVA")
    
    def create_simple_llava_test(self) -> None:
        """
        Crea un test simple para verificar LLaVA funcional.
        """
        print("\n🧪 Creando test simple de LLaVA...")
        
        simple_test = '''
#!/usr/bin/env python3
"""
Test Simple de LLaVA
==================

Prueba básica para verificar que LLaVA funciona antes del testing real.
"""

import torch
from PIL import Image
import requests
from transformers import AutoProcessor, LlavaForConditionalGeneration

def test_llava_basic():
    """Test básico de LLaVA."""
    
    print("🦙 Cargando LLaVA-1.5-7B...")
    
    try:
        # Cargar modelo y procesador
        model_id = "llava-hf/llava-1.5-7b-hf"
        
        processor = AutoProcessor.from_pretrained(model_id)
        model = LlavaForConditionalGeneration.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            device_map="auto"
        )
        
        print("   ✅ Modelo cargado exitosamente")
        
        # Test con imagen simple
        print("🖼️  Creando imagen de prueba...")
        
        # Crear imagen simple con texto
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (400, 300), color='white')
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.load_default()
        except:
            font = None
            
        draw.text((50, 150), "Hello LLaVA!", fill='black', font=font)
        img.save("test_image.png")
        
        # Test de inferencia
        print("🔍 Probando inferencia...")
        
        prompt = "USER: <image>\\nWhat text do you see in this image? ASSISTANT:"
        
        inputs = processor(text=prompt, images=img, return_tensors="pt")
        
        # Generar respuesta
        generate_ids = model.generate(**inputs, max_length=30)
        response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        
        print(f"📝 Respuesta: {response}")
        print("🎉 LLaVA está funcionando correctamente!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en test de LLaVA: {e}")
        print("💡 Verificar instalación siguiendo install_llava.sh")
        return False

if __name__ == "__main__":
    test_llava_basic()
'''
        
        with open("test_llava_simple.py", "w", encoding="utf-8") as f:
            f.write(simple_test)
        
        print("   ✅ Test creado: test_llava_simple.py")
        print("   📋 Ejecutar después de instalar LLaVA")
    
    def load_attack_files(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Carga los archivos de ataque generados previamente.
        
        Returns:
            Diccionario con información de ataques
        """
        print(f"\n📂 Cargando ataques desde {self.results_dir}...")
        
        attack_files = {
            "ocr_attacks": [],
            "pipeline_attacks": []
        }
        
        # Buscar archivos de ataque
        if not os.path.exists(self.results_dir):
            print(f"   ❌ Directorio {self.results_dir} no encontrado")
            return attack_files
        
        files = os.listdir(self.results_dir)
        
        # Clasificar archivos
        for filename in files:
            if filename.endswith('.png'):
                filepath = os.path.join(self.results_dir, filename)
                
                if filename.startswith('test_ocr_'):
                    # Extraer información del nombre
                    parts = filename.replace('test_ocr_', '').replace('.png', '').split('_')
                    technique = '_'.join(parts[:-1])
                    index = int(parts[-1])
                    
                    attack_files["ocr_attacks"].append({
                        "filepath": filepath,
                        "filename": filename,
                        "technique": technique,
                        "index": index
                    })
                    
                elif filename.startswith('test_pipeline_'):
                    # Extraer información del nombre
                    parts = filename.replace('test_pipeline_', '').replace('.png', '').split('_')
                    technique = '_'.join(parts[:-1])
                    index = int(parts[-1])
                    
                    attack_files["pipeline_attacks"].append({
                        "filepath": filepath,
                        "filename": filename,
                        "technique": technique,
                        "index": index
                    })
        
        print(f"   📊 Ataques encontrados:")
        print(f"      🎯 OCR: {len(attack_files['ocr_attacks'])}")
        print(f"      🔄 Pipeline: {len(attack_files['pipeline_attacks'])}")
        
        return attack_files
    
    def print_setup_instructions(self) -> None:
        """Imprime instrucciones detalladas de setup."""
        print("\n" + "="*60)
        print("📋 INSTRUCCIONES DE SETUP - LLaVA LOCAL")
        print("="*60)
        
        print("\n🚀 PASO 1: Instalar LLaVA")
        print("   1. Ejecutar: bash install_llava.sh")
        print("   2. O seguir pasos manuales del script")
        print("   3. Verificar instalación con: python test_llava_simple.py")
        
        print("\n🧪 PASO 2: Test Básico")
        print("   1. Ejecutar test_llava_simple.py")
        print("   2. Verificar que LLaVA responde correctamente")
        print("   3. Confirmar que puede procesar imágenes")
        
        print("\n🎯 PASO 3: Testing Real (después del setup)")
        print("   1. Ejecutar testing contra 40 ataques generados")
        print("   2. Medir tasas de éxito OCR vs Pipeline")
        print("   3. Obtener primeros datos empíricos")
        
        print("\n⚡ REQUISITOS TÉCNICOS:")
        print("   • GPU recomendada (8GB+ VRAM)")
        print("   • 16GB+ RAM")
        print("   • ~10GB espacio en disco")
        print("   • Conexión a internet (descarga inicial)")
        
        print("\n🎯 OBJETIVO INMEDIATO:")
        print("   → Instalar LLaVA siguiendo install_llava.sh")
        print("   → Ejecutar test_llava_simple.py")
        print("   → Confirmar que está listo para testing real")
        
        print("\n" + "="*60)

def main():
    """Función principal de setup."""
    print("🦙 SETUP LLaVA - PRIMERA VALIDACIÓN REAL")
    print("Preparando testing contra modelo funcional")
    print("="*50)
    
    try:
        # Inicializar tester
        tester = LLaVALocalTester()
        
        # Verificar instalación actual
        is_installed = tester.check_llava_installation()
        
        if not is_installed:
            # Crear scripts de instalación
            tester.install_llava_requirements()
            tester.create_simple_llava_test()
        
        # Cargar ataques existentes
        attack_files = tester.load_attack_files()
        
        # Mostrar instrucciones
        tester.print_setup_instructions()
        
        print("\n🎉 Setup de LLaVA preparado!")
        print("📝 Seguir instrucciones de instalación manual")
        
    except Exception as e:
        print(f"\n❌ Error en setup: {e}")
        raise

if __name__ == "__main__":
    main()
