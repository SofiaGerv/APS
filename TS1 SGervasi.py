# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 20:43:20 2025

@author: Sofía
"""

#Trabajo Semanal 1

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pdsmodulos as pds

#Defino variables
A= 1  #Volts
Vm = 0  #Volts
f0 = 1.0  #Hz
fase = 0 #Radianes
N = 1000
fs = 300 #Hz

#Defino la funcion
def mi_funcion_sen(A, Vm, f0, fase, N, fs):
    tt= np.linspace(0,(N-1)*(1/fs),N)
    xx = A* np.sin(2 * np.pi * f0 * tt + fase) + Vm
    return xx, tt

xx, tt = mi_funcion_sen(A, Vm, f0, fase, N, fs)

# Grafico la señal
plt.plot(tt, xx)