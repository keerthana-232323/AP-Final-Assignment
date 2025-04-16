class LengthMismatchException(Exception):
    pass


def weave(list1, list2):
    if len(list1) != len(list2):
        raise LengthMismatchException("The two lists must have equal lengths.")

    return list1 + list2


# Example usage
try:
    print(weave([], []))
    print(weave([1, 2, 3], [4, 5, 6]))
    print(weave([1, 2], [3, 4, 5]))
except LengthMismatchException as err:
    print(f"LengthMismatchException: {err}")