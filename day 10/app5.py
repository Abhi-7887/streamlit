import streamlit as st
import google.generativeai as genai

st.title("welcome to streamlit app")

user_input = st.text_input("ask me anything")

genai.configure(api_key="AIzaSyCG-z4sWIwdVVqMKlb_v7m4mmF8XPIwyXk")

model = genai.GenerativeModel("models/gemini-3-flash-preview")

if user_input:
    response=model.generate_content(user_input)
    st.write("response:", response.text)