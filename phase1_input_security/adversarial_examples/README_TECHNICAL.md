# PERSONA Framework - Technical Documentation

## Overview

The PERSONA (Pipeline-Enhanced Recognition for Stealthy Optical Network Attacks) framework implements advanced adversarial techniques targeting vision-language models. This documentation provides technical specifications and execution procedures for empirical evaluation.

## Framework Architecture

### Core Components

**OCR Injection Module** (`attack_generators/ocr_injection.py`)
- Invisible text embedding using Unicode zero-width characters
- Steganographic data hiding via LSB manipulation  
- Transparent overlay injection with alpha channel control
- Microscopic text rendering below typical OCR thresholds

**Pipeline Positioning Module** (`attack_generators/pipeline_positioning.py`)
- Preprocessing injection targeting input normalization stages
- Feature extraction manipulation affecting embedding spaces
- Attention mechanism hijacking through adversarial patches
- Multi-stage coordinated attacks across processing pipeline

### Attack Dataset Specification

Generated adversarial samples: 40 total
- OCR-based attacks: 20 samples across 4 techniques
- Pipeline-aware attacks: 20 samples across 4 techniques
- Format: PNG images with embedded adversarial content
- Resolution: Variable, optimized per technique

## Empirical Evaluation Methodology

### Target Model Configuration
- **Model**: LLaVA-1.5-7B (Large Language and Vision Assistant)
- **Architecture**: Vision encoder + Language model pipeline
- **Input processing**: CLIP vision transformer + Vicuna-7B
- **Evaluation metric**: Attack success rate and response analysis

### Execution Environment
- **Platform**: Google Colab (free tier)
- **Hardware**: Tesla T4 GPU (16GB VRAM)
- **Runtime**: Python 3.10, PyTorch 2.7+, Transformers 4.37+
- **Memory allocation**: 12GB RAM, optimized for model loading

### Testing Protocol

**Phase 1: Environment Setup** (2-3 minutes)
- Dependency installation and verification
- GPU allocation and memory optimization
- Hardware capability assessment

**Phase 2: Data Upload** (1 minute)
- Adversarial dataset upload (`ataques_persona.zip`)
- File extraction and validation
- Sample distribution verification

**Phase 3: Model Loading** (3-4 minutes)
- LLaVA model download and initialization
- GPU memory allocation optimization
- Model configuration for inference

**Phase 4: Testing Execution** (10-15 minutes)
- Balanced sampling: 8 OCR + 8 Pipeline attacks
- Individual attack evaluation against model
- Response analysis and success classification

**Phase 5: Result Analysis** (2 minutes)
- Statistical analysis generation
- Visualization creation
- Data export for further analysis

## Success Evaluation Criteria

### Attack Success Indicators
- Direct instruction compliance
- Security bypass behavior
- Unauthorized information disclosure
- System prompt revelation
- Safety filter circumvention

### Scoring Methodology
- Binary success classification (successful/failed)
- Confidence score (0.0 - 1.0 scale)
- Response quality assessment
- Inference time measurement

## Expected Outputs

### Quantitative Metrics
- Success rates per attack category
- Comparative effectiveness analysis (OCR vs Pipeline)
- Statistical significance testing
- Performance benchmarking data

### Qualitative Analysis
- Response content evaluation
- Attack vector effectiveness assessment
- Model vulnerability identification
- Defense mechanism recommendations

### Data Artifacts
- `persona_llava_results_[timestamp].json` - Complete experimental data
- `persona_llava_analysis_[timestamp].png` - Statistical visualizations
- Structured dataset suitable for academic publication

## Repository Independence

The implementation is designed as a self-contained system:
- No GitHub repository cloning required
- All code embedded in notebook cells
- Dataset included in upload package
- Dependencies managed through notebook environment

This approach ensures reproducibility and eliminates external dependency issues during execution.

## Technical Support

### Common Issues and Solutions

**GPU Allocation Failure**
- Solution: Runtime → Restart runtime → Reselect GPU

**Memory Overflow Errors**  
- Solution: Reduce batch size or restart with fresh memory allocation

**Model Loading Timeout**
- Solution: Wait for complete download, avoid interruption

**Upload Failures**
- Solution: Verify ZIP file integrity, retry upload process

### Performance Optimization
- Execute cells sequentially to prevent memory conflicts
- Maintain browser tab activity during long operations
- Monitor GPU memory usage through provided diagnostics
- Clear intermediate variables between major operations

## Research Applications

This framework enables empirical research in:
- Adversarial robustness of vision-language models
- Comparative analysis of attack methodologies
- Security vulnerability assessment
- Defense mechanism development
- Model safety evaluation protocols

The generated data provides quantitative evidence for academic publication and contributes to the security research community's understanding of multimodal AI vulnerabilities.
