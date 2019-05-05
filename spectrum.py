import numpy as np
import matplotlib.pyplot as plt

E=np.genfromtxt("Spectrum45kVRh.csv")
plt.title("Tugsten anode spectrum at 45kV")
plt.xlabel(r'Energy(keV) ')
plt.ylabel(r"photon fluence ($\frac{photons}{mm^2})$")
plt.plot(E[:,0],E[:,1])
plt.savefig("Spectrum45kV.png")
