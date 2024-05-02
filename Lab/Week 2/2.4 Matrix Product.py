# # x=[list(map(int,i.split()))for i in input().split(',')]
# # print('matrix-1')
# # for i in x:
# #     print(i)
# # pro=1
# # for row in x:
# #     for ele in row:
# #         pro *=ele
# # print('product',pro)
# #
# #
# #
# # #1 4 5,7 3,4,46 7 3
# # # -------------------------------------------------------

# x=[list(map(int,i.split()))for i in input().split(',')]
# print('matrix-1')
# for i in x:
#     print(i)
# y=[list(map(int,i.split()))for i in input().split(',')]
# print('matrix-2')
# for i in y:
#     print(i)
# print()
#
# pro = [[0] * len(y[0]) for _ in range(len(x))]
# # for i in pro:
# #     print(i)
#
# # iterate through rows of X
# for i in range(len(x)):
#    # iterate through columns of Y
#    for j in range(len(y[0])):
#         # iterate through rows of Y
#        for k in range(len(y)):
#            pro[i][j] += x[i][k] * y[k][j]
#
# for r in pro:
#     print(r)
# -------------------------------------------------------
# n1=int(input('enter range'))
# m1=[]
# for i in range(n1):
#     k=[int(i) for i in input('enter matrix').split(',')]
#     m1.append(k)
# n2=int(input('enter range 2'))
# m2=[]
# for i in range(n2):
#     k=[int(i) for i in input('enter matrix 2').split(',')]
#     m2.append(k)
# result=[]
# for i in range(n1):
#     row=[]
#     for j in range(len(m2[0])):
#         temp=0
#         for k in range(n2):
#             temp+=m1[i][k]*m2[k][j]
#         row.append(temp)
#     result.append(row)
# for i in result:
#     print(*i,sep=', ')
# ----------------------------------------------------------
# def matrix_multiply():
#     # Get the dimensions of the matrices from the user
#     rows_A = int(input("Enter the number of rows for matrix A: "))
#     cols_A = int(input("Enter the number of columns for matrix A: "))
#     rows_B = int(input("Enter the number of rows for matrix B: "))
#     cols_B = int(input("Enter the number of columns for matrix B: "))
#
#     # Check if the matrices can be multiplied
#     if cols_A!= rows_B:
#         print("Error: Matrices cannot be multiplied")
#         return
#
#     # Create the matrices
#     A = [[0 for _ in range(cols_A)] for _ in range(rows_A)]
#     B = [[0 for _ in range(cols_B)] for _ in range(rows_B)]
#
#     # Get the elements of the matrices from the user
#     print("Enter the elements of matrix A:")
#     for i in range(rows_A):
#         for j in range(cols_A):
#             A[i][j] = float(input(f"Enter element ({i+1},{j+1}): "))
#
#     print("Enter the elements of matrix B:")
#     for i in range(rows_B):
#         for j in range(cols_B):
#             B[i][j] = float(input(f"Enter element ({i+1},{j+1}): "))
#
#     # Perform matrix multiplication
#     C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
#     for i in range(rows_A):
#         for j in range(cols_B):
#             for k in range(cols_A):  # or 'range(rows_B)'
#                 C[i][j] += A[i][k] * B[k][j]
#
#     # Print the result
#     print("The result of the matrix multiplication is:")
#     for row in C:
#         print(" ".join(str(x) for x in row))
#
# matrix_multiply()
# ----------------------------------------------------------
# Python3 program to multiply two matrices.
# MAX = 100
#
#
# # Function to print Matrix
# def printMatrix(M, rowSize, colSize):
#     for i in range(rowSize):
#         for j in range(colSize):
#             print(M[i][j], end=" ")
#
#         print()
#
#     # Function to multiply two matrices
#
#
# # A[][] and B[][]
# def multiplyMatrix(row1, col1, A,
#                    row2, col2, B):
#     # Matrix to store the result
#     C = [[0 for i in range(MAX)]
#          for j in range(MAX)]
#
#     # Check if multiplication is Possible
#     if (row2 != col1):
#         print("Not Possible")
#         return
#
#     # Multiply the two
#     for i in range(row1):
#         for j in range(col2):
#             C[i][j] = 0
#             for k in range(row2):
#                 C[i][j] += A[i][k] * B[k][j];
#
#             # Print the result
#     print("Resultant Matrix: ")
#     printMatrix(C, row1, col2)
#
#
# # Driver Code
# if __name__ == "__main__":
#
#     A = [[0 for i in range(MAX)]
#          for j in range(MAX)]
#     B = [[0 for i in range(MAX)]
#          for j in range(MAX)]
#
#     # Read size of Matrix A from user
#     row1 = int(input("Enter the number of rows of First Matrix: "))
#     col1 = int(input("Enter the number of columns of First Matrix: "))
#
#     # Read the elements of Matrix A from user
#     print("Enter the elements of First Matrix: ");
#     for i in range(row1):
#         for j in range(col1):
#             A[i][j] = int(input("A[" + str(i) +
#                                 "][" + str(j) + "]: "))
#
#     # Read size of Matrix B from user
#     row2 = int(input("Enter the number of rows of Second Matrix: "))
#     col2 = int(input("Enter the number of columns of Second Matrix: "))
#
#     # Read the elements of Matrix B from user
#     print("Enter the elements of Second Matrix: ");
#     for i in range(row2):
#         for j in range(col2):
#             B[i][j] = int(input("B[" + str(i) +
#                                 "][" + str(j) + "]: "))
#
#     # Print the Matrix A
#     print("First Matrix: ")
#     printMatrix(A, row1, col1)
#
#     # Print the Matrix B
#     print("Second Matrix: ")
#     printMatrix(B, row2, col2)
#
#     # Find the product of the 2 matrices
#     multiplyMatrix(row1, col1, A, row2, col2, B)
#
# # This code is contributed by Ryuga
#----------------------------------------------------------------------------------------
x=[]
[r1,c1]=list(map(int,input().split(',')))
for i in range(r1):
    u=list(map(int,input().split(',')))
    x.append(u)
pro=1
for i in x:
    for j in i:
        pro=pro*j
print(pro)
