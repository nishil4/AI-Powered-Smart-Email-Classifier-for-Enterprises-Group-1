import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pickle

# -----------------------------
# Load Train & Test datasets
# -----------------------------
train_df = pd.read_csv("data/processed/train_with_urgency.csv")
test_df = pd.read_csv("data/processed/test_with_urgency.csv")

X_train = train_df["clean_text"]
y_train = train_df["urgency"]

X_test = test_df["clean_text"]
y_test = test_df["urgency"]

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -----------------------------
# Logistic Regression Model
# -----------------------------
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train_tfidf, y_train)

# -----------------------------
# Evaluation
# -----------------------------
y_pred = model.predict(X_test_tfidf)

print("\nTest Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
pickle.dump(model, open("models/urgency_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/urgency_vectorizer.pkl", "wb"))

print("\n Urgency model saved successfully.")