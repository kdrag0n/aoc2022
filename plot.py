import matplotlib.pyplot as plt
import numpy as np

xs=[]
ys=[]
with open('real-rnds.csv','r') as f:
    for l in f.read().split('\n'):
        if l:
            x,y=l.split(',')
            x = int(x)
            y = int(y)
            xs.append(x)
            ys.append(y)

ys=np.diff(ys)
xs=xs[1:]

plt.plot(xs,ys)
plt.show()
