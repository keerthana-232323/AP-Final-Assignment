class DimensionMismatchException(Exception):
    pass


def matMul(A, B):
    m = int(len(A) ** 0.5)
    n = m
    p = int(len(B) ** 0.5)
    if n != p:
        raise DimensionMismatchException("Matrix dimensions do not match for multiplication.")

    result = [0] * (m * p)

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i * p + j] += A[i * n + k] * B[k * p + j]

    return result


A = [1, 2, 0, 4, 0, 5, 0, 7, 9]
B = [1, 2, 0, 4, 0, 5, 0, 7, 9]
try:
    result = matMul(A, B)
    print(result)
except DimensionMismatchException as e:
    print(e)
