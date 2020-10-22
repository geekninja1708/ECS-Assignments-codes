

from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import numpy as np

nsamples=90
k = np.linspace(-2,2,nsamples)

l = []
for k1 in k:
  p = [-0.1,6.8,-153.2,1144-k1]
  l.append(np.roots(p))

l = np.array(l)

l1 = [l[i][l[i].imag==0].real for i in range(nsamples)]

for i,q in enumerate(l1):
  if len(q)==1:
    l1[i]=[q[0],q[0],q[0]]
l1 = np.array(l1)

from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import numpy as np
k2 = np.array([[k1,k1,k1] for k1 in k ])
plt.figure(figsize=(8,5))
plt.xlabel('k')
plt.ylabel('C')
plt.grid('True')

up = int(38*nsamples/100)
low = int(93*nsamples/100)

e = []
for q in l1[up:low]:
  e.append(q[1])

e = np.array(e)
plt.scatter(k2,l1,marker='.',s=30,edgecolors='yellow')
plt.scatter(k[up:low],e,s=30,facecolors='none',edgecolors='red')
plt.legend(labels=['Sinks','Sources'])
plt.show()
