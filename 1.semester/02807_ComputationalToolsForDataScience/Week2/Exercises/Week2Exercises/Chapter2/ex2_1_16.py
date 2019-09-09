def histogram(a, m):
    histogramArray = [0 for x in range(m)]
    for i in range(len(a)):
        histogramArray[a[i]] += 1
    return histogramArray

print(histogram([0,1,2,3,4,5,5,4,4,4,4,4], 6))