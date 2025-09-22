import numpy as np
from signals import create_sine_wave

frequency = 5
duration = 2

sine_wave = create_sine_wave(frequency, duration)

print("First 10 samples of the sine wave:")
print(sine_wave[:10])