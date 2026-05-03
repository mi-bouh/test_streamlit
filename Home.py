# Affichage de l'écran principal
if not st.session_state.progression and not st.session_state.resultat:
    audio_record = st.audio_input("Enregistrez un son (seules les 10 premières secondes seront analysées) :", sample_rate=22050)
    audio_upload = st.file_uploader("Ou téléversez un fichier :", type=["mp3", "wav"])
    oui = st.button("Soumettre l'enregistrement audio")

    if oui:
        if audio_record is None and audio_upload is None:
            st.error("Aucun enregistrement n'a été détecté !")

        # Dans le cas d'un fichier téléversé
        elif audio_record is None:
            if audio_upload.type in ["mp3", "wav"]:
                extension = os.path.splitext(audio_upload.name)[1]

                with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as tmp_file:
                    tmp_file.write(audio_upload.getvalue())
                    path = tmp_file.name
                    y, sr = librosa.load(path)
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
