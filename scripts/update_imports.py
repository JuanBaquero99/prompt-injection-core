#!/usr/bin/env python3
"""
Script para actualizar todos los imports de prompt_injection_core 
a la nueva estructura del monorepo
"""

import os
import re
from pathlib import Path

def update_imports_in_file(file_path):
    """Actualiza los imports en un archivo específico"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Si no se puede leer como UTF-8, intentar con latin-1
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    original_content = content
    
    # Reemplazos de imports
    replacements = [
        # Imports básicos
        (r'from prompt_injection_core import PromptScanner', 'from scanner.scanner import PromptScanner'),
        (r'from prompt_injection_core\.scanner\.scanner import PromptScanner', 'from scanner.scanner import PromptScanner'),
        (r'from prompt_injection_core\.core import PromptScanner', 'from core import PromptScanner'),
        
        # Imports de detectores
        (r'from prompt_injection_core\.detectors\.ml_detector import MLDetector', 'from detectors.ml_detector import MLDetector'),
        (r'from prompt_injection_core\.detectors\.jailbreak import JailbreakDetector', 'from detectors.jailbreak import JailbreakDetector'),
        (r'from prompt_injection_core\.detectors\.leak import SystemLeakDetector', 'from detectors.leak import SystemLeakDetector'),
        (r'from prompt_injection_core\.detectors\.roleplay import RolePlayDetector', 'from detectors.roleplay import RolePlayDetector'),
        (r'from prompt_injection_core\.detectors\.models import Detection', 'from detectors.models import Detection'),
        (r'from prompt_injection_core\.detectors import (.+)', r'from detectors import \1'),
        
        # Imports generales
        (r'import prompt_injection_core', 'import core'),
        
        # CLI referencias
        (r'python -m prompt_injection_core\.cli', 'python cli.py'),
        (r"'prompt_injection_core\.cli'", "'cli'"),
        
        # Referencias en comandos
        (r'-m.*prompt_injection_core\.cli', 'cli.py'),
    ]
    
    # Aplicar reemplazos
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # Solo escribir si hubo cambios
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def update_all_imports():
    """Actualiza todos los imports en el proyecto de prompt injection"""
    
    base_path = Path("./phase1_input_security/prompt_injection")
    
    if not base_path.exists():
        print("❌ No se encuentra la carpeta de prompt injection")
        return
    
    # Extensiones de archivo a procesar
    extensions = {'.py', '.md'}
    
    updated_files = []
    
    # Recorrer todos los archivos
    for file_path in base_path.rglob('*'):
        if file_path.is_file() and file_path.suffix in extensions:
            if update_imports_in_file(file_path):
                updated_files.append(file_path)
    
    print(f"🔧 Actualizados {len(updated_files)} archivos:")
    for file_path in updated_files:
        print(f"   ✅ {file_path}")
    
    print("\n✨ Actualización de imports completada!")

if __name__ == "__main__":
    update_all_imports()
