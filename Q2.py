# Find the largest index of a character in str1 that is also present in str2

def minIndexFirstString(str1, str2):
    largest_index = -1
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                largest_index = i
    return largest_index


input_word1 = input("Enter string 1: ")
input_word2 = input("Enter string 2: ")
largest = minIndexFirstString(input_word1, input_word2)
print(f"The largest index is {largest}.")
