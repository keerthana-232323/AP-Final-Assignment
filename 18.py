def delDup(int_list):
    length = len(int_list)
    org_list = []
    for i in range(length):
        if int_list[i] not in org_list:
            org_list.append(int_list[i])

    return org_list


print(delDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20]))
print(delDup([-1, 1, -1, 8]))
