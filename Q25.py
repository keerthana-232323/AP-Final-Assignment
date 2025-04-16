class InvalidKValueException(Exception):
    pass


def kMax(I, k):
    if k <= 0 or k > len(I):
        raise InvalidKValueException("Invalid value of k. It must be between 1 and the length of the list.")

    sorted_list = sorted(I, reverse=True)

    return sorted_list[k - 1]


try:
    print(kMax([10, 2, 4, 5, 7, 9], 1))
    print(kMax([10, 2, 4, 5, 7, 9], 2))
    print(kMax([10, 2, 4, 5, 7, 9], 3))
    print(kMax([10, 2, 4, 5, 7, 9], 7))  # Raises InvalidKValueException
except InvalidKValueException as err:
    print(f"InvalidKValueException: {err}")
