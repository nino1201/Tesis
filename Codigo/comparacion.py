import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
def funcExp(x, p1,p2,p3):
  return -p1*np.exp(-p3*x)+p2


TeCd=np.array([0.4719,0.722,0.9586, 0.9964])
Th=np.array([0.1,0.2,0.5,1])
TeCdNew=np.array([0.45,0.686,0.927,0.988])

popt1, pcov1 = curve_fit(funcExp, Th, TeCd,p0=(1.0,1.2,10.))

p11 = popt1[0]
p21 = popt1[1]
p31 = popt1[2]


popt2, pcov2 = curve_fit(funcExp, Th, TeCdNew,p0=(1.0,1.2,10.))

p12 = popt2[0]
p22 = popt2[1]
p32 = popt2[2]

x=np.linspace(0.1,2)
TeCdNew2=funcExp(x,p11,p21,p31)
SiNew=funcExp(x,p12,p22,p32)

plt.scatter(Th,TeCd)
plt.scatter(Th,TeCdNew)
plt.plot(x, TeCdNew2)
plt.plot(x, SiNew)
plt.savefig("comparacion.png")
