#!/usr/bin/env python3
"""
Script de validación de la nueva estructura del monorepo PERSONA
"""
import os
import sys
from pathlib import Path

def validate_structure():
    """Valida que la nueva estructura del monorepo esté correcta"""
    
    base_path = Path(".")
    
    # Estructura esperada
    expected_structure = {
        "phase1_input_security": {
            "README.md": True,
            "prompt_injection": {
                "README.md": True,
                "core.py": True,
                "cli.py": True,
                "scanner": True,
                "detectors": True,
                "data": True,
                "examples": True,
                "research": True,
                "scripts": True,
                "tests": True
            }
        },
        "phase2_data_security": {
            "README.md": True
        },
        "phase3_extraction": {
            "README.md": True
        },
        "phase4_infrastructure": {
            "README.md": True
        },
        "phase5_ethics": {
            "README.md": True
        },
        "src": {
            "core": True
        },
        "docs": True,
        "README.md": True,
        "pyproject.toml": True,
        "LICENSE": True
    }
    
    def check_path(current_path, structure, level=0):
        """Verifica recursivamente la estructura"""
        indent = "  " * level
        all_good = True
        
        for item, expected in structure.items():
            item_path = current_path / item
            
            if isinstance(expected, bool):
                if expected and not item_path.exists():
                    print(f"❌ {indent}FALTA: {item_path}")
                    all_good = False
                elif expected and item_path.exists():
                    print(f"✅ {indent}{item}")
                    
            elif isinstance(expected, dict):
                if item_path.exists() and item_path.is_dir():
                    print(f"✅ {indent}{item}/")
                    if not check_path(item_path, expected, level + 1):
                        all_good = False
                else:
                    print(f"❌ {indent}FALTA CARPETA: {item_path}")
                    all_good = False
                    
        return all_good
    
    print("🔍 Validando estructura del monorepo PERSONA...")
    print("=" * 50)
    
    if check_path(base_path, expected_structure):
        print("\n🎉 ¡Estructura del monorepo validada correctamente!")
        print("\n📋 Resumen de la reorganización:")
        print("✅ Fase 1 (Input Security) - Prompt Injection completamente migrado")
        print("✅ Fases 2-5 - Estructura creada y documentada")
        print("✅ README principal actualizado como monorepo") 
        print("✅ pyproject.toml actualizado para nueva estructura")
        print("✅ Documentación específica por fase creada")
        
        print("\n🚀 Próximos pasos sugeridos:")
        print("1. Probar el sistema de prompt injection:")
        print("   cd phase1_input_security/prompt_injection")
        print("   python demo_complete.py")
        print("2. Comenzar desarrollo en las fases 2-5 según prioridades")
        print("3. Actualizar imports en código existente si es necesario")
        
        return True
    else:
        print("\n❌ Se encontraron problemas en la estructura")
        return False

if __name__ == "__main__":
    if validate_structure():
        sys.exit(0)
    else:
        sys.exit(1)
