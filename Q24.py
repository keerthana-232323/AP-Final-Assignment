def splitsum(I):
    return [sum(x**2 for x in I if x > 0), sum(x**3 for x in I if x < 0)]


I = [1, -2, 3, 4, -5]
result = splitsum(I)
print(result)
