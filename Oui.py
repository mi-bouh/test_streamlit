import streamlit as st
from mutagen.mp3 import MP3 as mp

def longueur(file):
    return file.info.length

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")
file = mp(audio)

if oui:
    st.audio(audio)
    st.write(longueur(file))