def rotations(s):
    """Generate all rotations of the string s."""
    return {s[i:] + s[:i] for i in range(len(s))}


def equivalent(str1, str2):
    longest_substring = ""

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring1 = str1[i:j]
            len_substring1 = len(substring1)

            for k in range(len(str2)):
                for l in range(k + 1, len(str2) + 1):
                    substring2 = str2[k:l]

                    substring2_rotations = rotations(substring2)

                    if substring1 in substring2_rotations:
                        if (len_substring1 > len(longest_substring) or
                                (len_substring1 == len(longest_substring) and substring1 < longest_substring)):
                            longest_substring = substring1

    return longest_substring


print(equivalent('hdjkoul', 'pokoudj'))
print(equivalent('ghajiop', 'abkoidj'))
print(equivalent('hdjkoul', 'pikpiaa'))
