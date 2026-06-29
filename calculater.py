import streamlit as st

def calculate(num1,num2,operator):
    if operator =="+":
        return num1 + num2
    elif operator =="-":
        return num1 - num2
    elif operator =="*":
        if num2==0:
            return "cannot divide by zero"
        return num1 * num2
    elif operator =="/":
        return num1 / num2
    elif operator =="**":
        return num1 ** num2
    elif operator =="//":
        return num1 // num2
    elif operator =="%":
        return num1 % num2
    else:
        return "invalid operator"

st.title("calculator")
num1= st.number_input("enter the first number")
num2= st.number_input("enter the second number")
operator= st.selectbox("select the operator",["+","-","/","*","%","**","//"])
if st.button("calculate"):
    result = calculate(num1,num2,operator)

    st.write("the result is:",result)