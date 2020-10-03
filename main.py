import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

#Load wav file sample frequency and data
fs, data = wavfile.read("Potatoes.wav")

#Calculate duration of sample and create time (x-axis) array
duration = len(data)/fs
t = np.linspace(0, duration, len(data))

#Plot sample in time domain
plt.figure()
plt.plot(t, data)
plt.show()