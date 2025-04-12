# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:36:49 2025

@author: Sofía
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Datos de la simulación

fs = 1000 # frecuencia de muestreo (Hz)
N = 1000 # cantidad de muestras
ts = 1/fs  # tiempo de muestreo
df =fs/N  # resolución espectral


R=200 # Numero de pruebas

#Generación de Señal

tt = np.linspace(0, (N-1)*ts, N).reshape((N,1)) # Vector columna de [N, 1]
vtt=np.tile(tt, (1,R)) #vector columna de [N, R]

f0=fs/4 #mitad de franja digital
fr=np.random.uniform(-1/2,1/2,size=(1,R)) #Vector flat de [1, R]
f1=f0+fr*df

aa= np.sqrt(2)
xk = aa*np.sin(2*np.pi*f1*vtt) 

#Generación del ruido
SNR=10
Pnk=10**(-SNR/10) #Potencia del Ruido
sigma=np.sqrt(Pnk)
nk=np.random.normal(0,sigma,(N,R))

#%% FFT
S=xk+nk #[N,R]

S_fft = np.fft.fft(S, axis=0) / N
ffx = np.linspace(0, (N-1)*df, N)
bfrec = ffx <= fs/2

# plt.figure()
# for i in range(R):
#     plt.plot(ffx[bfrec], 10 * np.log10(2 * np.abs(S_fft[bfrec, i]) ** 2))

# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Densidad de Potencia (dB)')
# plt.title('Espectro de la señal')
# plt.grid(True)
# plt.show()

#%% Ventana Flattop
wf=signal.windows.flattop(N).reshape((N,1)) #matriz [N,1]
xwf=S*wf

xwf_fft = np.fft.fft(xwf, axis=0) / N


# plt.figure()
# for i in range(R):
#     plt.plot(ffx[bfrec], 10 * np.log10(2 * np.abs(xwf_fft[bfrec, i]) ** 2))

# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Densidad de Potencia (dB)')
# plt.title('Espectro Ventaneado con Flattop')
# plt.grid(True)
# plt.show()

#%% Ventana Blackman Harris
wb=signal.windows.blackmanharris(N).reshape((N,1)) 
xwb=S*wb

xwb_fft = np.fft.fft(xwb, axis=0) / N


# plt.figure()
# for i in range(R):
#     plt.plot(ffx[bfrec], 10 * np.log10(2 * np.abs(xwb_fft[bfrec, i]) ** 2))

# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Densidad de Potencia (dB)')
# plt.title('Espectro Ventaneado con Blackman Harris')
# plt.grid(True)
# plt.show()

#%% Ventana Hann
wh=signal.windows.hann(N).reshape((N,1)) 
xwh=S*wh

xwh_fft = np.fft.fft(xwh, axis=0) / N

# plt.figure()
# for i in range(R):
#     plt.plot(ffx[bfrec], 10 * np.log10(2 * np.abs(xwh_fft[bfrec, i]) ** 2))

# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Densidad de Potencia (dB)')
# plt.title('Espectro Ventaneado con Hann')
# plt.grid(True)
# plt.show()

#%% Busco los a1 de cada ventana para la frec N/4

vs=np.abs(S_fft[250,:]) # Frec N/4 de la FFT
vf=np.abs(xwf_fft[250,:]) # Frec N/4 de la ventana Flattop
vb=np.abs(xwb_fft[250,:]) #Frec N/4 de la ventana Blackman Harris
vh=np.abs(xwh_fft[250,:]) #Frec N/4 de la ventana Hann

# plt.figure()
# plt.hist(vs, bins=10, color='orange', alpha=0.5, label='Box')
# plt.hist(vf, bins=10, color='purple', alpha=0.5, label='Ventana Flattop')
# plt.hist(vb, bins=10, color='pink', alpha=0.5, label='Ventana Blackman Harris')
# plt.hist(vh, bins=10, color='yellow', alpha=0.5, label='Ventana Hann')


# plt.title('Histograma')
# plt.xlabel('A1')
# plt.ylabel('Frecuencia')
# plt.legend()
# plt.show()

#%%Calculo de la Varianza y el Sesgo de a1
sesgo_a1_box=np.mean(vs-aa)
sesgo_a1_f=np.mean(vf-aa)
sesgo_a1_bh=np.mean(vb-aa)
sesgo_a1_h=np.mean(vh-aa)

varianza_a1_box=np.var(vs-aa)
varianza_a1_f=np.var(vf-aa)
varianza_a1_bh=np.var(vb-aa)
varianza_a1_h=np.var(vh-aa)

# i_box=np.mean(vs-sesgo_a1_box-aa)
# i_f=np.mean(vf-sesgo_a1_box-aa)
# i_bh=np.mean(vb-sesgo_a1_box-aa)
# i_h=np.mean(vh-sesgo_a1_box-aa)

#%% Estimador Ω1

arg_vs=np.argmax((1/N)*np.abs(S_fft[bfrec,:])**2,axis=0)
arg_vf=np.argmax((1/N)*np.abs(xwf_fft[bfrec,:])**2,axis=0)
arg_vb=np.argmax((1/N)*np.abs(xwb_fft[bfrec,:])**2,axis=0)
arg_vh=np.argmax((1/N)*np.abs(xwh_fft[bfrec,:])**2,axis=0)

omega_vs=arg_vs*df
omega_vf=arg_vf*df
omega_vb=arg_vb*df
omega_vh=arg_vh*df

plt.figure()
plt.hist(omega_vs, bins=10, color='yellow', alpha=0.5, label='Box')
plt.hist(omega_vf, bins=10, color='purple', alpha=0.5, label='Ventana Flattop')
plt.hist(omega_vb, bins=10, color='green', alpha=0.5, label='Ventana Blackman Harris')
plt.hist(omega_vh, bins=10, color='orange', alpha=0.5, label='Ventana Hann')

plt.title('Histograma')
plt.xlabel('Omega')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

#%%Calculo de la Varianza y el Sesgo de Ω1
sesgo_o1_box=np.mean(omega_vs-f1)
sesgo_o1_f=np.mean(omega_vf-f1)
sesgo_o1_bh=np.mean(omega_vb-f1)
sesgo_o1_h=np.mean(omega_vh-f1)

varianza_o1_box=np.var(omega_vs-f1)
varianza_o1_f=np.var(omega_vf-f1)
varianza_o1_bh=np.var(omega_vb-f1)
varianza_o1_h=np.var(omega_vh-f1)







