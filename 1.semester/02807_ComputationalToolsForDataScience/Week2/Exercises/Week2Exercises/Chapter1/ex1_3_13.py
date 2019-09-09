import math
import sys

n = int(sys.argv[1])

def writePowersOfTwo(n):
    if n < 0:
        return
    elif n == 0:
        print(math.pow(2, 0))
    else:
        for i in range(0,n):
            print(math.pow(2, i))

writePowersOfTwo(n)