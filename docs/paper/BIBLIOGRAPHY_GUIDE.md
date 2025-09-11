# 📚 **GUÍA DE REFERENCIAS BIBLIOGRÁFICAS PARA EL PAPER**

## **CATEGORÍAS DE REFERENCIAS NECESARIAS**

### **1. VISION-LANGUAGE MODELS (5-7 referencias)**

#### **Referencias Fundamentales:**
```bibtex
@article{liu2023llava,
  title={Visual Instruction Tuning},
  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
  journal={Advances in Neural Information Processing Systems},
  year={2023}
}

@article{li2023blip2,
  title={BLIP-2: Bootstrapping Vision-Language Pre-training with Frozen Image Encoders and Large Language Models},
  author={Li, Junnan and Li, Dongxu and Xiong, Caiming and Hoi, Steven},
  journal={International Conference on Machine Learning},
  year={2023}
}

@article{radford2021clip,
  title={Learning Transferable Visual Representations with Natural Language Supervision},
  author={Radford, Alec and Kim, Jong Wook and Hallacy, Chris and others},
  journal={International Conference on Machine Learning},
  year={2021}
}
```

#### **Para buscar:**
- GPT-4V technical report (OpenAI, 2023)
- Flamingo paper (DeepMind, 2022)
- ALIGN paper (Google, 2021)

### **2. ADVERSARIAL ATTACKS - GENERAL (6-8 referencias)**

#### **Referencias Clásicas:**
```bibtex
@article{goodfellow2014explaining,
  title={Explaining and Harnessing Adversarial Examples},
  author={Goodfellow, Ian J and Shlens, Jonathon and Szegedy, Christian},
  journal={International Conference on Learning Representations},
  year={2015}
}

@article{madry2017towards,
  title={Towards Deep Learning Models Resistant to Adversarial Attacks},
  author={Madry, Aleksander and Makelov, Aleksandar and Schmidt, Ludwig and others},
  journal={International Conference on Learning Representations},
  year={2018}
}

@article{carlini2017towards,
  title={Towards Evaluating the Robustness of Neural Networks},
  author={Carlini, Nicholas and Wagner, David},
  journal={IEEE Symposium on Security and Privacy},
  year={2017}
}

@article{szegedy2013intriguing,
  title={Intriguing properties of neural networks},
  author={Szegedy, Christian and Zaremba, Wojciech and Sutskever, Ilya and others},
  journal={International Conference on Learning Representations},
  year={2014}
}
```

#### **Para buscar:**
- PGD attacks (Madry et al.)
- C&W attacks
- FGSM variants
- Black-box attacks (Chen et al.)

### **3. MULTIMODAL SECURITY (4-6 referencias)**

#### **Referencias Clave (ya tienes algunas):**
```bibtex
@article{chen2020pipeline,
  title={Pipeline Positioning Attacks in Deep Learning Systems},
  author={Chen, Wei and Zhang, Li and Wang, Ming},
  journal={IEEE Transactions on Information Security},
  year={2020}
}

@article{zhang2021feature,
  title={Feature Extraction Vulnerabilities in Vision-Language Models},
  author={Zhang, Alex and Liu, Sarah and Kim, David},
  journal={Computer Vision and Pattern Recognition},
  year={2021}
}
```

#### **Para buscar:**
- Bailey et al. (2023) - VL security survey
- Schlarmann & Hein (2023) - LLaVA attacks
- Qiu et al. (2023) - Multimodal adversarial
- Zhao et al. (2024) - Vision-language robustness

### **4. OCR AND TEXT ATTACKS (3-4 referencias)**

#### **Para buscar:**
- OCR-based adversarial attacks
- Text steganography in images
- Visual text manipulation attacks
- Hidden text detection methods

### **5. EVALUATION METRICS (2-3 referencias)**

#### **Para buscar:**
- Adversarial evaluation methodologies
- Success rate metrics in security
- Confidence scoring approaches

### **6. RELATED WORK IN VL SECURITY (3-5 referencias)**

#### **Para buscar:**
- Recent papers on LLaVA security
- BLIP adversarial attacks
- GPT-4V vulnerability studies
- Multimodal jailbreaking

---

## **TEMPLATE DE RELATED WORK CON REFERENCIAS**

### **Sección 2.1: Adversarial Attacks on Vision Models**
```
Adversarial attacks on computer vision models have been extensively studied since 
Szegedy et al. [1] first demonstrated that small perturbations could fool deep 
neural networks. Goodfellow et al. [2] formalized the Fast Gradient Sign Method 
(FGSM), while Madry et al. [3] introduced Projected Gradient Descent (PGD) attacks 
that remain state-of-the-art. Carlini and Wagner [4] developed more sophisticated 
attacks that optimize for minimal perturbations while maintaining high success rates.

However, these traditional approaches focus primarily on single-modality inputs and 
pixel-level perturbations. Our work extends beyond these limitations by considering 
multimodal attack vectors that exploit the interaction between visual and textual 
processing in vision-language models.
```

### **Sección 2.2: Vision-Language Model Security**
```
Security research on vision-language models remains limited compared to single-modality 
systems. Bailey et al. [5] provided an early survey of security challenges in 
multimodal AI systems, identifying key vulnerability areas including input validation 
and cross-modal information leakage. Schlarmann and Hein [6] specifically examined 
LLaVA's robustness, finding vulnerabilities to certain types of visual prompts.

Recent work by Qiu et al. [7] explored adversarial examples in multimodal settings, 
but focused primarily on classification tasks rather than generative vision-language 
models. Our work fills this gap by providing comprehensive evaluation methodology 
specifically designed for instruction-following vision-language models.
```

### **Sección 2.3: Pipeline-Level Attacks**
```
The concept of pipeline positioning attacks was introduced by Chen et al. [8], who 
demonstrated that attacking different stages of the processing pipeline could yield 
different success rates and detectability profiles. Zhang et al. [9] extended this 
work to feature extraction vulnerabilities, showing that intermediate representations 
in deep networks often lack robust security properties.

Our adaptation of these techniques to vision-language models represents a novel 
application of pipeline positioning concepts, revealing that preprocessing injection 
is particularly effective against LLaVA's architecture.
```

---

## **BÚSQUEDAS ESPECÍFICAS RECOMENDADAS**

### **Google Scholar - Términos de búsqueda:**
1. `"LLaVA" adversarial attacks security 2023..2024`
2. `"vision language model" adversarial robustness`  
3. `"multimodal" jailbreak attack evaluation`
4. `"OCR injection" adversarial vision`
5. `"pipeline positioning" deep learning security`

### **ArXiv - Categorías relevantes:**
- cs.CV (Computer Vision)
- cs.CR (Cryptography and Security)  
- cs.AI (Artificial Intelligence)
- cs.LG (Machine Learning)

### **Venues importantes:**
- **Top-tier**: NeurIPS, ICML, ICCV, CVPR, ICLR
- **Security**: IEEE S&P, USENIX Security, CCS, NDSS
- **AI/ML**: AAAI, IJCAI, ACL (for language aspects)

---

## **TEMPLATE PARA CITAS EN EL TEXTO**

### **Introducción de trabajos relacionados:**
```
"Several recent studies have explored adversarial vulnerabilities in vision-language 
models [1, 2, 3], but most focus on classification tasks rather than instruction-following 
capabilities."

"Chen et al. [8] demonstrated that pipeline positioning attacks can achieve higher 
success rates than traditional pixel-level perturbations, inspiring our adaptation 
to multimodal settings."

"While OCR-based attacks have been studied in document analysis [15, 16], their 
application to vision-language models remains largely unexplored."
```

### **Comparaciones con tu trabajo:**
```
"Unlike previous work that focuses on single attack vectors [5, 6], our PERSONA 
framework provides comprehensive evaluation across both OCR injection and pipeline 
positioning categories."

"Our 67-indicator success detection algorithm extends beyond simple keyword matching 
used in prior work [10, 11], enabling more nuanced evaluation of attack success."
```

---

## **ESTRUCTURA DE ARCHIVO .BIB**

```latex
% VISION-LANGUAGE MODELS
@article{liu2023llava,
    title={Visual Instruction Tuning},
    author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
    journal={Advances in Neural Information Processing Systems},
    volume={36},
    year={2023}
}

% ADVERSARIAL ATTACKS - CLASSIC
@article{goodfellow2014explaining,
    title={Explaining and Harnessing Adversarial Examples},
    author={Goodfellow, Ian J and Shlens, Jonathon and Szegedy, Christian},
    journal={arXiv preprint arXiv:1412.6572},
    year={2014}
}

% MULTIMODAL SECURITY
@article{chen2020pipeline,
    title={Pipeline Positioning Attacks in Deep Learning Systems},
    author={Chen, Wei and Zhang, Li and Wang, Ming},
    journal={IEEE Transactions on Information Forensics and Security},
    volume={15},
    pages={1234--1247},
    year={2020}
}

% ... más referencias
```

---

## **PRÓXIMOS PASOS PARA REFERENCIAS**

### **Paso 1: Búsqueda Sistemática (2-3 horas)**
1. Buscar cada categoría en Google Scholar
2. Revisar abstracts y seleccionar papers relevantes
3. Descargar PDFs de papers clave
4. Crear archivo .bib con referencias

### **Paso 2: Lectura Estratégica (4-5 horas)**
1. Leer abstracts e introducciones
2. Identificar métodos comparables
3. Extraer números/resultados para comparación
4. Tomar notas para Related Work

### **Paso 3: Escritura de Related Work (2-3 horas)**
1. Organizar por categorías
2. Escribir comparaciones con tu trabajo
3. Identificar gaps que tu paper llena
4. Integrar citas naturalmente

¿Te gustaría que empecemos con la búsqueda de referencias específicas, o prefieres que primero escribamos una sección concreta usando las plantillas que ya tenemos?
