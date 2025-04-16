# Define a function to check if a given word is a palindrome

def checkPalindrome(word):
    j = -1
    for i in range(int(len(word)/2)):
        if word[i] == word[j]:
            j -= 1
        else:
            return False
    return True


input_word = input("Enter a word to check if it is a palindrome: ")
is_palindrome = checkPalindrome(input_word)
if is_palindrome:
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")
