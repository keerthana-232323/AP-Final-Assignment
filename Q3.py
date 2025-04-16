# Take the first letters of a sentence and return a word cocatenating them

def firstLetters(s):
    words_list = s.split(" ")
    first_letters = []
    for word in words_list:
        first_letters.append(word[0])
    return "".join(first_letters)


input_sentence = input("Enter a string: ")
print(firstLetters(input_sentence))
