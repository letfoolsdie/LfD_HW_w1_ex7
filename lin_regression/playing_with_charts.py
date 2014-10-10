import matplotlib.pyplot as pl
import numpy as np
import random

def builddataset(n):
    data_set = [random.uniform(-1, 1) for i in range(n)]
    return data_set
    
x = builddataset(1000)
y = [i*2 for i in x]

pl.plot(x, y)
pl.show()