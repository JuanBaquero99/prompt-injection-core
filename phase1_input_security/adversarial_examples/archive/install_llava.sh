
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
