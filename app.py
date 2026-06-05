import streamlit as st
import pickle
import random
import re

# =====================================
# LOAD MODEL & VECTORIZER
# =====================================

try:
    model = pickle.load(open("sentiment_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
except FileNotFoundError:
    st.error(
        "Model files not found. Please make sure sentiment_model.pkl and vectorizer.pkl are in the same folder."
    )
    st.stop()

# =====================================
# HAPPY / UNHAPPY MESSAGES
# =====================================

happy_messages = {
    "happy_1": "😊 Great choice! Customers seem very happy with this product.",
    "happy_2": "🎉 Excellent! This review expresses a positive experience.",
    "happy_3": "👍 Nice! The overall sentiment is positive.",
    "happy_4": "🌟 This review shows customer satisfaction."
}

unhappy_messages = {
    "unhappy_1": "😞 Unfortunately, this review expresses dissatisfaction.",
    "unhappy_2": "⚠️ Customers may not be happy with this product.",
    "unhappy_3": "👎 The sentiment appears negative.",
    "unhappy_4": "💔 This review indicates a poor experience."
}

# =====================================
# TEXT CLEANING
# =====================================

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# =====================================
# SENTIMENT FUNCTION
# =====================================

def predict_sentiment(review_text):

    cleaned = clean_text(review_text)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    score = model.decision_function(vector)[0]

    confidence = min(
        100,
        round(abs(score) * 20, 2)
    )

    return prediction, confidence

# =====================================
# STREAMLIT UI
# =====================================

st.set_page_config(
    page_title="Amazon Review Sentiment Analysis",
    page_icon="🛒"
)

st.title("🛒 Amazon Review Sentiment Analysis")

st.write(
    "Enter an Amazon product review and predict whether it is Positive or Negative."
)

review = st.text_area(
    "Enter Review",
    height=150
)

if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:

        prediction, confidence = predict_sentiment(review)

        # Amazon Polarity
        # 0 = Negative
        # 1 = Positive

        if prediction == 1:

            st.success("Positive Review 😊")

            st.info(
                random.choice(
                    list(happy_messages.values())
                )
            )

        else:

            st.error("Negative Review 😞")

            st.warning(
                random.choice(
                    list(unhappy_messages.values())
                )
            )

        st.metric(
            "Confidence Score",
            f"{confidence}%"
        )

# =====================================
# SAMPLE REVIEWS
# =====================================

st.subheader("Sample Positive Reviews")

st.code(
"""
This product is amazing and works perfectly.

Excellent quality and worth every penny.

Fantastic purchase. Highly recommended.
"""
)

st.subheader("Sample Negative Reviews")

st.code(
"""
Worst product ever. Waste of money.

Very disappointed with the quality.

The item stopped working after one day.
"""
)