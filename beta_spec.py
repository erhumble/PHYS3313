import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


B =83.09e-3
R = (57.29e-2)/2
q = 1.6e-19
c = 299792458
m = 9.109e-31
eV = 1.6e-19
background_rad = 12
filename = 'beta_data_thallium.csv'

df=pd.read_csv(filename, sep=',')
beta_data = df.to_numpy(dtype=float)[:, 0:5]
p = []
background = []
for i in range(0, len(beta_data)):
    if(beta_data[i,0] > 0):
        print("Beta angle is: " + str(beta_data[i,0] * (3.14/180)))
        p_point = q*B*(R/math.tan((beta_data[i,0]*(3.14/180))/2))
        p.append(p_point)
    else:
        background.append(beta_data[i, 4])

background_rad = np.average(background)
dKdP = []
for i in range(0, len(p)):
    dKdP_add = (p[i]*(c**2)) / math.sqrt((p[i]**2)*(c**2) + (m**2)*(c**4))
    dKdP.append(dKdP_add)
    #print('done1')
print(dKdP)
dPdTheta = []
for i in range(0, len(p)):
    dPdTheta_add = q*B*R / (2*(math.sin((beta_data[i,0]* (3.14/180))/2))**2)
    dPdTheta.append(dPdTheta_add)
    print('done2')
print("DONE")

#dKdTheta = dPdTheta * dKdP

dKdTheta = []
for i in range(0, len(dKdP)):
    dKdTheta_add = dPdTheta[i]*dKdP[i]
    dKdTheta.append(dKdTheta_add)
print("DONE3")

print(dKdTheta)

delta_k_theta = 10*np.asarray(dKdTheta)

normalized_counts = (beta_data[0:9, 4] - background_rad) / delta_k_theta
print(normalized_counts)

# now convert theta to kinetic energy
KE = []
for i in range(0, len(p)):
    KE_add = (math.sqrt((p[i]*c)**2 + (m*(c**2))**2) - m*(c**2)) /  q
    KE.append(KE_add)

print("KE lenght: " + str(len(KE)))
print(KE)

print('normalized counts: ' + str(len(normalized_counts)))
print(normalized_counts)
plt.scatter(KE, normalized_counts)
plt.title(filename)
plt.xlabel('Kinetic Energy (eV)')
plt.ylabel('count rate per unit kinetic energy')
plt.show()