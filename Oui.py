import librosa
import math
import streamlit as st

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")
duration = librosa.get_duration(path = audio)
heures = math.floor(duration / 3660)

if oui:
    st.audio(audio)
    st.write(heures)