# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 18:57:37 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#Defino variables
vmax= 1  #Volts 
dc = 0  #Volts
ff = 2000  #Hz
ph = 0 #Radianes
nn = 1000 # N
fs = 200000 #Hz
Ts=1/fs


#Defino la funcion
def mi_funcion_sen(vmax, dc, ff, ph, nn, fs):
    tt= np.linspace(0,(nn-1)*Ts,nn).flatten()
    xx = vmax* np.sin(2 * np.pi * ff * tt + ph) + dc
    return xx, tt

xx, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)

# #%% Sintetizar y graficar una señal sinusoidal de 2KHz

# plt.figure()
# plt.plot(tt, xx, color='black')

# #%% Sintetizar y graficar una señal sinusoidal de 2KHz, amplificada y desfasada en pi/2
# vmax= 2
# ph=np.pi/2

# x1, tt = mi_funcion_sen(vmax, dc, ff, ph, nn, fs)

# plt.figure()
# plt.plot(tt, x1, color='black')

# #%% Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia
# fm=1000 #Frecuencia de la señal moduladora
# mm=2*np.sin(2 * np.pi * fm * tt + ph) #señal moduladora

# x2=xx*mm

# plt.figure()
# plt.subplot(211)
# plt.plot(tt, xx, color='tab:red', linestyle='--')
# plt.plot(tt, mm, color='tab:orange', linestyle='--')
# plt.subplot(212)
# plt.plot(tt, x2, color='black')

# #%%  75% de la potencia
# E=vmax**2/2 #energía
# threshold=E*0.75

# xx_clipped = np.clip(xx, -threshold, threshold)

# plt.figure()
# plt.plot(tt, xx, color='tab:gray',linestyle='--')
# plt.plot(tt, xx_clipped, color='black')

# #%% Sintetizar y graficar una señal cuadrada de 4KHz
# ff = 4000  #Hz

# x3=signal.square(2*np.pi*tt*ff)

# plt.figure()
# plt.plot(tt, x3, color='black')



# # %% Pulso rectangular de 10ms
# x4=np.zeros_like(tt)
# x4[500:511]=1

# plt.figure()
# plt.plot(x4)

# #%% Verificar ortogonalidad entre la primera señal y las demás
# o=np.inner(xx,xx)
# o1=np.inner(xx,x1)
# o3=np.inner(xx,xx_clipped)
# o2=np.inner(xx,x3)
# o4=np.inner(xx,x4)

# #%% Verificar autocorrelacion entre la primera señal y las demás
# Rxx=signal.correlate(xx,xx)
# Rxx1=signal.correlate(xx,x1)
# Rxx2=signal.correlate(xx,x2)
# Rxxc=signal.correlate(xx,xx_clipped)
# Rxx3=signal.correlate(xx,x3)
# Rxx4=signal.correlate(xx,x4)


# plt.plot()
# plt.subplot(611)
# plt.plot(Rxx,color='black',label='Rxx')
# plt.legend()


# plt.subplot(612)
# plt.plot(Rxx1,color='black',label='Rxx1')
# plt.legend()


# plt.subplot(613)
# plt.plot(Rxx2,color='black',label='Rxx2')
# plt.legend()


# plt.subplot(614)
# plt.plot(Rxxc,color='black',label='Rxxc')
# plt.legend()


# plt.subplot(615)
# plt.plot(Rxx3,color='black',label='Rxx3')
# plt.legend()


# plt.subplot(616)
# plt.plot(Rxx4,color='black',label='Rxx4')
# plt.legend()

#%%
zz=2*np.sin(10000*tt)*np.sin(5000*tt)
yy=np.cos(10000*tt-5000*tt)-np.cos(10000*tt+5000*tt)

plt.figure()
plt.title('Comparación de la señales con  α= ω1⋅t, β= ω2⋅t, ω1=10000 y ω2=5000')
plt.subplot(211)
plt.plot(tt, zz, color='tab:olive',label='2⋅sin(α)⋅sin(β)')
plt.legend()
plt.subplot(212)
plt.plot(tt, yy, color='tab:blue', label='cos(α−β)−cos(α+β)')
plt.legend()




