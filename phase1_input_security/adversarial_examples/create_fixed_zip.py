#!/usr/bin/env python3
"""
Script para crear un ZIP correcto de los ataques PERSONA para Colab
Soluciona el problema de estructura de carpetas
"""

import zipfile
import os
from pathlib import Path

def create_correct_zip():
    """Crea un ZIP con la estructura correcta para Colab"""
    
    # Rutas
    base_path = Path("real_testing_results")
    zip_path = Path("ataques_persona_fixed.zip")
    
    if not base_path.exists():
        print(f"❌ ERROR: Carpeta {base_path} no encontrada")
        print("Asegúrate de estar en la carpeta adversarial_examples")
        return False
    
    # Contar archivos
    attack_files = list(base_path.glob("*.png"))
    ocr_files = [f for f in attack_files if "ocr_" in f.name]
    pipeline_files = [f for f in attack_files if "pipeline_" in f.name]
    
    print(f"📊 CREANDO ZIP CORREGIDO")
    print(f"=" * 30)
    print(f"Archivos OCR encontrados: {len(ocr_files)}")
    print(f"Archivos Pipeline encontrados: {len(pipeline_files)}")
    print(f"Total de ataques: {len(attack_files)}")
    
    if len(attack_files) == 0:
        print("❌ No se encontraron archivos de ataque")
        return False
    
    # Crear ZIP con estructura correcta
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Crear la carpeta real_testing_results dentro del ZIP
        for attack_file in attack_files:
            # Agregar cada archivo en la ruta real_testing_results/
            arcname = f"real_testing_results/{attack_file.name}"
            zipf.write(attack_file, arcname)
            print(f"✅ Agregado: {arcname}")
    
    # Verificar el ZIP creado
    print(f"\n📦 VERIFICACIÓN DEL ZIP")
    print(f"=" * 25)
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        files_in_zip = zipf.namelist()
        print(f"Archivos en ZIP: {len(files_in_zip)}")
        print("Estructura:")
        for file in sorted(files_in_zip)[:5]:
            print(f"  - {file}")
        if len(files_in_zip) > 5:
            print(f"  ... y {len(files_in_zip) - 5} archivos más")
    
    file_size = zip_path.stat().st_size / (1024 * 1024)  # MB
    print(f"\n✅ ZIP creado exitosamente:")
    print(f"   Archivo: {zip_path}")
    print(f"   Tamaño: {file_size:.1f} MB")
    print(f"   Estructura: real_testing_results/ con {len(attack_files)} ataques")
    
    return True

if __name__ == "__main__":
    print("🔧 GENERADOR DE ZIP CORREGIDO PARA COLAB")
    print("=" * 45)
    
    success = create_correct_zip()
    
    if success:
        print(f"\n🎯 ¡LISTO! Usa 'ataques_persona_fixed.zip' en Colab")
        print(f"Este ZIP tiene la estructura correcta que espera el notebook")
    else:
        print(f"\n❌ Error creando el ZIP. Verifica la ubicación de los archivos.")
