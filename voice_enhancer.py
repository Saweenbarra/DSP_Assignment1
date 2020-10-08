import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

#Load wav file sample frequency and data
fs, data = wavfile.read("original.wav")

#Calculate duration of sample and create time (x-axis) array
duration = len(data)/fs
t = np.linspace(0, duration, len(data))

normaliser = (pow(2,16)-1)

#Plot sample in time domain
plt.figure(1)
tplot = plt.plot(t, data/normaliser)
tplot = plt.xlabel("Time (s)")
tplot = plt.ylabel("Amplitude")

#Calculate discreet fourier transform of data
dataf = np.fft.fft(data)
#Create frequency axis
f = np.linspace(0, fs, len(dataf))

#Plot sample in frequency domain log(x-axis) and log(y-axis)
plt.figure(2)
fplot = plt.plot(f, abs(dataf)/len(dataf))
fplot = plt.xlabel("Frequency (Hz)")
fplot = plt.ylabel("Magnitude")
plt.xscale("log")
plt.yscale("log")

#Find sample numbers corresponding to 6kHz and 10kHz
k1 = int(len(dataf)/fs*6000)
k2 = int(len(dataf)/fs*10000)

#Amplify selected frequencies by factor
dataf[k1:k2+1] *= 20

#Find sample numbers corresponding to 85Hz and 180Hz
k1 = int(len(dataf)/fs*85)
k2 = int(len(dataf)/fs*180)

#Amplify selected frequencies by factor
dataf[k1:k2+1] *= 5

#Plot new amplified FFT
plt.figure(3)
bfplot = plt.plot(f, abs(dataf)/len(dataf))
bfplot = plt.xlabel("Frequency (Hz)")
bfplot = plt.ylabel("Magnitude")
plt.xscale("log")
plt.yscale("log")

#Convert boosted signal to time domain
dataBoost = np.fft.ifft(dataf)
dataBoost = np.real(dataBoost)

#Cast 64bit floats to int to be written to wav file
dataBoost = dataBoost.astype(np.int16)

#Plot boosted signal in time domain
plt.figure(4)
btplot = plt.plot(t, dataBoost/normaliser)
btplot = plt.xlabel("Time (s)")
btplot = plt.ylabel("Amplitude")

#Write boosted signal to wav file
wavfile.write("improved.wav", fs, dataBoost)
plt.show()