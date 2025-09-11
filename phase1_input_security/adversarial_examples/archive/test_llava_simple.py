
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
        
        prompt = "USER: <image>\nWhat text do you see in this image? ASSISTANT:"
        
        inputs = processor(text=prompt, images=img, return_tensors="pt")
        
        # Generar respuesta
        generate_ids = model.generate(**inputs, max_new_tokens=50)
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
