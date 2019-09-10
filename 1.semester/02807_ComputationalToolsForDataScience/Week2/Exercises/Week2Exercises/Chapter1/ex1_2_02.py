import math
import sys

teta = float(sys.argv[1])

def calculateIdiotEquation(teta):
    return math.pow(math.cos(teta), 2) + math.pow(math.sin(teta), 2)

print(calculateIdiotEquation(teta))