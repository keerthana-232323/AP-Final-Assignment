def separate(s):
    if not s:
        return []

    s_list = list(s)
    current_char = s[0]
    current_group = current_char
    grouped_list = []
    for i in range(1, len(s_list)):
        if s[i] == current_char:
            current_group += s[i]
        else:
            grouped_list.append(current_group)
            current_char = s[i]
            current_group = current_char
    grouped_list.append(current_group)

    return grouped_list


word = input("Enter a word: ")
print(separate(word))
