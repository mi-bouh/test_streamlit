import streamlit as st
import time
import librosa
import io
from Transfert import spectrogram_matrice, repeat_matrices

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
if "duration" not in st.session_state:
    st.session_state.duration = 0

# À la réinitialisation de l'application
if st.session_state.nouveau:
    st.session_state.resultat = False
    st.session_state.progression = False
    st.session_state.nouveau = False
    st.rerun()

# Affichage de l'écran principal
if not st.session_state.progression and not st.session_state.resultat:
    st.write("Fournissez un enregistrement audio à analyser :")
    st.write("Attention! Si deux enregistrements sont fournis, le fichier téléversé sera ignoré !")
    audio_record = st.audio_input("Attention ! Notez que seules les 10 premières secondes seront analysées !", sample_rate=22050)
    audio_upload = st.file_uploader("Ou téléversez un fichier", type=["mp3", "wav"])
    oui = st.button("Soumettre l'enregistrement audio")

    if oui:
        if audio_record is None and audio_upload is None:
            st.error("Aucun enregistrement n'a été détecté !")
        elif audio_record is None:
            type_mime = audio_upload.type
            if type_mime in ["mp3", "wav"]:
                st.session_state.audio = audio_upload.getvalue()
                y, sr = librosa.load(audio_upload)
                st.session_state.duration = librosa.get_duration(y=y, sr=sr)
                st.session_state.progression = True
                st.rerun()
            else:
                st.error("Le format du fichier n'est pas valide")
                st.rerun()
        else:
            st.session_state.audio = audio_record.getvalue()
            y, sr = librosa.load(audio_record)
            st.session_state.duration = librosa.get_duration(y=y, sr=sr)
            st.session_state.progression = True
            st.rerun()

# Affichage de la barre de chargement
if st.session_state.progression:
    st.write("Veuillez patienter...")

    progress_bar = st.progress(0)
    audio_buffer = io.BytesIO(st.session_state.audio)
    uniforme = repeat_matrices(spectrogram_matrice(audio_buffer))
    time.sleep(0.8)
    progress_bar.progress(10)
    # Insérer l'intégration du modèle ici éventuellement
    st.session_state.oiseau = "Colibri" # À modifier pour le renvoi du modèle
    progress_bar.progress(90)
    st.session_state.progression = False
    st.session_state.resultat = True
    progress_bar.progress(100)
    time.sleep(0.8)
    st.rerun()

if st.session_state.resultat:
    st.write(f"L'espèce d'oiseau détectée est : {st.session_state.oiseau}")
    st.write(f"L'enregistrement avait une durée de {st.session_state.duration} secondes")
    reset = st.button("Détecter un nouvel oiseau")
    if reset:
        st.session_state.nouveau = True
        st.rerun()