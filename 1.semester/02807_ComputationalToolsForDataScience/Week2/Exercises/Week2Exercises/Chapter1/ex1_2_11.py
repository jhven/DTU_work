import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def isDivisable(a, b):
    if a <= 0 or b <= 0:
        return "The input must be positive integers!"
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False

print(isDivisable(a, b))