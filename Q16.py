def extractDup(arr):
    dups = []
    for i in range(len(arr)):
        if arr[i] not in dups:
            if arr.count(arr[i]) > 1:
                dups.append(arr[i])

    return dups


print(extractDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20]))
print(extractDup([-1, 1, -1, 8]))
print(extractDup([-3, 1, -1, 8]))
