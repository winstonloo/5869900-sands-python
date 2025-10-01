import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from signals import *

def time_shift(signal, shift, s_r):
    shift_samples = int(shift * s_r)
    if shift_samples > 0:
        return np.concatenate((np.zeros(shift_samples), signal[:-shift_samples]))
    elif shift_samples < 0:
        return np.concatenate((signal[-shift_samples:], np.zeros(-shift_samples)))
    else:
        return signal
    
def time_scale(signal, scale):
    indices = np.arange(0, len(signal), scale)
    indices = indices[indices < len(signal)].astype(int)
    return signal[indices]

def amplitude_scale(signal, scale):
    return signal * scale

def add_signals(signal1, signal2):
    length = min(len(signal1), len(signal2))
    return signal1[:length] + signal2[:length] 

def multiply_signals(signal1, signal2):
    length = min(len(signal1), len(signal2))
    return signal1[:length] * signal2[:length]
