import matplotlib.pyplot as plt
import numpy as np
from signals import *
from operations import *

f=1
s_t=0
e_t=10
a = 1
s_r=100

wave = create_sine_signal(f, s_t, e_t, a, s_r)

time_shifted_wave = time_shift(wave, 2, s_r)
time_scaled_wave = time_scale(wave, 2)
amplitude_scaled_wave = amplitude_scale(wave, 2)
added_wave = add_signals(wave, time_shifted_wave)
multiplied_wave = multiply_signals(wave, time_shifted_wave)

plt.plot(time_shifted_wave)
plt.ylabel("Amplitude")
plt.xlabel("time")
plt.show()
plt.savefig("sineplot.png")
