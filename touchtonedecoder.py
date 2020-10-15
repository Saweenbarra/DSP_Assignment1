import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import math

fs = 1000
touchtones = np.genfromtxt("touchtones.dat",dtype=None,delimiter=' ')
touchtones[:,1] = touchtones[:,1].astype(np.int16)

wavfile.write("touchtones.wav", fs, touchtones[:,1])

oldi = 0
seperate_tones = []
j = 0
fd_freqs = [[303, 230, 148, 59, 209, 336, 477],[1,2,3,4,5,6,7]] #fold down frequancies corresponding to tone frequancies

def Tone_ID(touchtone):
    f_touchtone = np.fft.fft(touchtone)
    f = np.linspace(0, fs, len(f_touchtone))
    k1 = int(len(f_touchtone)/fs*500)
    
    f_touchtonedB = 20*np.log10(abs(f_touchtone)*2/len(f_touchtone)/(pow(2,15)-1))
    peaks = np.where(f_touchtonedB[1:k1] > np.max(f_touchtonedB[1:k1]) - 5)
    peaks = list(peaks[0])

    peaks = np.delete(peaks, np.argwhere(np.ediff1d(peaks) <= 1) + 1) #remove consecutive peaks which are within 1 of each other

    for i in range(len(peaks)):
        peaks[i] = peaks[i]*fs/len(f_touchtone)
        for j in range(len(fd_freqs[0])):  
            if math.isclose(peaks[i],fd_freqs[0][j],rel_tol = 0.05,abs_tol=10):
                print(fd_freqs[0][j],fd_freqs[1][j])

    print(peaks)

    plt.figure(2)
    fplot = plt.plot(f, f_touchtonedB)
    fplot = plt.xlabel("Frequency (Hz)")
    fplot = plt.ylabel("FS")
    plt.xlim(right = fs/2,left = 1)
    

for i in range(len(touchtones[:,1])):
    if(touchtones[:,1][i] > 3300 or touchtones[:,1][i] < 3200):
        j = 0    
    if(touchtones[:,1][i] < 3300 and touchtones[:,1][i] > 3200):
        j += 1
        if j > 10:
            if i > oldi + 20:
                seperate_tones.append(touchtones[oldi:(i-10)])
                Tone_ID(touchtones[oldi:(i-10)][:,1])
            oldi = i

#Tone_ID(seperate_tones[0][:,1])
plt.figure(1)
tplot = plt.plot(touchtones[:,0], touchtones[:,1])
for i in range(len(seperate_tones)):
    tplot = plt.plot(seperate_tones[i][:,0], seperate_tones[i][:,1],'r')
tplot = plt.xlabel("Time (ms)")
tplot = plt.ylabel("Amplitude")
#plt.show()
