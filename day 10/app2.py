import streamlit as st

st.write("some basic commands like slider button, etc")

age= st.slider("enter your age", 1, 100, 25)
city = st.selectbox("choose your city",[" delhi", "mumbai", "pune", "sambhajinagar"])

if st.button("show details :"):
    st.write("age", age)
    st.write("city",city)