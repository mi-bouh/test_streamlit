import librosa
import streamlit as st

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")
oiseau = "Coucou"

if oui:
    st.write("Cet oiseau est : ", oiseau)