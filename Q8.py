VOWELS = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]


def delVowels(s):
    s_list = list(s)
    new_list = []
    for char in s_list:
        if char not in VOWELS:
            new_list.append(char)

    return "".join(new_list)


s = input("Enter a string: ")
print(delVowels(s))
