def minOp(string1, string2):
    m = len(string1)
    n = len(string2)
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            else:
                if string1[j - 1] == string2[i - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1

    return table[n][m]


input_word1 = input("Enter string 1: ")
input_word2 = input("Enter string 2: ")
print(minOp(input_word1, input_word2))
