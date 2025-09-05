# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 19:28:38 2025

@author: Sofía
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N=10
Ts=1/1000

tt= np.linspace(0,(N-1)*Ts,N).flatten()

x1=(2*np.pi*2000*tt)