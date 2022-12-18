import matplotlib.pyplot as plt
import numpy as np

xs=[]
heights=[]
with open('real-rnds.csv','r') as f:
    for l in f.read().split('\n'):
        if l:
            x,y=l.split(',')
            x = int(x)
            y = int(y)
            xs.append(x)
            heights.append(y)

for size in range(20, 2500):
    start = heights[0]
    end = heights[size]
    end2 = heights[size*2]
    if end2 == start + end + end:
        print('found', size)
        print('d', end-start)
        break
