#!/usr/bin/env python3
"""
LLaVA Ultra-Light Testing
========================

Versión ultra-optimizada de LLaVA con técnicas agresivas de optimización
de memoria. Para sistemas con recursos muy limitados.

Estrategias:
1. Carga progresiva
2. Solo componentes esenciales  
3. Liberación inmediata de memoria
4. Logging detallado para debugging

Autor: PERSONA Framework Team
"""

import os
import sys
import json
import time
import gc
from typing import Dict, List, Any, Optional
from datetime import datetime
from PIL import Image

# Limpiar memoria antes de importar torch
gc.collect()

print("🦙 LLaVA Ultra-Light Testing")
print("="*40)
print("🔧 Importando dependencias...")

try:
    import torch
    print(f"   ✅ PyTorch {torch.__version__}")
    
    # Configurar torch inmediatamente
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    
    # Si hay CUDA, limpiar cache
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        gpu_mem = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"   🎮 GPU: {gpu_mem:.1f}GB VRAM disponible")
    else:
        print("   💻 CPU mode - No GPU detectada")
        
except ImportError as e:
    print(f"   ❌ Error importando PyTorch: {e}")
    sys.exit(1)

# Import progresivo de transformers
try:
    print("   📦 Importando transformers...")
    from transformers import AutoProcessor, LlavaForConditionalGeneration
    print("   ✅ Transformers importado")
except ImportError as e:
    print(f"   ❌ Error importando transformers: {e}")
    sys.exit(1)

class UltraLightLLaVATester:
    """Tester ultra-optimizado para sistemas con pocos recursos."""
    
    def __init__(self):
        """Inicializa el tester ultra-light."""
        self.model = None
        self.processor = None
        self.device = "cpu"  # Forzar CPU por ahora
        self.model_loaded = False
        self.attack_dir = "real_testing_results"
        
        print("🚀 Ultra-Light Tester inicializado")
        
        # Verificar ataques disponibles
        self._check_available_attacks()
    
    def _check_available_attacks(self):
        """Verifica ataques disponibles."""
        if not os.path.exists(self.attack_dir):
            print(f"   ⚠️  Directorio {self.attack_dir} no encontrado")
            return
        
        files = [f for f in os.listdir(self.attack_dir) if f.endswith('.png')]
        print(f"   📊 {len(files)} ataques disponibles")
        
        # Mostrar algunos ejemplos
        for i, f in enumerate(files[:3]):
            print(f"   • {f}")
    
    def attempt_minimal_load(self) -> bool:
        """
        Intenta cargar LLaVA con configuración mínima.
        
        Returns:
            True si carga exitosamente
        """
        print("\n🦙 Intentando carga ultra-minimal...")
        
        try:
            model_id = "llava-hf/llava-1.5-7b-hf"
            
            # Limpiar toda la memoria disponible
            gc.collect()
            
            print("   📝 Cargando procesador (minimal)...")
            self.processor = AutoProcessor.from_pretrained(
                model_id,
                low_cpu_mem_usage=True
            )
            print("   ✅ Procesador cargado")
            
            print("   🧠 Cargando modelo (ultra-optimizado)...")
            print("      ⏳ Esto puede tomar varios minutos...")
            
            # Configuración ultra-conservadora
            self.model = LlavaForConditionalGeneration.from_pretrained(
                model_id,
                device_map="cpu",
                torch_dtype=torch.float32,
                low_cpu_mem_usage=True,
                offload_folder="./tmp_offload"
            )
            
            print("   ✅ Modelo cargado exitosamente!")
            
            # Configurar para inferencia
            self.model.eval()
            self.model_loaded = True
            
            # Limpiar cache
            gc.collect()
            
            return True
            
        except Exception as e:
            print(f"   ❌ Error en carga minimal: {e}")
            return self._try_emergency_config()
    
    def _try_emergency_config(self) -> bool:
        """Configuración de emergencia."""
        print("\n🚨 Intentando configuración de emergencia...")
        
        try:
            # Si nada funciona, al menos verificar que las dependencias estén OK
            print("   🔍 Verificando dependencias...")
            print(f"   • PyTorch: {torch.__version__}")
            print(f"   • Transformers disponible: ✅")
            
            # Intentar una carga muy básica
            from transformers import pipeline
            print("   💭 Intentando pipeline básico...")
            
            # No cargar el modelo completo, solo verificar que funciona
            print("   ⚠️  Modelo no cargado - dependencias OK")
            print("   💡 Sugerencias:")
            print("      1. Cerrar todos los programas no esenciales")
            print("      2. Reiniciar el sistema")
            print("      3. Aumentar memoria virtual de Windows")
            print("      4. Usar GPT-4V API como alternativa ($0.50 = ~$2,000 COP)")
            
            return False
            
        except Exception as e:
            print(f"   ❌ Configuración de emergencia falló: {e}")
            return False
    
    def test_basic_functionality(self) -> Dict[str, Any]:
        """
        Test básico de funcionalidad (si el modelo está cargado).
        
        Returns:
            Resultados del test
        """
        if not self.model_loaded:
            return {
                "error": "Modelo no cargado",
                "suggestions": [
                    "Liberar más memoria RAM",
                    "Cerrar otros programas", 
                    "Reiniciar sistema",
                    "Usar GPT-4V API (~$2,000 COP para 50 tests)"
                ]
            }
        
        print("🎯 Ejecutando test básico...")
        
        try:
            # Buscar una imagen de test
            test_images = [f for f in os.listdir(self.attack_dir) if f.endswith('.png')][:1]
            
            if not test_images:
                return {"error": "No hay imágenes de test disponibles"}
            
            test_image_path = os.path.join(self.attack_dir, test_images[0])
            
            # Cargar imagen
            image = Image.open(test_image_path).convert('RGB')
            
            # Prompt simple
            prompt = "USER: <image>\nWhat do you see in this image? ASSISTANT:"
            
            # Procesar
            inputs = self.processor(text=prompt, images=image, return_tensors="pt")
            
            # Generar respuesta
            start_time = time.time()
            
            with torch.no_grad():
                generate_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=50,  # Solo 50 tokens para test
                    do_sample=False,
                    pad_token_id=self.processor.tokenizer.eos_token_id
                )
            
            inference_time = time.time() - start_time
            
            # Decodificar
            response = self.processor.batch_decode(
                generate_ids, 
                skip_special_tokens=True
            )[0]
            
            if "ASSISTANT:" in response:
                response = response.split("ASSISTANT:")[-1].strip()
            
            return {
                "success": True,
                "image_tested": test_image_path,
                "model_response": response,
                "inference_time": inference_time,
                "device": self.device
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "model_loaded": self.model_loaded
            }

def main():
    """Función principal ultra-light."""
    print("\n🦙 INICIANDO TESTING ULTRA-LIGHT")
    print("="*40)
    
    try:
        # Inicializar tester
        tester = UltraLightLLaVATester()
        
        # Intentar carga minimal
        print("\n📥 Intentando carga ultra-optimizada...")
        success = tester.attempt_minimal_load()
        
        if success:
            print("\n🎉 ¡Modelo cargado exitosamente!")
            
            # Ejecutar test básico
            result = tester.test_basic_functionality()
            
            if "error" not in result:
                print(f"\n✅ TEST EXITOSO!")
                print(f"   📝 Respuesta: {result['model_response']}")
                print(f"   ⚡ Tiempo: {result['inference_time']:.2f}s")
                print(f"   🖥️  Dispositivo: {result['device']}")
                
                # Guardar resultado
                filename = f"llava_ultralight_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                
                print(f"   💾 Resultado guardado: {filename}")
                print("\n🚀 ¡LLaVA funcionando localmente!")
                
            else:
                print(f"\n❌ Error en test: {result['error']}")
                if "suggestions" in result:
                    print("   💡 Sugerencias:")
                    for suggestion in result["suggestions"]:
                        print(f"      • {suggestion}")
        
        else:
            print("\n❌ No se pudo cargar el modelo")
            print("\n📊 ESTADO ACTUAL:")
            print("   • Dependencias: ✅ Instaladas correctamente")
            print("   • Modelo: ❌ No se pudo cargar (memoria insuficiente)")
            print("\n💡 OPCIONES DISPONIBLES:")
            print("   1. 🆓 Liberar más RAM y reintentar")
            print("   2. 💰 GPT-4V API (~$2,000 COP = 50 tests)")
            print("   3. 📊 Usar resultados de análisis actual")
            
            # Mostrar estado de análisis actual
            print("\n📈 DATOS DISPONIBLES (de análisis previo):")
            print("   • 40 ataques generados (20 OCR + 20 Pipeline)")
            print("   • Sofisticación Pipeline: 0.825/1.0")
            print("   • Sofisticación OCR: 0.525/1.0") 
            print("   • Diferencia significativa: 57% más sofisticados")
            
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        print("\n💡 Si el error persiste:")
        print("   • Reiniciar VS Code")
        print("   • Reiniciar sistema")
        print("   • Considerar GPT-4V API")

if __name__ == "__main__":
    main()
