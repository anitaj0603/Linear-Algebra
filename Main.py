import numpy as np

try:
    n = int(input("Enter the size of the square matrix (e.g., 3 for a 3x3 matrix): "))

    matrix = []

    print("Enter the matrix row by row. Separate numbers with spaces:")
    for i in range(n):

        row = input(f"Enter row {i + 1}: ").split()

        if len(row) != n:
            print("Error: Each row must have exactly", n, "numbers.")
            exit()
        matrix.append([float(num) for num in row])


    matrix_array = np.array(matrix)


    determinant = np.linalg.det(matrix_array)
    print("The determinant is:", determinant)
except:
    print("An error occurred. Please make sure to enter valid numbers.")