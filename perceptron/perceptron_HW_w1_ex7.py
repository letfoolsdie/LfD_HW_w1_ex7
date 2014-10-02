__author__ = 'Nikolay_Semyachkin'

import random
# get random points to build target function
x1 = random.uniform(-1, 1)
y1 = random.uniform(-1, 1)
x2 = random.uniform(-1, 1)
y2 = random.uniform(-1, 1)


#build target function by 2 given points
def target(x1, y1, x2, y2, x):
    return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1


#create uniformly distributed data set of the given size
def builddataset(n):
    data_set = [[random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(n)]
    return data_set


#check each point in data set by target function and assign points to one area (1) or another (-1)
def evaluatedatatargetfunction(data, x1, y1, x2, y2):
    #build points for target function and check the data

    for i in data:
        if target(x1, y1, x2, y2, i[0]) < i[1]:
            i.append(1.0)
        else:
            i.append(-1.0)
    return data


#simply creates vectors for further use from given points by adding 1.0 in front of coordinates
def buildxvectors(data):
    vectors = [[1.0, data[i][0], data[i][1]] for i in range(len(data))]
    return vectors


#so as the name says it multiply two vectors of the same size and returns the result
def multiplyvectors(w, x):
    scalar = [a * b for a, b in zip(w, x)]
    return sum(scalar)


#ok, this function evaluates the data and assign it to one area or another.
#Returns the set of points that was classified differently from the target function
def evaluatedatahypothesys(data, w, vectors):
    misclassified = []
    for i in range(len(data)):
        point = multiplyvectors(w, vectors[i])
        if point * data[i][2] <= 0:
            misclassified.append(data[i])
    return misclassified


w = [0, 0, 0]
iterations = 0
data = builddataset(10)
#print(buildxvectors(data))
vectors = buildxvectors(data)
evaluatedatatargetfunction(data, x1, y1, x2, y2)

while True:
    misclassified = evaluatedatahypothesys(data, w, vectors)
    #print(misclassified)
    if misclassified:
        iterations += 1
        random_point = random.choice(misclassified)
        w[0] = w[0] + random_point[2]
        w[1] = w[1] + random_point[2] * random_point[0]
        w[2] = w[2] + random_point[2] * random_point[1]
    else:
        #print(iterations)
        break
print(w)

data = builddataset(1000)

vectors = buildxvectors(data)
evaluatedatatargetfunction(data, x1, y1, x2, y2)
misclassified = evaluatedatahypothesys(data, w, vectors)
missed = len(misclassified) / 1000.

print(missed)