import math
import sys

x = sys.argv[1].split(',')
y = sys.argv[2].split(',')

def euclideanDistance(x, y):
    result = 0
    if len(x) != len(y):
        return "Vectors must be of same dimension! Vectors have dimensions " + len(x) + " and " + len(y)

    for i in range(0, len(x)):
        result += math.pow(float(x[i]) - float(y[i]), 2)
    return result

print(euclideanDistance(x, y))