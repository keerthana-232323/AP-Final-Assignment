class InvalidArgument(Exception):
    """Custom Exception to be raised for negative integers passed as arguments."""
    pass


def shift(s, acount=None, ccount=None):
    try:
        if acount != None:
            if acount < 0:
                raise InvalidArgument ("Negative acount not allowed.")
        if ccount != None:
            if ccount < 0:
                raise InvalidArgument ("Negative ccount not allowed.")
    except InvalidArgument as err:
        print(f"InvalidArgument: {err}")
    else:
        n = len(s)
        if acount:
            acount = acount % n
            new_s = s[acount:] + s[:acount]
            s = new_s
        if ccount:
            ccount = ccount % n
            new_s = s[-ccount:] + s[:-ccount]
            s = new_s
        return s


word = input("Enter a string: ")
shifted_word = shift(word, ccount=6, acount=3)
if shifted_word:
    print(shifted_word)
