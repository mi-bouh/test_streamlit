import streamlit as st

st.title("Salut !")

variable = st.text_input("Envoyer l'extrait", key="variable")
st.page_link("page_1.py", label="Page principale")