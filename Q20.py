def oddCollatz(n):
    if n <= 0:
        raise ValueError("Input must cannot be less than 1.")

    collatz_sequence = []

    while n != 1:
        if n % 2 == 1:
            collatz_sequence.append(n)
            n = 3 * n + 1
        else:
            n = n // 2

    collatz_sequence.append(1)
    return collatz_sequence


try:
    print(oddCollatz(1))
    print(oddCollatz(3))
    print(oddCollatz(5))
    print(oddCollatz(7))
except ValueError as err:
    print(f"ValueError: {err}")
