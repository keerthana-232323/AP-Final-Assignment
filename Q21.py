def moveZeros(int_list):
    return [x for x in int_list if x != 0] + [0] * int_list.count(0)


print(moveZeros([1, 2, 0, 4, 0, 5, 0]))
