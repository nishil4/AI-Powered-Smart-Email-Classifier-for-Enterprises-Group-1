import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pickle

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/processed/module3_final_train_output.csv")

X = df["text"]
y = df["urgency"]

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_tfidf = vectorizer.fit_transform(X)

# -----------------------------
# Logistic Regression Model
# -----------------------------
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_tfidf, y)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_tfidf)

# -----------------------------
# Evaluation
# -----------------------------
print("\nAccuracy:", accuracy_score(y, y_pred))

print("\nClassification Report:\n")
print(classification_report(y, y_pred))

# -----------------------------
# Save Model
# -----------------------------
pickle.dump(model, open("models/urgency_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/urgency_vectorizer.pkl", "wb"))

print("\nUrgency model saved successfully.")