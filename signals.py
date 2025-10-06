import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# Frequency f, start s_t, end e_t, amplitude a, sample rate s_r

def create_sine_signal(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(s_t, e_t, int(s_r * duration))
    v = a * np.sin(2 * np.pi * f * t)
    return t,v

def create_square_signal(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(s_t, e_t, int(s_r * duration))
    sine_wave = np.sin(2 * np.pi * f * t)
    v = a * np.sign(sine_wave)
    return t,v

def create_sawtooth_signal(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(s_t, duration, int(s_r * duration))
    v = a * signal.sawtooth(2 * np.pi * f * t)
    return t,v

def create_triangle_signal(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(s_t, e_t, int(s_r * duration))
    v = a * signal.sawtooth(2 * np.pi * f * t, 0.5)
    return t,v

def create_unit_step_signal(s_t, e_t, s_r, a,step_time):
    duration = e_t - s_t
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(s_t, e_t, int(s_r * duration))
    v = np.where(t >= step_time, a, 0)
    return t,v

