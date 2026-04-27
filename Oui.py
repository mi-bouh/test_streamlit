import librosa
import math
import streamlit as st

audio = st.audio_input("Enregistrez !")
# audio = "01 Plus tôt.mp3"
oui = st.button("Soumettre l'enregistrement audio")
duration = librosa.get_duration(path = audio)
minutes = math.floor(duration / 60)
secondes = duration - minutes

if oui:
    st.audio(audio)
    st.write(minutes, "minutes")
    st.write(secondes, "secondes")
    st.write(secondes-math.floor(secondes), "reste")