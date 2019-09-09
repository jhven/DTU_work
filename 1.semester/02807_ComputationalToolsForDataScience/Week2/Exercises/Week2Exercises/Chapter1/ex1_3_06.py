import sys

n = int(sys.argv[1])

def writeHelloWorldNTimes(n):
    for i in range(1, n + 1):
        if i % 10 == 1 and (i % 100) // 10 != 1:
            print(str(i) + "st Hello, World!")
        elif i % 10 == 2:
            print(str(i) + "nd Hello, World!")
        elif i % 10 == 3:
            print(str(i) + "rd Hello, World!")
        else:
            print(str(i) + "th Hello, World!")

writeHelloWorldNTimes(n)