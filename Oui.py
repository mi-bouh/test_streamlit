import streamlit as st
import time
import random
import librosa

# Variables d'affichage :
# progression : Barre de progression + Texte d'attente
# resultat : Nom de l'espèce d'oiseau renvoyé par le modèle
# nouveau : Réinitialisation de l'application après un test

if "progression" not in st.session_state:
    st.session_state.progression = False

if "resultat" not in st.session_state:
    st.session_state.resultat = False

if "nouveau" not in st.session_state:
    st.session_state.nouveau = False

if st.session_state.nouveau:
    st.session_state.resultat = False
    st.session_state.progression = False
    st.session_state.nouveau = False
    st.rerun()

if not st.session_state.progression and not st.session_state.resultat:
    audio = st.audio_input("Enregistrez !")
    oui = st.button("Soumettre l'enregistrement audio")

    if oui:
        st.session_state.progression = True
        st.rerun()

if st.session_state.progression:
    st.write("Veuillez patienter...")

    progress_bar = st.progress(0)
    y, sr = librosa.load(audio, duration=10.0)
    progress_bar.progress(50)
    for i in range(50):
        num = random.uniform(0, 0.15)
        time.sleep(num)
        progress_bar.progress(i + 1)

    time.sleep(0.8)
    st.session_state.progression = False
    st.session_state.resultat = True
    st.rerun()

if st.session_state.resultat:
    st.write("Cet oiseau est un oiseau ")
    reset = st.button("Détecter un nouvel oiseau")
    if reset:
        st.session_state.nouveau = True
        st.rerun()