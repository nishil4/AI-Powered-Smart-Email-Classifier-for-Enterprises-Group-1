import os
import pandas as pd
import torch
import numpy as np
from datasets import Dataset
from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

train_path = os.path.join(BASE_DIR, "data", "processed", "train_clean.csv")
test_path = os.path.join(BASE_DIR, "data", "processed", "test_clean.csv")

# -----------------------------
# Load Data
# -----------------------------
print("Loading processed data...")

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

train_df = train_df[["clean_text", "category_id"]]
test_df = test_df[["clean_text", "category_id"]]

train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# -----------------------------
# Load Tokenizer
# -----------------------------
print("Loading DistilBERT tokenizer...")

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize_function(example):
    return tokenizer(
        example["clean_text"],
        padding="max_length",
        truncation=True,
        max_length=128
    )

train_dataset = train_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)

train_dataset = train_dataset.rename_column("category_id", "labels")
test_dataset = test_dataset.rename_column("category_id", "labels")

train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
test_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

# -----------------------------
# Load Model
# -----------------------------
print("Loading DistilBERT model...")

num_labels = 6

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels
)

# -----------------------------
# Metrics Function
# -----------------------------
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=1)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, predictions, average="weighted"
    )
    acc = accuracy_score(labels, predictions)
    return {
        "accuracy": acc,
        "f1": f1,
        "precision": precision,
        "recall": recall,
    }

# -----------------------------
# Training Arguments
# -----------------------------
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_dir="./logs",
    load_best_model_at_end=True
)

# -----------------------------
# Trainer
# -----------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics
)

# -----------------------------
# Train
# -----------------------------
print("Training started...")
trainer.train()

# -----------------------------
# Save Model
# -----------------------------
model_path = os.path.join(BASE_DIR, "models", "distilbert_model")

model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)
metrics = trainer.evaluate()

print("\n===== Final Evaluation =====")
print("Accuracy:", round(metrics["eval_accuracy"] * 100, 2), "%")
print("F1 Score:", round(metrics["eval_f1"] * 100, 2), "%")
print("Precision:", round(metrics["eval_precision"] * 100, 2), "%")
print("Recall:", round(metrics["eval_recall"] * 100, 2), "%")
print("\nDistilBERT model trained and saved successfully.")