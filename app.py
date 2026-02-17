import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import re

st.set_page_config(page_title="AI Smart Email Classifier", layout="wide")

st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 700;
        background: linear-gradient(90deg, #4A90E2, #50E3C2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📧 AI Smart Email Intelligence Dashboard</div>', unsafe_allow_html=True)

# -----------------------
# Load Models
# -----------------------
model = pickle.load(open("category_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
urgency_model = pickle.load(open("urgency_model.pkl", "rb"))

# -----------------------
# Business Category Mapping
# -----------------------
category_mapping = {
    "spam": "Spam",
    "promotions": "Feedback",
    "social_media": "Feedback",
    "forum": "Complaints",
    "verify_code": "Requests",
    "updates": "Requests"
}

# -----------------------
# Load Data
# -----------------------
df = pd.read_csv("clean_train.csv")

# Convert dataset categories to business categories
df["category"] = df["category"].map(category_mapping).fillna(df["category"])

# Dummy Date Column (for demo)
df["date"] = pd.date_range(start="2024-01-01", periods=len(df), freq="H")

# -----------------------
# Sidebar Filters
# -----------------------
st.sidebar.title("🔎 Filters")

selected_category = st.sidebar.multiselect(
    "Filter by Category",
    options=df["category"].unique(),
    default=df["category"].unique()
)

selected_urgency = st.sidebar.multiselect(
    "Filter by Urgency",
    options=df["urgency"].unique(),
    default=df["urgency"].unique()
)

keyword = st.sidebar.text_input("Search by Keyword")

# Apply filters
filtered_df = df[
    (df["category"].isin(selected_category)) &
    (df["urgency"].isin(selected_urgency))
]

if keyword:
    filtered_df = filtered_df[filtered_df["clean_text"].str.contains(keyword, case=False)]

# -----------------------
# Dashboard Title
# -----------------------
st.markdown("---")

# -----------------------
# Metrics Section
# -----------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📨 Total Emails", value=len(filtered_df))

with col2:
    st.metric(label="🚨 High Urgency", value=len(filtered_df[filtered_df["urgency"] == "High"]))

with col3:
    st.metric(label="📂 Categories", value=filtered_df["category"].nunique())

# -----------------------
# Charts Section
# -----------------------
col4, col5 = st.columns(2)

fig_category = px.pie(
    filtered_df,
    names="category",
    hole=0.4,
    title="Category Distribution"
)
fig_category.update_layout(template="plotly_dark")
col4.plotly_chart(fig_category, use_container_width=True)

fig_urgency = px.pie(
    filtered_df,
    names="urgency",
    hole=0.4,
    title="Urgency Distribution"
)
fig_urgency.update_layout(template="plotly_dark")
col5.plotly_chart(fig_urgency, use_container_width=True)

st.markdown("---")

category_counts = filtered_df["category"].value_counts().reset_index()
category_counts.columns = ["category", "count"]

fig_bar = px.bar(
    category_counts,
    x="category",
    y="count",
    title="Email Count by Category",
    color="category"
)

fig_bar.update_layout(template="plotly_dark")
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("### 📈 Email Volume Trend")

trend_df = filtered_df.groupby(filtered_df["date"].dt.date).size().reset_index(name="count")

fig_trend = px.line(trend_df, x="date", y="count", markers=True)
fig_trend.update_layout(template="plotly_dark")

st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------
# Email Explorer
# -----------------------
st.markdown("## 📩 Email Explorer")

st.dataframe(filtered_df[["subject", "category", "urgency", "date"]])

st.markdown("## ✉️ Live Email Classification")

user_input = st.text_area("Paste an email here")

if st.button("Classify Email"):
    if user_input:
        processed_text = user_input.lower()
        vectorized = vectorizer.transform([processed_text])
        
        raw_category = model.predict(vectorized)[0]
        category_pred = category_mapping.get(raw_category, raw_category)

        urgency_pred = urgency_model.predict(vectorized)[0]
        
        st.success(f"Predicted Category: {category_pred}")
        st.warning(f"Predicted Urgency: {urgency_pred}")