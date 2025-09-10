# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 19:28:38 2025

@author: Sofía
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parametros de la simulacion
vmax= 1  #Volts 
dc = 0  #Volts
ff = 2000  #Hz
ph = 0 #Radianes
N = 1000 # N
fs = 200000 #Hz
Ts=1/fs #seg
df=fs/N 

#EJERCICIO 1
#%% Para x[n]=xx

tt = np.linspace(0, (N-1)*Ts, N).flatten()  
xx = vmax * np.sin(2 * np.pi * ff * tt + ph) + dc 

# Ecuación en diferencias
y=np.zeros(N) #vector salida hecho en ceros

def ecuacion_dif(x):
    for n in range(N):                      
        
        y[n] = 0.03 * x[n]
        
        if n >= 1:                          
            y[n] += 0.05 * x[n-1]
        
        if n >= 2:                          
            y[n] += 0.03 * x[n-2]
            
        if n >= 1:                         
            y[n] += 1.5 * y[n-1]
            
        if n >= 2:                          
            y[n] += -0.5 * y[n-2]
    
    return y

yy=ecuacion_dif(xx)


# plt.plot(tt, yy)
# plt.title('Grafico de y[n] para x[n]=xx')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Para x[n]=x1
vmax= 2
ph=np.pi/2

x1 = vmax * np.sin(2 * np.pi * ff * tt + ph) + dc 

y1=ecuacion_dif(x1)

# plt.figure()
# plt.plot(tt, yy)
# plt.title('Grafico de y[n] para x[n]=x1')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Para x[n]=x2
vmax= 1
ph=0

x2= (vmax * np.sin(2 * np.pi * ff * tt + ph) + dc)*(2*np.sin(2 * np.pi * 1000 * tt + ph) + dc)

y2=ecuacion_dif(x2)

# plt.figure()
# plt.plot(tt, yy)
# plt.title('Grafico de y[n] para x[n]=x2')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Para x[n]=x3
threshold=(vmax**2/2)*0.75

x3= np.clip(xx, -threshold, threshold)

y3=ecuacion_dif(x3)

# plt.figure()
# plt.plot(tt, yy)
# plt.title('Grafico de y[n] para x[n]=x3')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Para x[n]=x4
ff = 4000  #Hz

x4=signal.square(2*np.pi*tt*ff)

y4=ecuacion_dif(x4)

# plt.figure()
# plt.plot(tt, yy)
# plt.title('Grafico de y[n] para x[n]=x4')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Para x[n]=x5

x5=np.zeros_like(tt)
x5[:200]=1 #10^(-3)*fs es 200

y5=ecuacion_dif(x5)

# plt.figure()
# plt.plot(tt, yy)
# plt.title('Grafico de y[n] para x[n]=x5')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Respuesta al Impulso
# Reemplazo x[n] por δ[n] y y[n] por h[n]

# Genero δ[n]
delta=np.zeros(N)
delta[0]=1

h=np.zeros(N)

def resp_impulso(delta):
    for n in range(N):                      
        
        h[n] = 0.03 * delta[n]
        
        if n >= 1:                          
            h[n] += 0.05 * delta[n-1]
        
        if n >= 2:                          
            h[n] += 0.03 * delta[n-2]
            
        if n >= 1:                         
            h[n] += 1.5 * h[n-1]
            
        if n >= 2:                          
            h[n] += -0.5 * h[n-2]
    
    return h

h=resp_impulso(delta)

# plt.figure()
# plt.plot(tt, h)
# plt.title('Respuesta al Impulso')
# plt.xlabel('N', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%% Respuesta al Impulso para x[n]=xx

yy_conv=np.convolve(xx,h,mode='full')
yy_conv = yy_conv[:N]


# plt.figure()
# plt.plot(tt, yy_conv)
# plt.title('Respuesta al Impulso con x[n]=xx')
# plt.xlabel('N', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#%%EJERCICIO 2
#Calculo de y[n]
for n in range(N):
    yy[n] = xx[n]

    if n >= 10:
        yy[n] += 3 * xx[n-10]
        
# plt.plot(tt, yy)
# plt.title('Grafico de y[n] = x[n] + 3·x[n-10]')
# plt.xlabel('Tiempo (ms)', fontsize=12)
# plt.ylabel('Amplitud (V)', fontsize=12)
# plt.legend()

#Calculo de δ[n] 

for n in range(N):
    # h[n] = δ[n] + 3·δ[n-10]
    h[n] = delta[n]  # Término δ[n]
    
    if n >= 10:  # Término 3·δ[n-10]
        h[n] += 3 * delta[n-10]

plt.figure()
plt.plot(tt, h)
plt.title('Respuesta al Impulso')
plt.xlabel('N', fontsize=12)
plt.ylabel('Amplitud (V)', fontsize=12)
plt.legend()


