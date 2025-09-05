# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 20:15:06 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from scipy import signal

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000  # cantidad de muestras  
ts = 1/fs # tiempo de muestreo
df = fs/N # resolución espectral
A=np.sqrt(2) #amplitud normalizada
f0=(N/4)*df

    
# Grilla de sampleo temporal
tt = np.linspace(0, (N-1)*ts, N).flatten()

#Senoidal de amplitud normalizada
xx= A*np.sin(2*np.pi*tt*f0) 

# Grilla de sampleo frecuencial
ff = np.linspace(0, (N-1)*df, N).flatten()

#Ventana Implicita (Rectangular)
XX=fft(xx)/N

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad de Potencia (dB)')
plt.title('Ventaneo en dBs') 
plt.xlim(0, df*(N/2)) 
plt.plot(ff,10*np.log10(XX),label='Rectangular')
plt.legend()

#Ventana Blackman
WB= signal.windows.blackman(N) 
xWB=xx*WB
XWB=fft(xWB)/N

plt.plot(ff,10*np.log10(XWB),label='Blackman')
plt.legend()

#Ventana Blackman
WF= signal.windows.flattop(N) 
xWF=xx*WF
XWF=fft(xWF)/N

plt.plot(ff,10*np.log10(XWF),label='Flattop')
plt.legend()









