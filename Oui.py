import streamlit as st
import time
import random
import librosa
import io

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

if "audio" not in st.session_state:
    st.session_state.audio = None

if "oiseau" not in st.session_state:
    st.session_state.oiseau = "Colibri"

if st.session_state.nouveau:
    st.session_state.resultat = False
    st.session_state.progression = False
    st.session_state.nouveau = False
    st.rerun()

if not st.session_state.progression and not st.session_state.resultat:
    audio_test = st.audio_input("Attention ! Notez que seules les 10 premières secondes seront analysées !")
    oui = st.button("Soumettre l'enregistrement audio")

    if oui:
        if audio_test is None:
            st.write("Aucun enregistrement n'a été détecté !")
        else:
            st.session_state.audio = audio_test.getvalue()
            st.session_state.progression = True
            st.rerun()

if st.session_state.progression:
    st.write("Veuillez patienter...")

    progress_bar = st.progress(0)
    audio_buffer = io.BytesIO(st.session_state.audio)
    y, sr = librosa.load(audio_buffer, duration=10.0, sr=None)
    time.sleep(0.8)
    progress_bar.progress(30)

    for i in range(50):
        num = random.uniform(0, 0.15)
        time.sleep(num)
        progress_bar.progress(i + 51)

    time.sleep(0.8)
    # Insérer l'intégration du modèle ici éventuellement :
    st.session_state.oiseau = "Colibri"
    st.session_state.duration = librosa.get_duration(y=y, sr=sr)
    st.session_state.progression = False
    st.session_state.resultat = True
    st.rerun()

if st.session_state.resultat:
    st.write(f"L'espèce d'oiseau détectée est : {st.session_state.oiseau}")
    st.write(f"L'enregistrement a une durée de {st.session_state.duration} secondes")
    reset = st.button("Détecter un nouvel oiseau")
    if reset:
        st.session_state.nouveau = True
        st.rerun()