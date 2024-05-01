def matrix_multiply():
    # Get the dimensions of the matrices from the user
    rows_A = int(input("Enter the number of rows for matrix A: "))
    cols_A = int(input("Enter the number of columns for matrix A: "))
    rows_B = int(input("Enter the number of rows for matrix B: "))
    cols_B = int(input("Enter the number of columns for matrix B: "))

    # Check if the matrices can be multiplied
    if cols_A!= rows_B:
        print("Error: Matrices cannot be multiplied")
        return

    # Create the matrices
    A = [[0 for _ in range(cols_A)] for _ in range(rows_A)]
    B = [[0 for _ in range(cols_B)] for _ in range(rows_B)]

    # Get the elements of the matrices from the user
    print("Enter the elements of matrix A:")
    for i in range(rows_A):
        for j in range(cols_A):
            A[i][j] = float(input(f"Enter element ({i+1},{j+1}): "))

    print("Enter the elements of matrix B:")
    for i in range(rows_B):
        for j in range(cols_B):
            B[i][j] = float(input(f"Enter element ({i+1},{j+1}): "))

    # Perform matrix multiplication
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or 'range(rows_B)'
                C[i][j] += A[i][k] * B[k][j]

    # Print the result
    print("The result of the matrix multiplication is:")
    for row in C:
        print(" ".join(str(x) for x in row))

matrix_multiply()