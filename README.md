# Prompt Injection Core 🛡️

**[EN DESARROLLO] Librería para detectar vulnerabilidades de prompt injection en LLMs**

```
 ____  ____   ___  __  __ ____ _____   ___ _   _ ______ _____ ____ _____ ___ ___  _   _ 
|  _ \|  _ \ / _ \|  \/  |  _ \_   _| |_ _| \ | |      |_   _|  __|  ___|___|  _ \| \ | |
| |_) | |_) | | | | |\/| | |_) || |    | ||  \| |        | | |  |_|__   |  | |_) |  \| |
|  __/|  _ <| |_| | |  | |  __/ | |    | || |\  |     _  | | |  __|__   |  |  _ <| |\  |
|_|   |_| \_\\___/|_|  |_|_|    |_|   |___|_| \_|    |_| |_| |____|___/|_||_| \_\_| \_|
```

## 🚧 Estado del Proyecto

- **Versión**: 0.1.0 (MVP en desarrollo)
- **Estado**: Experimento inicial, buscando feedback
- **Objetivo**: Crear una librería modular para auditoría de seguridad en LLMs

## 🎯 Visión

Esta será la primera librería de un ecosistema modular para seguridad en LLMs:

1. **prompt-injection-core** 👈 *Empezamos aquí*
2. **llm-security-scanner** (próximo)
3. **prompt-defense-kit** (futuro)
4. **adversarial-nlp-toolkit** (futuro)

## 🔧 Instalación (cuando esté listo)

```bash
pip install prompt-injection-core
```

## 💡 Uso Planeado

```python
from prompt_injection_core import PromptScanner

scanner = PromptScanner()
result = scanner.scan("Ignore previous instructions...")

print(f"Risk Score: {result.risk_score}/100")
print(f"Vulnerabilities: {result.vulnerabilities_found}")
```

## 🛠️ Desarrollo

```bash
# Instalar para desarrollo
git clone https://github.com/JuanBaquero99/prompt-injection-core
cd prompt-injection-core
pip install -e ".[dev]"

# Ejecutar tests (cuando estén listos)
pytest
```

## 📋 TODO MVP

- [ ] Detector básico de jailbreaking
- [ ] Detector de system prompt leaking  
- [ ] CLI simple
- [ ] Tests básicos
- [ ] Documentación de uso

## 🤝 Feedback Bienvenido

Este es un proyecto experimental. Si tienes ideas, casos de uso, o quieres contribuir:

- 🐛 [Reportar Issues](https://github.com/JuanBaquero99/prompt-injection-core/issues)
- 💡 [Sugerir Features](https://github.com/JuanBaquero99/prompt-injection-core/discussions)
- 🤝 [Contribuir](https://github.com/JuanBaquero99/prompt-injection-core/pulls)

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para detalles.

---

**Desarrollado por [Juan Pablo Baquero](https://github.com/JuanBaquero99)**

*⭐ ¿Te interesa el proyecto? ¡Dale una estrella para seguir el progreso!*
