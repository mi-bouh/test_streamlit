import librosa

audio = "01 Plus tôt.mp3"
print(round(librosa.get_duration(path = audio), 3))