import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

fs = 1000
touchtones = np.genfromtxt("./touchtones.dat",dtype=None,delimiter=' ')
#touchtones_t, touchtones_m = np.hsplit(touchtones,2)
touchtones_m = touchtones[:,1]
t = touchtones[:,0]

touchtones_m = touchtones_m.astype(np.int16)

plt.figure(1)

wavfile.write("output.wav", fs, touchtones_m)

tplot = plt.plot(t, touchtones_m)
tplot = plt.xlabel("Time (s)")
tplot = plt.ylabel("Amplitude")
#plt.show()

def Dial_detector (touchtones_m):
    oldi = 0
    seperate_tones = []
    j = 0
    for i in range(len(touchtones_m)):
        if(touchtones_m[i] > 3300 or touchtones_m[i] < 3200):
            j = 0    
        if(touchtones_m[i] < 3300 and touchtones_m[i] > 3200):
            j += 1
            if j > 10:
                if i > oldi + 20:
                    seperate_tones.append(touchtones[oldi:(i-10)])
                oldi = i
                
    print(seperate_tones)
    for i in range(len(seperate_tones)):
        tplot = plt.plot(seperate_tones[i][:,0], seperate_tones[i][:,1],'r')
    tplot = plt.xlabel("Time (ms)")
    tplot = plt.ylabel("Amplitude")
    plt.show()



Dial_detector(touchtones_m)

#def Dial_Identifier():