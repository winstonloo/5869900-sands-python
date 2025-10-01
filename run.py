import matplotlib.pyplot as plt
import numpy as np
from signals import *
from operations import *

f=1
s_t=0
e_t=10
a = 1
s_r=100

wave = create_triangle_signal(f, s_t, e_t, a, s_r)

time_shifted_wave = time_shift(wave, 2, s_r)

time_scaled_wave = time_scale(wave, 2)

amplitude_scaled_wave = amplitude_scale(wave, 2)

added_wave = add_signals(wave, time_shifted_wave)

multiplied_wave = multiply_signals(wave, time_shifted_wave)

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
ax1.plot(wave)
ax2.plot(time_scaled_wave)

plt.show()

