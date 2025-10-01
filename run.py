import matplotlib.pyplot as plt
import numpy as np
from signals import *


f=1
s_t=0
e_t=10
a = 10
s_r=100

sine_wave = create_sine_signal(f, s_t, e_t, a, s_r)

print("First 10 samples of the sine wave:")
print(sine_wave[:10])

plt.plot(sine_wave[:10])
plt.ylabel("Amplitude")
plt.xlabel("time")
plt.show
plt.savefig("sineplot.png")