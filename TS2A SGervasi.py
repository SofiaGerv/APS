# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 18:50:23 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig

## Filtro A
#Propongo
Q = 1
w0 = 1 #rad/s

# Ingreso la funcion transferencia H(s) como vectores 

num = np.array([ w0 / Q, 0 ])
den = np.array([ 1., w0 / Q, w0**2 ])

# Creo la función de transferencia
H = sig.TransferFunction(num, den)

# Especifico las frecuencias a evaluar
frec = np.logspace(-2, 2, 200)  # Frecuencias en rad/s

# Respuesta de módulo y fase
w, mag, fase = sig.bode(H, frec)

# Convierto la fase de grados a radianes
faser = np.deg2rad(fase)

#Busco polos y ceros
ceros, polos, _= sig.tf2zpk(num, den)

# Gráfico de la respuesta de módulo (en dB)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title("Respuesta de Módulo")
plt.xlabel("Frecuencia [rad/s]")
plt.ylabel("Módulo [dB]")
plt.grid(True)

# Gráfico de la respuesta en fase (en grados)
plt.subplot(2, 1, 2)
plt.semilogx(w, faser)
plt.title("Respuesta en Fase")
plt.xlabel("Frecuencia [rad/s]")
plt.ylabel("Fase [rad]")
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ['$-\\pi$', '$-\\pi/2$', '$0$', '$\\pi/2$', '$\\pi$']) 
plt.grid(True)


plt.tight_layout()
plt.show()

# Graficar los ceros y los polos

plt.figure(figsize=(8, 8))
ax = plt.gca()

plt.plot(ceros.real, ceros.imag, 'o', markersize=8, label='Ceros')
plt.plot(polos.real, polos.imag, 'x', markersize=8, label='Polos')

# Dibujar el círculo unitario 
unit_circle = plt.Circle((0, 0), radius=1, fill=False, color='gray', linestyle='--')
ax.add_artist(unit_circle)

# Configurar los ejes
plt.axvline(0, color='black', linewidth=0.5)  # Eje imaginario
plt.axhline(0, color='black', linewidth=0.5)  # Eje real

# Establecer límites para los ejes (ajustar según la ubicación de polos y ceros)
max_val = max(np.max(np.abs(polos)), np.max(np.abs(ceros)), 1.5) 
plt.xlim([-max_val, max_val])
plt.ylim([-max_val, max_val])

# Añadir etiquetas y título
plt.xlabel(r'$\theta$')
plt.ylabel("jw")
plt.title('Diagrama de Polos y Ceros')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box') # Asegurar que el círculo unitario sea circular
plt.show()