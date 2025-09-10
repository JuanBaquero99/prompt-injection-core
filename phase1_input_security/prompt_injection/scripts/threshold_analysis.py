"""
threshold_analysis.py
---------------------
Analysis of probability threshold impact on model performance.
Loads validation data, computes metrics (precision, recall, F1) for different thresholds, and visualizes results.
"""

import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

DATASET_PATH = 'data/dataset_final.csv'
df = pd.read_csv(DATASET_PATH)

# Load model and vectorizer
vectorizer, clf = joblib.load('data/rf_model.pkl')

# Use same split as training
from sklearn.model_selection import train_test_split
X = df['prompt']
y = df['label']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Vectorize validation set
X_val_vec = vectorizer.transform(X_val)
y_true = (y_val == "malicious").astype(int)

# Get prediction probabilities for validation
probs = clf.predict_proba(X_val_vec)[:, 1]  # Probability of 'malicious' class

# Print probability statistics
print("Probability summary for 'malicious' class (validation):")
print(f"Min: {probs.min():.4f}, Max: {probs.max():.4f}, Mean: {probs.mean():.4f}, Std: {probs.std():.4f}")
print(f"First 10 values: {probs[:10]}")

umbral_range = np.linspace(0, 0.5, 100)
results = []
for threshold in umbral_range:
    y_pred = (probs >= threshold).astype(int)
    tp = ((y_pred == 1) & (y_true == 1)).sum()
    tn = ((y_pred == 0) & (y_true == 0)).sum()
    fp = ((y_pred == 1) & (y_true == 0)).sum()
    fn = ((y_pred == 0) & (y_true == 1)).sum()
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    results.append({'threshold': threshold, 'precision': precision, 'recall': recall, 'f1': f1, 'fp': fp, 'fn': fn})

# Visualization
results_df = pd.DataFrame(results)
plt.figure(figsize=(10,6))
plt.plot(results_df['threshold'], results_df['precision'], label='Precision')
plt.plot(results_df['threshold'], results_df['recall'], label='Recall')
plt.plot(results_df['threshold'], results_df['f1'], label='F1-score')
plt.xlabel('Probability threshold')
plt.ylabel('Metric')
plt.title('Threshold impact on model performance (validation)')
plt.legend()
plt.grid(True)
plt.show()
print(results_df.sort_values('f1', ascending=False).head(5))
