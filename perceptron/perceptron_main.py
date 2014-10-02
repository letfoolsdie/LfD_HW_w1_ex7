__author__ = 'Nikolay_Semyachkin'
import random
import math
import copy

def perceptron_training (x1, y1, x2, y2, training_size):
    def target(x1, y1, x2, y2, x):
        return ((y2-y1)/(x2-x1))*(x-x1)+y1
    w = [0, 0, 0]


w = [0, 0, 0]
def target(x1, y1, x2, y2, x):
    return ((y2-y1)/(x2-x1))*(x-x1)+y1
x1 = random.uniform (-1, 1)
y1 = random.uniform (-1, 1)
x2 = random.uniform (-1, 1)
y2 = random.uniform (-1, 1)


def multiply_vectors(w, x):
    g = [a*b for a, b in zip(w, x)]
    return math.copysign(1, sum(g))


data_set = []
for i in range(10):
    data_set.append([random.uniform(-1, 1), random.uniform(-1, 1)])
#g = copy.deepcopy(data_set)
g = [[1.0, data_set[i][0], data_set[i][1]] for i in range(10)]


#print(g)
#print(multiply_vectors(w, g[0]))
for i in data_set:
    if target(x1, y1, x2, y2, i[0]) < i[1]:
        i.append(1.0)
    else:
        i.append(-1.0)
misclassified = []
for i in range(10):
    if data_set[i][2] != multiply_vectors(w, g[i]):
        misclassified.append(data_set[i])


#print(g)

print(data_set)
print(misclassified)