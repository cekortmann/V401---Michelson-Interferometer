import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  


nu = uarray ([2540,2607,2117,3002,2504,2519,2836,2596,2664,2967],[0,0,0,0,0,0,0,0,0,0])

ud = uarray(5.00*10**(-3),0.01*10**(-3))

def Lambda(d,z):
    return d/5.046/z*2

n = len(nu) 
print(n)                            # Anzahl der Daten
mean = sum(nu)/n  
print(mean)                   # Mittelwert
sigma = (sum((nu - mean)**2)/n-1)**(1/2) 
m= sum(Lambda(ud,nu))/len(Lambda(ud,nu))

print(sigma)
print('Lambda', Lambda(ud,nu))
print('Mittelwert',Lambda(ud,mean))