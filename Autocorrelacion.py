# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 20:30:10 2025

@author: Sofía
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#%% Autocorrelacion
M=8
x=np.zeros(M)
x[0:3]=1

print(x)

# plt.figure()
# Rxx=signal.correlate(x,x)
# plt.stem(Rxx)

# plt.plot(Rxx,linestyle='--')

#%% Correlacion
M=8
x=np.zeros(M)
x[:2]=1

y=np.zeros(M)
y[5]=1

Rxy=signal.correlate(x,y)

plt.figure()
plt.plot(x,'x:',label='x')
plt.plot(y,'x:',label='y')
plt.plot(Rxy,label='Rxy')
plt.legend()
plt.show()

#%%
# N=8
# n=np.arange(N)

# x=4+3*np.sin(n*np.pi*(1/2))











