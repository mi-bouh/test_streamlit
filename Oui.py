import librosa
import streamlit as st

audio = st.audio_input("Enregistrez !")
oui = st.button("Soumettre l'enregistrement audio")
oiseau = "Coucou"
if "afficher" not in st.session_state:
    st.session_state.afficher = False

if oui:
    import time
    st.write("Veuillez patienter...")

    progress_bar = st.progress(0)

    for i in range(100):
        time.sleep(0.07)
        progress_bar.progress(i + 1)

    time.sleep(0.8)
    st.session_state.afficher = True
    oui = False
    st.rerun()

if st.session_state.afficher:
    st.write("Cet oiseau est : ", oiseau)