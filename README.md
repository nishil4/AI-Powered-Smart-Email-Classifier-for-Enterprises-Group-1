<<<<<<< HEAD
# 📧 AI-Powered Smart Email Intelligence System

## 🚀 Project Overview

Enterprises receive thousands of emails daily, including customer complaints, support requests, promotions, updates, and spam. Manually triaging these emails is inefficient and delays response times.

This project builds an end-to-end AI-powered email intelligence system that:

- Automatically classifies emails into 6 categories
- Detects urgency levels (High / Medium / Low)
- Provides an interactive analytics dashboard for monitoring and filtering emails

The solution improves operational efficiency by prioritizing critical emails and reducing manual workload.

---

## 🎯 Key Features

- ✅ Multi-class email categorization (6 enterprise categories)
- ✅ Urgency detection using hybrid rule-based + ML approach
- ✅ Handles imbalanced classes using weighted optimization
- ✅ 98%+ classification accuracy
- ✅ ~99% urgency detection accuracy
- ✅ Interactive Streamlit dashboard
- ✅ Real-time email classification support
- ✅ Advanced filtering (category, urgency, keyword search)
- ✅ Data visualization with Plotly (pie charts, bar charts, trends)

---

## 🧠 Machine Learning Approach

### 1️⃣ Data Preprocessing

- Lowercasing text
- Removing special characters
- Whitespace normalization
- Creation of clean_text column
- Handling class imbalance

### 2️⃣ Text Vectorization

- TF-IDF (Term Frequency–Inverse Document Frequency)
- 10,000 max features
- Sparse high-dimensional representation

### 3️⃣ Model Architecture

- Logistic Regression (multi-class classification)
- Class weighting for urgency detection
- Model persistence using Pickle

---

## 📊 Model Performance

| Task                          | Accuracy  |
| ----------------------------- | --------- |
| Email Category Classification | **98.4%** |
| Urgency Detection             | **98.9%** |

- High recall for urgent emails (~93%)
- Balanced precision and recall across all classes
- Robust performance on test dataset

---

## 📊 Dashboard Features

The Streamlit dashboard includes:

- 📌 Category Distribution (Donut Chart)
- 📌 Urgency Distribution
- 📌 Email Count by Category (Bar Chart)
- 📌 Email Volume Trend (Time Series)
- 📌 Interactive Filtering (Category / Urgency)
- 📌 Keyword-based search
- 📌 Live email classification input

---

## 🛠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Plotly
- Pickle (Model Serialization)

---

## 📂 Project Structure
=======
# 📧 AI-Powered Smart Email Intelligence System

## 🚀 Project Overview

Enterprises receive thousands of emails daily, including customer complaints, support requests, promotions, updates, and spam. Manually triaging these emails is inefficient and delays response times.

This project builds an end-to-end AI-powered email intelligence system that:

- Automatically classifies emails into 6 categories
- Detects urgency levels (High / Medium / Low)
- Provides an interactive analytics dashboard for monitoring and filtering emails

The solution improves operational efficiency by prioritizing critical emails and reducing manual workload.

---

## 🎯 Key Features

- ✅ Multi-class email categorization (6 enterprise categories)
- ✅ Urgency detection using hybrid rule-based + ML approach
- ✅ Handles imbalanced classes using weighted optimization
- ✅ 98%+ classification accuracy
- ✅ ~99% urgency detection accuracy
- ✅ Interactive Streamlit dashboard
- ✅ Real-time email classification support
- ✅ Advanced filtering (category, urgency, keyword search)
- ✅ Data visualization with Plotly (pie charts, bar charts, trends)

---

## 🧠 Machine Learning Approach

### 1️⃣ Data Preprocessing

- Lowercasing text
- Removing special characters
- Whitespace normalization
- Creation of clean_text column
- Handling class imbalance

### 2️⃣ Text Vectorization

- TF-IDF (Term Frequency–Inverse Document Frequency)
- 10,000 max features
- Sparse high-dimensional representation

### 3️⃣ Model Architecture

- Logistic Regression (multi-class classification)
- Class weighting for urgency detection
- Model persistence using Pickle

---

## 📊 Model Performance

| Task                          | Accuracy  |
| ----------------------------- | --------- |
| Email Category Classification | **98.4%** |
| Urgency Detection             | **98.9%** |

- High recall for urgent emails (~93%)
- Balanced precision and recall across all classes
- Robust performance on test dataset

---

## 📊 Dashboard Features

The Streamlit dashboard includes:

- 📌 Category Distribution (Donut Chart)
- 📌 Urgency Distribution
- 📌 Email Count by Category (Bar Chart)
- 📌 Email Volume Trend (Time Series)
- 📌 Interactive Filtering (Category / Urgency)
- 📌 Keyword-based search
- 📌 Live email classification input

---

## 🛠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Plotly
- Pickle (Model Serialization)

---

## 📂 Project Structure
>>>>>>> 225523f2f4667903f6db7ff650d61bf1228d4cb7
