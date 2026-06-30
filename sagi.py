import streamlit as st
st.title("password checker")
password=st.text_input("enter the password",type="password")
if st.button("submit"):
    if password=="noble123": 
        st.success("$ correct password")
    else:
        st.error(" wrong password") 