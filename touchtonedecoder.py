import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

fs = 1000
touchtones = np.genfromtxt("./touchtones.dat",dtype=None,delimiter=' ')
touchtones_t, touchtones_m = np.hsplit(touchtones,2)

touchtones_m = touchtones_m.astype(np.int16)

plt.figure(1)

wavfile.write("output.wav", fs, touchtones_m)

tplot = plt.plot(touchtones_t, touchtones_m)
tplot = plt.xlabel("Time (s)")
tplot = plt.ylabel("Amplitude")
plt.show()
def Dial_detector (touchtones_m):
    for i in range(len(touchtones_m)):
        if(touchtones_m[i] > 3300 or touchtones_m[i] < 3175):
            (touchtones_m[i])
        else:
            return 0

#def Dial_Identifier():