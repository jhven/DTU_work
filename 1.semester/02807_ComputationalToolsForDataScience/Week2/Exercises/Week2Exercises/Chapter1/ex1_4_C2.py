import sys

x = sys.argv[1].split(',')

def findLongestPlateau(x):
    plateauValue = -999999999
    plateauLocation = [0, 0]
    for i in range(len(x)):
        if i == 0:
            plateauValue = x[i]
        elif i == len(x) - 1 and plateauValue < x[i]:
            plateauValue = x[i]
            plateauLocation[0] = i
            plateauLocation[1] = i
        elif plateauValue < x[i] and x[i] < x[i+1]:
            continue
        elif plateauValue < x[i] and x[i] > x[i+1]:
            plateauValue = x[i]
            plateauLocation[0] = i
            plateauLocation[1] = i
        elif plateauValue < x[i] and x[i] == x[i+1]:
            plateauValue = x[i]
            plateauLocation[0] = i
        elif plateauValue == x[i] and x[i] == x[i+1]:
            continue
        elif plateauValue == x[i] and x[i] > x[i+1]:
            plateauLocation[1] = i
        elif plateauValue == x[i] and x[i] < x[i+1]:
            continue

    return [plateauValue, plateauLocation[0], plateauLocation[1]]

result = findLongestPlateau(x)
print("Highest plateau is at the value of", result[0], "located from", result[1], "to", result[2], "(zero-based).")