import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Page config
st.set_page_config(page_title="IMDB Sentiment Analysis", layout="centered")

st.title("IMDB Movie Review Sentiment Analysis")

st.write("Enter a movie review to classify it as Positive or Negative.")

# Load word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load trained model
model = load_model("simple_rnn_imdb.h5")

# Helper function to decode review
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Preprocess user text
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Prediction function
def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)
    sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"
    return sentiment, prediction[0][0]


# Example reviews
example_reviews = [
    "This movie was amazing and the acting was brilliant.",
    "The film was boring and the story made no sense.",
    "I loved the cinematography and the emotional storyline.",
    "The movie was too long and completely predictable."
]

selected_review = st.selectbox("Try an example review", example_reviews)

# Text input
review = st.text_area("Movie Review", selected_review)

# Prediction button
if st.button("Classify"):

    sentiment, score = predict_sentiment(review)

    st.subheader("Result")

    if sentiment == "Positive":
        st.success("Positive Review 😊")
    else:
        st.error("Negative Review 😞")

    st.write("Prediction Score:", float(score))

    st.progress(float(score))


# About model section
st.markdown("---")

st.subheader("About the Model")

st.write("""
This sentiment analysis model is built using a **Simple Recurrent Neural Network (RNN)** trained on the **IMDB movie review dataset**.

**Model Details**
- Architecture: Simple RNN
- Dataset: IMDB Movie Reviews
- Task: Binary Sentiment Classification
- Framework: TensorFlow / Keras
""")
