# #list inside list input in pyhton
# # Create an empty list to store the input
# list1 = []
#
# # Take input from the user
# input_string = input("Enter a list of lists, separated by commas: ")
#
# # Split the input string into a list of strings
# list_of_strings = input_string.split(",")
#
# # Iterate over the list of strings and convert each string to a list
# for string in list_of_strings:
#     list1.append(string.split())
#
# # Print the list
# print(list1)
# ----------------------
# # Create an empty list to store the input
# list1 = []
#
# # Take input from the user
# input_string = input("Enter a list of lists, separated by commas: ")
#
# # Split the input string into a list of strings
# list_of_strings = input_string.split(",")
#
# # Iterate over the list of strings
# for string in list_of_strings:
#     # Create an empty list to store the sub-list
#     sublist = []
#
#     # Split the string into a list of strings
#     list_of_elements = string.split()
#
#     # Iterate over the list of elements and append each element to the sub-list
#     for element in list_of_elements:
#         sublist.append(element)
#
#     # Append the sub-list to the final list
#     list1.append(sublist)
#
# # Print the list
# print(list1)
# _______________________________________________________
# #integer list inside a list input
# # Read input from user
# input_str = input("Enter a list of lists of integers separated by commas, where each list is separated by spaces: ")
#
# # Split the input string into a list of strings, where each string is a list of integers
# list_str = input_str.split(',')
#
# # Convert each string to a list of integers
# lists = [list(map(int, sublist.split())) for sublist in list_str]
#
# # Print the resulting list of lists of integers
# print(lists)
# ______________________________________________________
# #matrix
# #matrix creation
# x=[list(map(int,i.split()))for i in input().split(',')]
# y=[list(map(int,i.split()))for i in input().split(',')]
# # 1 2 3,4 5 6
# # 10 11,20 21,30 31
# #empty matrix for multiplication min of rows and columns
# pro = [[0] * len(y[0]) for _ in range(len(x))]
# #output
# #[140, 146]
# #[320, 335]
# _______________________________________________________
#
# #list itteration
# x=[1,2,3,4,7,7,7,8,9]
# for i in range(0,len(x)):
#     print(i)
# print()
# output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
#
# for i in x :
#     print(i)
# print()
# output
# 1
# 2
# 3
# 4
# 7
# 7
# 7
# 8
# 9
#
# for i in range(len(x)):
#     print(i)
# output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# _______________________________________________________
# #matrix itteration
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# ------------------------------
# for i in matrix:
#     print(i)
# output
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# -------------------------------
# for i in range(len(matrix)):
#     print(i)
# output
# 0
# 1
# 2
# -------------------------------
# #accessing each element of the matrix
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# pmatrixrint(matrix)
# for row in matrix:
#     # Iterate over the columns of the row
#     for element in row:
#         # Print the element
#         print(element)
# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# --------------------------------
# # Get the element at row 1, column 2 of the matrix
# element = matrix[1][2]
#
# # Print the element
# print(element)
# output
# 6
# ---------------------------------
# # Set the element at row 1, column 2 of the matrix to 10
# matrix[1][2] = 10
#
# # Print the matrix
# print(matrix)
# output  [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
# --------------------------------
# #accessing row of a matrix
# def get_row(matrix, row_index):
#   """Returns the row of a matrix at the given index.
#
#   Args:
#     matrix: A 2D list representing the matrix.
#     row_index: The index of the row to get.
#
#   Returns:
#     A list representing the row of the matrix at the given index.
#   """
#
#   row = []
#   for i in range(len(matrix[0])):
#     row.append(matrix[row_index][i])
#   return row
#
#
# # Example usage:
#
# matrix = [[1, 2, 3], [4, 5, 6]]
# row = get_row(matrix, 1)
# print(row)
# output
# [4, 5, 6]
# --------------------------
# #accessing row of a matrix
# Using a list comprehension:
# def get_row(matrix, row_index):
#   """Returns the row of a matrix at the given index.
#
#   Args:
#     matrix: A 2D list representing the matrix.
#     row_index: The index of the row to get.
#
#   Returns:
#     A list representing the row of the matrix at the given index.
#   """
#
#   return [matrix[row_index][i] for i in range(len(matrix[0]))]
#
#
# # Example usage:
#
# matrix = [[1, 2, 3], [4, 5, 6]]
# row = get_row(matrix, 1)
# print(row)
# output
# [4, 5, 6]
# ---------------------------------------
# #accessing column elements of a matrix
# matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# for k in range(len(matrix[0])):
#     for sub in matrix:
#         print(sub[k])
#     print()
#
# output
# 1
# 4
# 7
# 10
#
# 2
# 5
# 8
# 11
#
# 3
# 6
# 9
# 12
# ---------------
# #accessing columns of a matrix using list comprehension
# matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#
#
# _______________________________________________________
