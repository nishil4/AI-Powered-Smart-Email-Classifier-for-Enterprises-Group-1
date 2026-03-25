import pandas as pd
from urgency_rule_based import detect_urgency_rule

# -----------------------------
# Load cleaned datasets
# -----------------------------
train_df = pd.read_csv("data/processed/train_clean.csv")
test_df = pd.read_csv("data/processed/test_clean.csv")

print("Datasets loaded successfully")

# -----------------------------
# Create urgency labels
# -----------------------------
train_df["urgency"] = train_df["clean_text"].apply(detect_urgency_rule)
test_df["urgency"] = test_df["clean_text"].apply(detect_urgency_rule)

print("Urgency labels generated")

# -----------------------------
# Save datasets
# -----------------------------
train_df.to_csv("data/processed/train_with_urgency.csv", index=False)
test_df.to_csv("data/processed/test_with_urgency.csv", index=False)

print("✅ Urgency datasets saved successfully")