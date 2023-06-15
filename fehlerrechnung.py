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



zu = uarray ([30, 17, 19, 21, 24],[0,0,0,0,0])

lam = ufloat(736*10**(-9), 1.5*10**(-9))

p = ufloat(0.6*100000, 0.05*100000)

def brech(z):
    return 1 + (z*lam*293.15*1.0132*100000)/(2*50*10**(-3)*273.15*(1.0131*100000-p))

n2 = len(zu) 
print(n2)                            # Anzahl der Daten
mean2 = sum(zu)/n2  
print(mean2)                   # Mittelwert
sigma2 = (sum((zu - mean2)**2)/n2-1)**(1/2) 
m2= sum(brech(zu))/len(brech(zu))

print(sigma2)
print('Lambda', brech(zu))
print('Mittelwert',brech(mean2))


ulexp= uarray(736.0,1.5)
utheo= uarray(635,0)
abw= (ulexp-utheo)/utheo
print(abw)
