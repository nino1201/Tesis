from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
x=np.array([1,50, 99,149,202,251])-1
y=np.array([1,44,97,150,200,251])-1
t=np.array([11,16,17,21,22,23,26,27,28,29,31,32,33,34,35,37,38,39,40,43,44,45,49,50,55])[::-1]*1.19/10


total=np.genfromtxt("CdTeEscalera2_20keV56.txt")*1e21
def AverageSquare(image,xi,xf,yi,yf):
	return np.mean(image[xi:xf+1,yi:yf+1])

def exponencial(x,I0,mu):
	return(I0*np.exp(-mu*x))

def Ac(Image):
	Datos=[]
	for i in range(5):
		for j in range(5):
			Datos.append(AverageSquare(Image,x[i],x[i+1],y[j],y[j+1]))			
	I=np.sort(Datos)
	t1=t


	popt1, pcov1 = curve_fit(exponencial, t1, I,p0=(0.5,0.8))
	return(popt1,I)

MI=Ac(total)[0]
Mu=MI[1]

print(Mu)


#plt.matshow(total)
plt.scatter(t,Ac(total)[1],s=2.5,c="r")
plt.plot(t,exponencial(t,MI[0],MI[1]))
plt.title(r"Intensity vs Distance")
plt.ylabel(r"Intensity $(p.d.u)$")
plt.xlabel(r"Distance $(mm)$")
#plt.clim(2,10)
#plt.colorbar()
plt.show()
