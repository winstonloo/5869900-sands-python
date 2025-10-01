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

plt.plot(wave)
plt.ylabel("Amplitude")
plt.xlabel("time")
plt.show()
plt.savefig("sineplot.png")

