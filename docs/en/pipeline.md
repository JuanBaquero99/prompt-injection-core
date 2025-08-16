# Dataset Processing Pipeline Documentation

## 1. Data Collection
- Public datasets downloaded from Hugging Face:
  - deepset/prompt-injections
  - xTRam1/safe-guard-prompt-injection
  - yanismiraoui/prompt_injections
  - (optional) qualifire/prompt-injections-benchmark (requires authentication)
- Data saved as pandas DataFrame.

## 2. Normalization
- A normalization function was created for each dataset, unifying the fields:
  - prompt
  - label (benign/malicious)
  - type
  - source
  - lang

## 3. Unification and Cleaning
- All normalized datasets concatenated into a single DataFrame.
- Duplicate prompts removed, keeping only unique examples.

## 4. Class Balancing
- Classes (benign/malicious) balanced using only unique examples.
- Final dataset size equals the minority group.

## 5. Export
- Final dataset exported to `data/dataset_final.csv`.

## 6. Validation
- A script was created to validate the dataset:
  - Count by source and label
  - Check for real duplicates
  - Check for empty prompts
  - Examples by source

## 7. Next Step Recommendation
- Split the dataset into training/validation.
- Train and evaluate prompt injection detection models.

---

This pipeline ensures a clean, balanced dataset ready for experimentation and model training.
