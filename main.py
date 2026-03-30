import streamlit as st

a = st.text_input("Entrez un nombre", "4")
st.write("Le carré de votre nombre est", int(a)**2)