def moveDups(s):
    list1 = []
    list2 = ["_"]
    for char in s:
        if char not in list1:
            list1.append(char)
        else:
            list2.append(char)

    if len(list2) > 1:
        for char in list2:
            list1.append(char)

    return "".join(list1)


s = input("Enter a string: ").lower()
print(moveDups(s))
