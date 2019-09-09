import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

def gcd(x, y):
    if x <= 0 or y <= 0:
        return "x and y must be positive integers!"
    elif x > y and x % y == 0:
        return y
    elif x > y and x % y != 0:
        return gcd(x % y, y)
    elif x < y and y % x == 0:
        return x
    elif x < y and y % x != 0:
        return gcd(x, y % x)
    elif x == y:
        return x

print(gcd(x, y))
