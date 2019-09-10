def canBeTriangle(a, b, c):
    return a + b >= c and a + c >= b and b + c >= a

print(canBeTriangle(3,4,5))
print(canBeTriangle(1,2,4))