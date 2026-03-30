import streamlit as st
import pandas as pd



st.title("Cocorico !")
st.header("Analyse de chants d'oiseaux")
st.page_link("page_2.py", label="Choisissez un fichier :")
uploaded_file = st.file_uploader("Fichier :", type="mp3", label_visibility="collapsed")
st.button("Envoyer l'extrait")

