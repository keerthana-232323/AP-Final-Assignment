# Return every letter in even indices in upper case. If the input string is already in upper case, raise an error
class UpperCaseException(Exception):
    """Custom error to be raised if the input string has uppercase letters."""
    pass


def evenIndexCapital(s):
    try:
        for char in s:
            if "A" <= char <= "Z":
                raise UpperCaseException("Input string has uppercase letters.")
    except UpperCaseException as err:
        print(f"UpperCaseException: {err}")
    else:
        result = ""
        for i in range(len(s)):
            if i % 2 == 0:
                result += s[i].upper()
            else:
                result += s[i]
        return result


input_word = input("Enter a word: ")
converted = evenIndexCapital(input_word)
if converted:
    print(converted)
