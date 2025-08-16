# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 19:11:47 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt


#Defino variables
vmax= 2  #Volts ; Energia=A^2/2
dc = 0  #Volts
ff = 10  #Hz
ph = 0 #Radianes
nn = 1000 # N
fs = 1000 #Hz
## 1/fs=Ts 

## A medida que aumento la frecuencia, disminuyo la cantidad de muestras por periodo
## En nyquist va a haber 2N/fs muestras, como N=fs, vamos a tener 2 muestras por periodo

#Defino la funcion
def mi_funcion_sen(vmax, dc, ff, ph, nn, fs):
    tt= np.linspace(0,(nn-1)*(1/fs),nn)
    xx = vmax* np.sin(2 * np.pi * ff * tt + ph) + dc
    return xx, tt

xx, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)


# Grafico la señal
plt.figure(1)
plt.plot(tt, xx)

## Grafico para f0=500 Hz (Nyquist)
ff=500

xx, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)

plt.figure(2)
plt.plot(tt, xx,':o')

## Como la fase es 0, los dos unicos puntos que deberia ver son los ceros del seno. Si cambio la fase, por ejemplo a pi/2, deberia ver los maximos 

## Grafico para f0=999 Hz
ff=999

xx, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)

plt.figure(3)
plt.plot(tt, xx)

## Grafico para f0=1001 Hz
ff=1001

xx, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)

plt.figure(4)
plt.plot(tt, xx)

## Grafico para f0=2001 Hz
ff=2001

xx, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)

plt.figure(5)
plt.plot(tt, xx)



