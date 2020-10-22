import matplotlib.pyplot as plt
import numpy as np

P=np.linspace(-2,2,10000)
m=0.7

X = []
Y = []

for u in P:
    X.append(u)
    m = np.random.random()
    for n in range(1001):
      m=(u*m)*(1-m)
    # The break is harmful here as it prevents completion of
    # the loop and collection of data in Y 
    for l in range(1051):
      C
    # Collection of data in Y must be done once per value of u
    Y.append(m)
# Remove the line between successive data points, this renders
# the plot illegible. Use a small marker instead.
plt.plot(X, Y, ls='', marker=',')
plt.show()
