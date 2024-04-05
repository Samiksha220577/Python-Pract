#matix 1
matrix = []
x=int(input("Enter range"))
print("enter 1st matrix elements")
for i in range(x):
   row = []
   for j in range(x):

      element = int(input())
      row.append(element)
   matrix.append(row)
print("matrix 1")
for j in matrix:
   print(j)
#matrix 2
matrix2=[]
print ("enter 2nd matrix elements")
for i in range(x):
   row2=[]
   for j in range(x):

      element2=int(input())
      row2.append(element2)
   matrix2.append(row2)
print("matrix2")
for i in matrix2:
   print(i)
#summation
sum=[]
for i in range(x):
   rows=[]
   for j in range(x):
      rows.append(0)
   sum.append(rows)
for i in range(x):
    for j in range(x):
        sum[i][j] = matrix[i][j] + matrix2[i][j]

print("sum of matrix is:")
for r in sum:
    print(r)




# # 2.1 add two matrices
# X= [list(map(int, i.split())) for i in input().split(',')]
# Y = [list(map(int, i.split())) for i in input().split(',')]
#
#
# result = [[0]*3 for i in range(len(X))]
# print(result)
# for i in range(len(Y)):
#     for j in range(len(Y[0])):
#         result[i][j] = X[i][j] + Y[i][j]
# for k in result:
#     print(k)