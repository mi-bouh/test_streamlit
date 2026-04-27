import librosa
import streamlit as st

audio = st.audio_input("Enregistrez !")
# audio = "01 Plus tôt.mp3"
oui = st.button("Soumettre l'enregistrement audio")
duration = librosa.get_duration(path = audio)
heures = duration / 60

if oui:
    st.audio(audio)
    st.write(heures, "minutes")