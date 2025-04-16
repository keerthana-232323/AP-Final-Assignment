# Remove k characters from the string so that each character occurs the same number of times. If it is not possible,
# return an empty string

def has_equal_frequencies(freq_map):
    # Remove zero-frequency characters
    to_delete = [char for char in freq_map if freq_map[char] == 0]
    for char in to_delete:
        del freq_map[char]
    return len(set(freq_map.values())) == 1


def get_frequency_map(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


def get_max_char(freq_map):
    return max(freq_map, key=lambda c: freq_map[c])


def build_string(freq_map):
    return ''.join(char * count for char, count in freq_map.items())


def try_remove_whole(freq_map, k):
    candidates = [char for char in freq_map if freq_map[char] == k]
    for char in candidates:
        temp_map = freq_map.copy()
        del temp_map[char]
        if has_equal_frequencies(temp_map):
            return temp_map
    return freq_map


def equalize_char_frequencies(input_str, k):
    freq_map = get_frequency_map(input_str)

    if has_equal_frequencies(freq_map.copy()):
        return input_str

    modified_map = try_remove_whole(freq_map.copy(), k)
    if has_equal_frequencies(modified_map.copy()):
        return build_string(modified_map)

    temp_map = freq_map.copy()
    for _ in range(k):
        max_char = get_max_char(temp_map)
        temp_map[max_char] -= 1

    if has_equal_frequencies(temp_map.copy()):
        return build_string(temp_map)
    else:
        return ''


print(equalize_char_frequencies('aabbcc', 0))
print(equalize_char_frequencies('aabbbcc', 0))
print(equalize_char_frequencies('aabbbcc', 1))
print(equalize_char_frequencies('aabbbcc', 2))
print(equalize_char_frequencies('aabbbcc', 3))
print(equalize_char_frequencies('aabbbcc', 4))
print(equalize_char_frequencies('aabbbcc', 5))
print(equalize_char_frequencies('aabbbcc', 6))
print(equalize_char_frequencies('aabbbcc', 7))
print(equalize_char_frequencies('aaaabbcc', 4))
