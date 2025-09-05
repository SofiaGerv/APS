# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 20:36:35 2025

@author: Sofía
"""
import numpy as np
import matplotlib.pyplot as plt

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000   # cantidad de muestras
    
ts = 1/fs # tiempo de muestreo
df = fs/N # resolución espectral
    
# grilla de sampleo temporal
tt = np.linspace(0, (N-1)*ts, N).flatten()

# array donde voy a guardar mi DFT, inicializado en 0
x=np.zeros(N,dtype=np.complex128) 


xx= np.sin(2*np.pi*tt)

for k in range(N): #rango va de 0 a N-1   
    for n in range(N):
        x[k]+=xx[n]*np.exp(-1j*k*n*2*np.pi*(1/N))
        
# grilla de sampleo frecuencial
ff = np.linspace(0, (N-1)*df, N).flatten()

modulo=np.abs(x)
fase=np.angle(x)

#Graficos
plt.figure()
plt.plot(ff, modulo)

