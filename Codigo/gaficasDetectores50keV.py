import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

TeCd=np.array([0.4719,0.722,0.9586,0.9923, 0.9964,0.9989])
#TeCdPaper=
Si=np.array([0.0053,0.0107,0.0273,0.0438,0.055,0.109])
Se=np.array([0.149,0.276,0.557,0.729,0.805,0.9589])
GaAs=np.array([0.151,0.281,0.5639,0.735,0.8108,0.961])

Th=np.array([0.1,0.2,0.5,0.8,1,2])

def funcExp(x, p1,p2,p3):
  return -p1*np.exp(-p3*x)+p2

def funcLog(x, p1,p2,p3):
  return p1*np.log(p3*x)+p2

popt1, pcov1 = curve_fit(funcExp, Th, TeCd,p0=(1.0,1.2,10.))

p11 = popt1[0]
p21 = popt1[1]
p31 = popt1[2]


popt2, pcov2 = curve_fit(funcExp, Th, Si,p0=(1.0,1.2,10.))

p12 = popt2[0]
p22 = popt2[1]
p32 = popt2[2]


popt3, pcov3 = curve_fit(funcExp, Th, Se,p0=(1.0,1.2,10.))

p13 = popt3[0]
p23 = popt3[1]
p33 = popt3[2]


popt4, pcov4 = curve_fit(funcExp, Th, GaAs,p0=(1.0,1.2,10.))

p14 = popt4[0]
p24 = popt4[1]
p34 = popt4[2]


x=np.linspace(0.1,2)

TeCdNew=funcExp(x,p11,p21,p31)
SiNew=funcExp(x,p12,p22,p32)
SeNew=funcExp(x,p13,p23,p33)
GaAsNew=funcExp(x,p14,p24,p34)

plt.scatter(Th, TeCd)
plt.scatter(Th, Si)
plt.scatter(Th, Se)
plt.scatter(Th, GaAs)
plt.plot(x, TeCdNew)
plt.plot(x, SiNew)
plt.plot(x, SeNew)
plt.plot(x, GaAsNew)

plt.savefig("50kev.png")

