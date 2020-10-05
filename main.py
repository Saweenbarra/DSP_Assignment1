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

#Calculate discreet fourier transform of data
dataf = np.fft.fft(data)
#Create frequency axis
f = np.linspace(0, fs, len(dataf))

#Plot sample in frequency domain log(x-axis) and log(y-axis)
plt.figure(2)
fplot = plt.plot(f, abs(dataf))
fplot = plt.xlabel("Frequency (Hz)")
fplot = plt.ylabel("Magnitude")
plt.xscale("log")
plt.yscale("log")

#Find sample numbers corresponding to 6kHz and 10kHz
k1 = int(len(dataf)/44100*6000)
k2 = int(len(dataf)/44100*10000)

#Amplify selected frequencies by factor
dataf[k1:k2+1] *= 1.00001

#Plot new amplified FFT
plt.figure(3)
bfplot = plt.plot(f, abs(dataf))
bfplot = plt.xlabel("Frequency (Hz)")
bfplot = plt.ylabel("Magnitude")
plt.xscale("log")
plt.yscale("log")

#Convert boosted signal to time domain
dataBoost = np.fft.ifft(dataf)
dataBoost = np.real(dataBoost)

#Plot boosted signal in time domain
plt.figure(4)
btplot = plt.plot(t, dataBoost)
btplot = plt.xlabel("Time (s)")
btplot = plt.ylabel("Amplitude")

#Write boosted signal to wav file
wavfile.write("PotatoesBoost.wav", fs, dataBoost)
plt.show()