from mutagen.mp3 import MP3 as mp

audio = mp("01 Plus tôt.mp3")
length = audio.info.length