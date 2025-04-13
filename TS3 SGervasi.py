# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 15:35:49 2025

@author: Sofía
"""

# módulos y funciones a importar
import matplotlib.pyplot as plt
import numpy as np

## Parte A

# Datos de la simulación

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000 # cantidad de muestras
f0 = 1 # Hz
ts = 1/fs  # tiempo de muestreo
df =fs/N  # resolución espectral

#%% Datos del ADC
B = 4 # bits
Vf = 2 # rango simétrico de +/- Vf Volts
q =  Vf/2**(B-1)# paso de cuantización de q Volts

# Datos del ruido 
Pnq = q**2/12# Potencia ruido cuántico [Watts]
kn = 1 # escala de la potencia de ruido analógico
Pna = Pnq * kn # Potencia ruido analógico [Watts] 


#%% Grilla de sampleo temporal

tt = np.linspace(0, (N-1)*ts, N) #tiempo de la experiencia

arg = 2*np.pi*f0*tt

xx = np.sqrt(2)*np.sin(arg) #Señal de energía normalizada
varianza = np.var(xx) #escalar por el desvio estandar

s = xx/np.sqrt(varianza) # señal analógica normalizada sin ruido
nn = np.random.normal(0, np.sqrt(Pna), N) # señal de ruido de analógico
sr = s + nn  # señal analógica de entrada al ADC (con ruido analógico)
srq = np.round(sr/q)*q # señal cuantizada

nq = srq - sr # señal de ruido de cuantización

#%%Señal temporal

plt.figure(1)

plt.plot(tt, srq, lw=1, color='green', marker='o', ls='dotted', label=' Señal Cuantizada (ADC OUT)')
plt.plot(tt, sr, lw=1, color='blue', marker='', ls='dotted', label='Señal Analógica con Ruido Analógico (ADC IN)')
plt.plot(tt, s, lw=2, color='orange', marker='', ls='solid', label='Señal Analógica')

plt.title('Señal muestreada por un ADC de {:d} bits, q={:3.3f}V, Kn={:d} '.format(B, q, kn))
plt.xlabel('tiempo [segundos]')
plt.ylabel('Amplitud [V]')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()

#%%Espectro

plt.figure(2)
ft_SR = 1/N*np.fft.fft( sr) #Vector de N muestras, num. complejos
ft_Srq = 1/N*np.fft.fft( srq)
ft_As = 1/N*np.fft.fft( s)
ft_Nq = 1/N*np.fft.fft( nq)
ft_Nn = 1/N*np.fft.fft( nn)

# Grilla de sampleo frecuencial
ff = np.linspace(0, (N-1)*df, N)

bfrec = ff <= fs/2

Nnq_mean = np.mean(np.abs(ft_Nq)**2)
nNn_mean = np.mean(np.abs(ft_Nn)**2)


plt.plot( ff[bfrec], 10* np.log10(2*np.abs(ft_As[bfrec])**2), color='orange', ls='dotted', label='s' )
plt.plot( ff[bfrec], 10* np.log10(2*np.abs(ft_SR[bfrec])**2), ':g', label='$ s_R $' )
plt.plot( ff[bfrec], 10* np.log10(2*np.abs(ft_Srq[bfrec])**2), lw=2, label='$ s_{RQ}$' )
plt.plot( np.array([ ff[bfrec][0], ff[bfrec][-1] ]), 10* np.log10(2* np.array([nNn_mean, nNn_mean]) ), '--r', label= '$ \overline{n} = $' + '{:3.1f} dB'.format(10* np.log10(2* nNn_mean)) )
plt.plot( np.array([ ff[bfrec][0], ff[bfrec][-1] ]), 10* np.log10(2* np.array([Nnq_mean, Nnq_mean]) ), '--c', label='$ \overline{n_Q} = $' + '{:3.1f} dB'.format(10* np.log10(2* Nnq_mean)) )
plt.plot( ff[bfrec], 10* np.log10(2*np.abs(ft_Nn[bfrec])**2), ':r')
plt.plot( ff[bfrec], 10* np.log10(2*np.abs(ft_Nq[bfrec])**2), ':c')



plt.title('Señal muestreada por un ADC de {:d} bits, q={:3.3f}V, Kn={:d} '.format(B, q, kn))
plt.ylabel('Densidad de Potencia [dB]')
plt.xlabel('Frecuencia [Hz]')
plt.ylim([-90, 5])
axes_hdl = plt.gca()
axes_hdl.legend()

#%% Histograma


plt.figure(3)
bins = 10
plt.hist(nq.flatten()/(q), bins=bins)
plt.plot( np.array([-1/2, -1/2, 1/2, 1/2]), np.array([0, N/bins, N/bins, 0]), '--r')
plt.title( 'Ruido de cuantización para {:d} bits, q={:3.3f}V, Kn={:d} '.format(B, q, kn))

plt.xlabel('Pasos de cuantización (q) [V]')

