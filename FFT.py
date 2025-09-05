# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 21:00:44 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000  # cantidad de muestras  
ts = 1/fs # tiempo de muestreo
df = fs/N # resolución espectral
    
# grilla de sampleo temporal
tt = np.linspace(0, (N-1)*ts, N).flatten()

# grilla de sampleo frecuencial
ff = np.linspace(0, (N-1)*df, N).flatten()

xx= np.sin(2*np.pi*tt*(N/4)*df) #Señal con frec 250Hz
x1= np.sin(2*np.pi*tt*((N/4)+0.5)*df) #Señal con frec 250.5Hz
x2= np.sin(2*np.pi*tt*((N/4)+1)*df) #Señal con frec 251Hz

#Aplico FFT
XX=fft(xx)
X1=fft(x1)
X2=fft(x2)

#Graficos
    
# plt.figure()    
# plt.title('FFT')  
# plt.plot(ff,np.abs(XX),'*',label='|XX|')
# plt.legend()


# plt.plot(ff,np.abs(X1),'*',label='|X1|')
# plt.legend()


# plt.plot(ff,np.abs(X2),'*',label='|X2|')
# plt.legend()

# plt.xlabel('Frecuencia [Hz]')
# plt.ylabel('|X[k]|')
# plt.xlim([0,N/2])

#Graficos en dBs
plt.figure()
plt.title('FFT en dBs')  
plt.plot(ff,20*np.log10(np.abs(XX)),'x',label='|XX| en dB')
plt.legend()

plt.plot(ff,20*np.log10(np.abs(X1)),'o',label='|X1| en dB')
plt.legend()

plt.plot(ff,20*np.log10(np.abs(X2)),'*',label='|X2| en dB')
plt.legend()

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|X[k]|')
plt.xlim([0,fs/2])
