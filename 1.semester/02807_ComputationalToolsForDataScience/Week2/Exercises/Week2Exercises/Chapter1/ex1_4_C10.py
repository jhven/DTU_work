import sys

x = sys.argv[1].split(',')

def hasDuplicates(x):
    return len(set(x)) == len(x)

print(hasDuplicates(x))