import streamlit as st

st.write("Salut")

a = st.text_input("Entrez un nombre", value="Nombre")

st.write(f"Le carré de votre nombre est : {int(a)^2}")