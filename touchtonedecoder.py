import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

fs = 1000
touchtones = np.genfromtxt("./touchtones.dat",dtype=None,delimiter=' ')
#touchtones_t, touchtones_m = np.hsplit(touchtones,2)
touchtones_m = touchtones[:,1]
duration = len(touchtones_m)/fs
t = np.linspace(0, duration, len(touchtones_m))

touchtones_m = touchtones_m.astype(np.int16)

plt.figure(1)

wavfile.write("output.wav", fs, touchtones_m)

tplot = plt.plot(t, touchtones_m)
tplot = plt.xlabel("Time (s)")
tplot = plt.ylabel("Amplitude")
plt.show()

def Dial_detector (touchtones_m):
    oldi = 0
    seperate_tones = np.zeros([1,2])
    for i in range(len(touchtones_m)):
        if(touchtones_m[i] < 3250 and touchtones_m[i] > 3200):
            if i > (oldi + 1):
                touchtone = touchtones[oldi:i]
                seperate_tones = np.append(seperate_tones,touchtone,axis=0)
            oldi = i
    print(seperate_tones)



Dial_detector(touchtones_m)

#def Dial_Identifier():