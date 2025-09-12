# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 17:21:58 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000  # cantidad de muestras  
ts = 1/fs # tiempo de muestreo (s)
df = fs/N # resolución espectral (Hz)
A=np.sqrt(2) #amplitud normalizada (V)
k0=N/4
k1=(N/4)+0.25
k2=(N/4)+0.5

#%% Genero las señales

tt = np.linspace(0, (N-1)*ts, N).flatten()
xx= A*np.sin(2*np.pi*tt*k0*df) 

x1=A*np.sin(2*np.pi*tt*k1*df) 

x2=A*np.sin(2*np.pi*tt*k2*df) 

#Verifico que la potencia de la señal este normalizada
var=np.var(xx)
print(f'Potencia de la Señal con k0=N/4: {var:3.1f}')
var1=np.var(x1)
print(f'Potencia de la Señal con k0=N/4 + 0.25: {var1:3.1f}')
var2=np.var(x2)
print(f'Potencia de la Señal con k0=N/4 + 0.5: {var2:3.1f}')

# Calculo la DEP
XX=fft(xx)
DP=(np.abs(XX))**2

X1=fft(x1)
DP1=(np.abs(X1))**2

X2=fft(x2)
DP2=(np.abs(X2))**2

#Grafico la DEP en dBs
ff = np.linspace(0, (N-1)*df, N).flatten()

# plt.title('DEP en dBs')  
# plt.subplot(3,1,1)
# plt.plot(ff,10*np.log10(DP),'x',label='|X|^2 en dB')
# plt.legend()
# plt.xlim((0, N/2)) 
# plt.subplot(3,1,2)
# plt.plot(ff,10*np.log10(DP1),'x',label='|X1|^2 en dB')
# plt.legend()
# plt.xlim((0, N/2)) 
# plt.subplot(3,1,3)
# plt.plot(ff,10*np.log10(DP2),'x',label='|X2|^2 en dB')
# plt.legend()
# plt.xlim((0, N/2)) 

#%% Verifico Parseval
P=(1/N)*np.sum(DP)
P1=(1/N)*np.sum(DP1)
P2=(1/N)*np.sum(DP2)

print(f'Potencia Unitaria de XX: {P:3.1f}')
print(f'Potencia Unitaria de X1: {P1:3.1f}')
print(f'Potencia Unitaria de X2: {P2:3.1f}')

#%% Zero Padding
M=10*N

padding=np.zeros(M) 
padding[:N]=xx

padding1=np.zeros(M) 
padding1[:N]=x1

padding2=np.zeros(M) 
padding2[:N]=x2


XX=fft(padding)
DP=(np.abs(XX))**2

X1=fft(padding1)
DP1=(np.abs(X1))**2

X2=fft(padding2)
DP2=(np.abs(X2))**2


df_p=fs/M
ff_p = np.linspace(0,(M-1)*df_p, M).flatten()

plt.title('DEP en dBs con Padding')  
plt.subplot(3,1,1)
plt.plot(ff_p,10*np.log10(DP),'x',label='|X|^2 en dB')
plt.legend()
plt.xlim((0, N/2)) 
plt.subplot(3,1,2)
plt.plot(ff_p,10*np.log10(DP1),'x',label='|X1|^2 en dB')
plt.legend()
plt.xlim((0, N/2)) 
plt.subplot(3,1,3)
plt.plot(ff_p,10*np.log10(DP2),'x',label='|X2|^2 en dB')
plt.legend()
plt.xlim((0, N/2)) 















