import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

fs = 1000
touchtones = np.genfromtxt("./touchtones.dat",dtype=None,delimiter=' ')
touchtones[:,1] = touchtones[:,1].astype(np.int16)

wavfile.write("touchtones.wav", fs, touchtones[:,1])

oldi = 0
seperate_tones = []
j = 0

def Tone_ID(touchtone):
    f_touchtone = np.fft.fft(touchtone)
    f = np.linspace(0, fs, len(f_touchtone))
    f_touchtonedB = 20*np.log10(abs(f_touchtone)*2/len(f_touchtone)/(pow(2,15)-1))

    plt.figure(2)
    fplot = plt.plot(f, f_touchtonedB)
    fplot = plt.xlabel("Frequency (Hz)")
    fplot = plt.ylabel("FS")
    plt.xscale("log")
    plt.xlim(right = fs/2)
    plt.xlim(left = 10)
    

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


plt.figure(1)
print(len(seperate_tones))
#tplot = plt.plot(touchtones[:,0], touchtones[:,1])
for i in range(1):
    tplot = plt.plot(seperate_tones[i][:,0], seperate_tones[i][:,1],'r')
tplot = plt.xlabel("Time (ms)")
tplot = plt.ylabel("Amplitude")
plt.show()
