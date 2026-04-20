import streamlit as st

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")

if oui:
    st.audio(audio)