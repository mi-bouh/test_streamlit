import librosa
import streamlit as st
import time

if "afficher" not in st.session_state:
    st.session_state.afficher = False

if "nouveau" not in st.session_state:
    st.session_state.nouveau = False

if st.session_state.nouveau:
    st.session_state.afficher = False

if not st.session_state.afficher:
    audio = st.audio_input("Enregistrez !")
    oui = st.button("Soumettre l'enregistrement audio")
    oiseau = "Coucou"

    if oui:
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
        st.session_state.nouveau = st.button("Détecter un nouvel oiseau")