import streamlit as st

audio_path = "01 Plus tôt.mp3"

st.write("Extraits audio :")
st.audio(audio_path, format="audio/mpeg")
a = st.text_input("Écrire ici :", "Valeur initiale")
st.write("Vous avez écrit :", a)