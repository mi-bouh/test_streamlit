import librosa
import numpy as np

#
def spectrogram_matrice(file_in,numbers_of_bins=128):
    try:
        y, sr = librosa.load(file_in,sr=22050,duration=10)
        if len(y) == 0:
            return None
        mel = librosa.feature.melspectrogram(y=y,sr=sr,n_mels=numbers_of_bins)
        mel = repeat_matrices(mel)
        log_mel = librosa.power_to_db(mel,ref=np.max)
        return log_mel.astype(np.float32)
    except Exception as e:(
        print(e))
    return None

def repeat_matrices(mel,target=431):
    if mel.shape[1] < target :
        repeats = int(np.ceil(target / mel.shape[1]))
        mel = np.tile(mel,(1,repeats))
    return mel[:, :target]