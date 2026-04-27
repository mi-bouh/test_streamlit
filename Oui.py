import librosa
import streamlit as st

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")
oiseau = "Coucou"
afficher = False

for i in range(1):
    if oui:
        import time
        st.write("Veuillez patienter...")

        progress_bar = st.progress(0)

        for i in range(100):
            time.sleep(0.07)
            progress_bar.progress(i + 1)

        time.sleep(0.8)
        afficher = True

    oui = False
    if afficher:
        st.write("Cet oiseau est : ", oiseau)