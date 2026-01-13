import streamlit as st

st.title(" make a simple alculator app")

num1 = st.number_input("enter the first no.")
num2 = st.number_input("enter the second no.")


operations = st.selectbox("select operation", ["multiply","divide","add","subtract"])

if st.button("calculate"):
    if operations =="add":
        result= num1+num2
    elif operations =="subtract":
        result= num1-num2
    elif operations =="multiply":
        result= num1*num2
    elif operations =="divide":
        if num2 != 0:
            result= num1/num2
        else:
            result = "error!! can not divide by 0"
    st.write("result",result)