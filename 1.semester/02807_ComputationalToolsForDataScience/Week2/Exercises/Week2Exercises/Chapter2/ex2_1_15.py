def rescaleArray(x):
    for i in range(len(x)):
        if float(x[i]) <= 0.0:
            return "Array must only contain stricly positive floating point values!"
        else:
            x[i] = (x[i] - min(x))/(max(x) - min(x))
    return x

print(rescaleArray([1.0, 2.0, 2.1, 0.2]))