import streamlit as st
import pandas as pd

st.title("Cocorico !")
st.header("Analyse de chants d'oiseaux")
uploaded_file = st.file_uploader("Choisissez un fichier :")
st.button("Envoyer l'extrait")