import streamlit as st

a = st.text_input("Entrez un nombre", "4")

try:
    b = int(a)**2
except ValueError:
    b = "Vous n'avez pas entré de nombre"

st.write("Le carré de votre nombre est", int(a)**2)