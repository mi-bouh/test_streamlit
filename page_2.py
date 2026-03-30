import streamlit as st

if "variable" in st.session_state:
    st.session_state.variable = st.session_state.variable
st.title("Salut !")

variable = st.text_input("Envoyer l'extrait", key="variable")
st.page_link("page_1.py", label="Page principale")