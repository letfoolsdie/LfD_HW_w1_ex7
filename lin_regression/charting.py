__author__ = 'Nikolay_Semyachkin'

import random
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
#from numpy.linalg import inv



#target function (provided in the exercise)
def target(x, y):
    return x**2 + y**2 - 0.6



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

def evaluatedatatargetfunction(data):
    #build points for target function and check the data
    noize = 0.1
    y = []
    for i in data:
        point = target(i[0], i[1])
        randd = random.uniform(0,1)
        if randd < noize:
            point *= -1.
        y.append(point)
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

#transforming data to non-linear space according to the formula provided in HW + building vectors immediately    
def transformdata(data):
    transformed = []    
    for i in data:
        transformed.append([1., i[0], i[1], i[0]*i[1], i[0]**2, i[1]**2])
    return transformed
total_error = 0.
total_out_error = 0.
#for i in range(1000):
    
    # get random points to build target function
#x1 = random.uniform(-1, 1)
#y1 = random.uniform(-1, 1)


data = np.array(builddataset(10))
targetv = np.array(evaluatedatatargetfunction(data))
vectors = np.array(transformdata(data))
dagger = np.dot(inv(np.dot(np.transpose(vectors), vectors)), np.transpose(vectors))
w = np.dot(dagger, targetv)
hypov = evaluatehypofunction(w, vectors)
plt.plot([k[0] for k in data], [i[0]**2 for i in data])
#    w_average += w
#print(w_average/1000)
#    error = classificationerror(targetv, hypov)
#print(w_average/1000)
#    in_sample_error = classificationerror(hypov, targetv)
#    total_error += in_sample_error
#print(total_error/1000)
