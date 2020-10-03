import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

#Load wav file sample frequency and data
fs, data = wavfile.read("Potatoes.wav")

#Calculate duration of sample and create time (x-axis) array
duration = len(data)/fs
t = np.linspace(0, duration, len(data))

#Plot sample in time domain
plt.figure(1)
tplot = plt.plot(t, data)
tplot = plt.xlabel("Time (s)")
tplot = plt.ylabel("Amplitude")

#Plot sample in frequency domain log(x-axis) and log(y-axis)
dataf = np.fft.fft(data)
f = np.linspace(0, fs, len(dataf))
plt.figure(2)
fplot = plt.plot(f, abs(dataf))
fplot = plt.xlabel("Frequency (Hz)")
fplot = plt.ylabel("Magnitude")
plt.xscale("log")
plt.yscale("log")
plt.show()