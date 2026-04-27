import librosa
import streamlit as st

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")
oiseau = "Coucou"


if oui:
    import time

    st.title("Exemple de barre de chargement")

    progress_bar = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)

    st.write("Cet oiseau est : ", oiseau)