import streamlit as st
import pandas as pd

st.title("Cocorico !")
st.header("Analyse de chants d'oiseaux")
uploaded_file = st.file_uploader("Choisissez un fichier :", type="mp3")
st.button("Envoyer l'extrait")
st.page_link("page_2.py")