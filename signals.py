import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequency f, start s_t, end e_t, amplitude a, sample rate s_t

def create_sine_wave(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    t = np.linspace(s_t, e_t, int(s_r * duration))
    return t, a * np.sin(2 * np.pi * f * t)

def create_square_wave(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    t = np.linspace(s_t, e_t, int(s_r * duration))
    sine_wave = np.sin(2 * np.pi * f * t)
    return t, a * np.sign(sine_wave)

def create_sawtooth_wave(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    t = np.linspace(s_t, duration, int(s_r * duration))
    return a * signal.sawtooth(2 * np.pi * f * t)

def create_triangle_wave(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    t = np.linspace(s_t, e_t, int(s_r * duration))
    return a * signal.sawtooth(2 * np.pi * f * t, 0.5)

