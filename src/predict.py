import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ---------------------------
# Load models
# ---------------------------
category_model = pickle.load(open("models/email_classifier.pkl", "rb"))
category_vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

urgency_model = pickle.load(open("models/urgency_model.pkl", "rb"))
urgency_vectorizer = pickle.load(open("models/urgency_vectorizer.pkl", "rb"))

# ---------------------------
# Category mapping
# ---------------------------
CATEGORY_MAPPING = {
    0: "Academic",
    1: "Complaint",
    2: "Request",
    3: "Feedback",
    4: "Spam",
    5: "General"
}

# ---------------------------
# Text cleaning
# ---------------------------
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# ---------------------------
# Prediction function
# ---------------------------
def predict_email(text):

    text = clean_text(text)

    # Category prediction
    text_vector = category_vectorizer.transform([text])
    category_id = category_model.predict(text_vector)[0]
    category = CATEGORY_MAPPING.get(category_id, "Unknown")

    category_conf = max(category_model.predict_proba(text_vector)[0]) * 100

    # Urgency prediction
    urgency_vector = urgency_vectorizer.transform([text])
    urgency = urgency_model.predict(urgency_vector)[0]
    urgency_conf = max(urgency_model.predict_proba(urgency_vector)[0]) * 100

    return category, category_conf, urgency, urgency_conf


# ---------------------------
# CLI testing
# ---------------------------
if __name__ == "__main__":

    user_input = input("Enter email text: ")

    cat, cat_conf, urg, urg_conf = predict_email(user_input)

    print("\nPrediction Result")
    print("------------------")
    print(f"Category: {cat} ({cat_conf:.2f}%)")
    print(f"Urgency: {urg} ({urg_conf:.2f}%)")