# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 21:36:54 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000  # cantidad de muestras  
ts = 1/fs # tiempo de muestreo
df = fs/N # resolución espectral
A=np.sqrt(2) #amplitud normalizada
f0=(N/4)*df

    
# grilla de sampleo temporal
tt = np.linspace(0, (N-1)*ts, N).flatten()

#Senoidal de amplitud normalizada
xx= A*np.sin(2*np.pi*tt*f0) 

#Calculo var, media y desvio estandar
var=np.var(xx)
media=np.mean(xx)
desv=np.std(xx)

# |x|^2
XX=fft(xx)
absXX=np.abs(XX)

DP=absXX**2 #Densidad Espectral de Potencia

# grilla de sampleo frecuencial
ff = np.linspace(0, (N-1)*df, N).flatten()


# #Grafico la DEP en dBs
plt.figure()
plt.title('DEP en dBs')  
plt.plot(ff,10*np.log10(DP),'x',label='|X|^2 en dB')
plt.xlim(0, N/2) 
plt.legend()

#toda la potencia esta concentrado en las dos deltas

#Verifico Parseval
P=(1/N)*np.sum(DP)
p=np.sum(np.abs(xx)**2)

print(p)
print(P)

##Zero Padding
padding=np.zeros(10*N) 
padding[:N]=xx

# |x|^2
XX_P=fft(padding)
absXX_P=np.abs(XX_P)

DP_P=absXX_P**2 #Densidad Espectral de Potencia

# grilla de sampleo frecuencial
M=10*N
df_p=fs/M
ff_p = np.linspace(0,(M-1)*df_p, M).flatten()


#Grafico la DEP en dBs
plt.figure()
plt.title('DEP en dBs con padding')  
plt.plot(ff_p,10*np.log10(DP_P),'x',label='|X|^2 en dB')
plt.xlim(0, N/2) 
plt.legend()















