import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt


fs, data = wavfile.read("Potatoes.wav")

duration = len(data)/fs
t = np.linspace(0, duration, len(data))

plt.figure()
plt.plot(t, data)
plt.show()