__author__ = 'Nikolay_Semyachkin'

import random
import numpy as np
from numpy import linalg
#from numpy.linalg import inv



#build target function by 2 given points
def target(x1, y1, x2, y2, x):
    return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1


#create uniformly distributed data set of the given size
def builddataset(n):
    data_set = [[random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(n)]
    return data_set

def evaluatehypofunction(w, vector):
    y = []    
    for i in vector:
        if np.dot(w, i) > 0:
            y.append(1.)
        else:
            y.append(-1.0)
    return np.array(y)
#check each point in data set by target function and assign points to one area (1) or another (-1)
def evaluatedatatargetfunction(data, x1, y1, x2, y2):
    #build points for target function and check the data
    y = []
    for i in data:
        if target(x1, y1, x2, y2, i[0]) < i[1]:
            y.append(1.0)
        else:
            y.append(-1.0)
    return y
    
def classificationerror(x, y):
    total_misclassified = 0.  
    for i in range(len(x)):
        if x[i] != y[i]:
            total_misclassified += 1
    return total_misclassified / len(x)


#simply creates vectors for further use from given points by adding 1.0 in front of coordinates
def buildxvectors(data):
    vectors = [[1.0, data[i][0], data[i][1]] for i in range(len(data))]
    return vectors
total_error = 0.
total_out_error = 0.


# get random points to build target function
x1 = random.uniform(-1, 1)
y1 = random.uniform(-1, 1)
x2 = random.uniform(-1, 1)
y2 = random.uniform(-1, 1)

data = np.array(builddataset(100))

targetv = np.array(evaluatedatatargetfunction(data, x1, y1, x2, y2))
vectors = np.array(buildxvectors(data))
dagger = np.dot(linalg.inv(np.dot(np.transpose(vectors), vectors)), np.transpose(vectors))
w = np.dot(dagger, targetv)

X = np.linspace(-1., 1, 256)
p = [target(x1, y1, x2, y2, i) for i in X]
pl.xlim(X.min() * 1.1, X.max() * 1.1)
colors = ['b' if i == 1. else 'r' for i in targetv]
pl.scatter([data[i][0] for i in range(len(data))], [data[i][1] for i in range(len(data))], 25, c = colors)
pl.plot(X, p)

#hypov = evaluatehypofunction(w, vectors)
#in_sample_error = classificationerror(hypov, targetv)
#total_error += in_sample_error

outofsample = np.array(builddataset(1000))
outtargetv = np.array(evaluatedatatargetfunction(outofsample, x1, y1, x2, y2))
outvectors = np.array(buildxvectors(outofsample))
hypov = evaluatehypofunction(w, outvectors)
