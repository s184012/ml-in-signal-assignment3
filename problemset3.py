import librosa
import librosa.display
import IPython
import numpy as np
from scipy import linalg
from scipy import stats
import scipy.signal
from scipy.linalg import toeplitz
from scipy.signal import wiener
from scipy import signal
import matplotlib.pyplot as plt
import sounddevice as sd # only needed for playing
import soundfile as sf # only needed if playing does not work
from scipy.io import loadmat
from IPython.display import Audio
from sklearn.linear_model import LassoLars
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct

problem= 'problem3_1'
matdata = loadmat(f'{irname}.mat')