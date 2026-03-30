import streamlit as st

a = st.text_input("Entrez un nombre", "4")

try:
    st.write("Le carré de votre nombre est", double(a)**2)
except ValueError:
    st.write("La valeur n'est pas valide")
