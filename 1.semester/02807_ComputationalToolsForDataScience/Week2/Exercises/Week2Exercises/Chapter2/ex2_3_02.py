import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def lnOfFactorialBruteforce(n):
    return math.log(factorial(n), math.e)

# def lnOfFactorialBruteforce(n):
#     if n < 0:
#         return "The input must be a positive integer!"
#     elif n == 0:
#         return 1
#     else:
#         factorial = n * lnOfFactorialBruteforce(n - 1)
#         return math.log(factorial, math.e)

def lnOfFactorial(n):
    return math.log(math.factorial(n), math.e)

print(lnOfFactorialBruteforce(10))
print(lnOfFactorial(10))