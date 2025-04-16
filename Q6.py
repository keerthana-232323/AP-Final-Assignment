# create a function that takes two strings and sort the alphabets not common to the strings

def distChar(s1, s2):
    not_existing_chars = []
    for char in s1:
        if char not in s2:
            if char not in not_existing_chars:
                not_existing_chars.append(char)

    for char in s2:
        if char not in s1:
            if char not in not_existing_chars:
                not_existing_chars.append(char)

    return "".join(sorted(not_existing_chars))


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
result = distChar(str1, str2)
print(result)
