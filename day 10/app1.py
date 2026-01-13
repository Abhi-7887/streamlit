import streamlit as st

st.title("some basic commands in streamlit")

name=  st.text_input("enter your name :")

if st.button ("submit"):
    st.write("hello",name)
