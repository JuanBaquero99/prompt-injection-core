import joblib
import pandas as pd
import os

def cargar_modelo(model_path):
    vectorizer, clf = joblib.load(model_path)
    return vectorizer, clf

def predecir_prompts(prompts_path, model_path):
    with open(prompts_path, 'r', encoding='utf-8') as f:
        prompts = [line.strip() for line in f if line.strip()]
    vectorizer, clf = cargar_modelo(model_path)
    X_vec = vectorizer.transform(prompts)
    preds = clf.predict(X_vec)
    for prompt, pred in zip(prompts, preds):
        print(f"Prompt: {prompt}\nPredicción: {pred}\n{'-'*40}")

if __name__ == "__main__":
    prompts_path = os.path.join("data", "prompts_test.txt")
    model_path = os.path.join("data", "rf_model.pkl")
    predecir_prompts(prompts_path, model_path)
