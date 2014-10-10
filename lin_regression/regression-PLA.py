# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 15:00:27 2014

@author: Nikolay_Semyachkin
"""

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

def getmisclassified(x, y, data):
    misclassified = []
    for i in range(len(x)):
        if x[i] != y[i]:
            misclassified.append([data[i], y[i]])
    return misclassified
#simply creates vectors for further use from given points by adding 1.0 in front of coordinates
def buildxvectors(data):
    vectors = [[1.0, data[i][0], data[i][1]] for i in range(len(data))]
    return vectors
total_error = 0.
total_out_error = 0.
total_iterations = 0.
for i in range(1000):
    
    # get random points to build target function
    x1 = random.uniform(-1, 1)
    y1 = random.uniform(-1, 1)
    x2 = random.uniform(-1, 1)
    y2 = random.uniform(-1, 1)
    
    data = np.array(builddataset(10))
    targetv = np.array(evaluatedatatargetfunction(data, x1, y1, x2, y2))
    vectors = np.array(buildxvectors(data))
    dagger = np.dot(inv(np.dot(np.transpose(vectors), vectors)), np.transpose(vectors))
    w = np.dot(dagger, targetv)
    hypov = evaluatehypofunction(w, vectors)
    iterations = 0
   # misclassified = getmisclassified(hypov, targetv, data)
    while True:
        misclassified = getmisclassified(hypov, targetv, data)
        #print(misclassified)
        if misclassified:
            iterations += 1
            random_point = random.choice(misclassified)
            w[0] = w[0] + random_point[1]
            w[1] = w[1] + random_point[1] * random_point[0][0]
            w[2] = w[2] + random_point[1] * random_point[0][1]
            hypov = evaluatehypofunction(w, vectors)
        else:
            #print(iterations)
            total_iterations += iterations
            break
            
print(total_iterations / 1000)
    #in_sample_error = classificationerror(hypov, targetv)
  #  total_error += in_sample_error
    
