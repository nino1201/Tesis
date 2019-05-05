from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit



# read data from a text file. One number per line
total=np.genfromtxt("CdTeEscalera10keV.txt")*1e21
total1=np.genfromtxt("CdTeEscalera15keV.txt")*1e21

total2=np.genfromtxt("CdTeEscalera20keV.txt")*1e21
total3=np.genfromtxt("CdTeEscalera25keV.txt")*1e21
total4=np.genfromtxt("CdTeEscalera30keV.txt")*1e21
total5=np.genfromtxt("CdTeEscalera35keV.txt")*1e21
Et=np.genfromtxt("CdTeEscalera2_30keV56.txt")*1e23


x=np.array([0,51, 99,147,196,245])
y=np.array([0,46,97,148,199,245])
t=np.array([40,38,36,34,32,30,28,26,24])*1.19/10
def AverageSquare(image,xi,xf,yi,yf):
	return np.mean(image[xi:xf+1,yi:yf+1])

def exponencial(x,I0,mu):
	return(I0*np.exp(-mu*x))

def Ac(Image):
	Datos=[]
	for i in range(5):
		Datos.append(AverageSquare(Image,0,52,y[i],y[i+1]))
		if i!=0:
			Datos.append(AverageSquare(Image,x[i],x[i+1],199,246))
	I=np.sort(Datos)
	


	popt1, pcov1 = curve_fit(exponencial, t, I,p0=(0.5,0.8))
	return(popt1,I)
Mu=np.zeros(6)
MuO=np.zeros(4)
E=np.array([10,15,20,25,30,35])

MI10=Ac(total)[0]
Mu[0]=MI10[1]
MuO[0]=MI10[1]

MI15=Ac(total1)[0]
Mu[1]=MI15[1]
MuO[1]=MI15[1]

MI20=Ac(total2)[0]
Mu[2]=MI20[1]
MuO[2]=MI20[1]

MI25=Ac(total3)[0]
Mu[3]=MI25[1]


MI30=Ac(total4)[0]
Mu[4]=MI30[1]
MuO[3]=MI30[1]

MI35=Ac(total5)[0]
Mu[5]=MI35[1]



MuO2=np.array([3.357,1.101,0.5714,0.3032])

x2=np.linspace(0.1,10)

plt.plot(x2,exponencial(x2,MI20[0],MI20[1]))
plt.scatter(t,Ac(total2)[1],s=2.5,c="r")
plt.title(r"Intensity vs Distance")
plt.ylabel(r"Intensity $ (p.d.u)$")
plt.xlabel(r"Distance $(mm)$")
plt.show()

#print(abs(MI30[0]))
#plt.matshow(Et)
#plt.colorbar()
#plt.clim(0.05,0.5)
#plt.yscale("log")
#plt.xscale("log")
#plt.title(r"$\mu$ vs Energy")
#plt.scatter(E,Mu,linewidth=0.6)
plt.show()




