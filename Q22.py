class DimensionMismatchException(Exception):
    """Custom exception for dimension mismatch."""
    pass


def printMat(matrix_list, rows, cols):
    # Check if the total number of elements matches the specified dimensions
    if len(matrix_list) != rows * cols:
        raise DimensionMismatchException("Dimension mismatch: the number of elements does not match the "
                                         "specified dimensions.")

    # Print the matrix in row-major order
    for i in range(rows):
        for j in range(cols):
            index = i * cols + j
            print(matrix_list[index], end=' ')
        print()


try:
    printMat([1, 2, 0, 4, 0, 5, 0, 7, 9], 3, 3)
except DimensionMismatchException as e:
    print(e)
