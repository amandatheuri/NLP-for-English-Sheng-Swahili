import streamlit as st
import pickle
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

with open("language_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌍 Language Identification System")
st.write("Enter short text in English, Swahili, Sheng, or Kikuyu.")

user_input = st.text_area("Enter text:")

if st.button("Predict Language"):
    if user_input.strip():
        cleaned = clean_text(user_input)
        prediction = model.predict([cleaned])[0]
        st.success(f"🌍 Predicted Language: **{prediction}**")
    else:
        st.warning("Please enter some text.")