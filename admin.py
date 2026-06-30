import streamlit as st

st.set_page_config(page_title="Standard Calculator", page_icon="📱")
st.title("📱 Standard Calculator")

if "equation" not in st.session_state:
    st.session_state.equation = ""

def add_to_equation(value):
    st.session_state.equation += str(value)

def calculate_result():
    try:
        result = str(eval(st.session_state.equation))
        st.session_state.equation = result
    except Exception:
        st.session_state.equation = "Error"

def clear_display():
    st.session_state.equation = ""

st.text_input(
    "Display", 
    value=st.session_state.equation, 
    disabled=True, 
    label_visibility="collapsed"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add_to_equation, args=("7",), use_container_width=True)
    st.button("4", on_click=add_to_equation, args=("4",), use_container_width=True)
    st.button("1", on_click=add_to_equation, args=("1",), use_container_width=True)
    st.button("C", on_click=clear_display, use_container_width=True)

with col2:
    st.button("8", on_click=add_to_equation, args=("8",), use_container_width=True)
    st.button("5", on_click=add_to_equation, args=("5",), use_container_width=True)
    st.button("2", on_click=add_to_equation, args=("2",), use_container_width=True)
    st.button("0", on_click=add_to_equation, args=("0",), use_container_width=True)

with col3:
    st.button("9", on_click=add_to_equation, args=("9",), use_container_width=True)
    st.button("6", on_click=add_to_equation, args=("6",), use_container_width=True)
    st.button("3", on_click=add_to_equation, args=("3",), use_container_width=True)
    st.button("=", on_click=calculate_result, use_container_width=True, type="primary")

with col4:
    st.button("/", on_click=add_to_equation, args=("/",), use_container_width=True)
    st.button("*", on_click=add_to_equation, args=("*",), use_container_width=True)
    st.button("-", on_click=add_to_equation, args=("-",), use_container_width=True)
    st.button("+", on_click=add_to_equation, args=("+",), use_container_width=True)