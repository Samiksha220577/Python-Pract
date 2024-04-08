# x=[1,2,3,4,7,7,7,8,9]
# for i in range(0,len(x)):
#     print(i)
# print()
#
# for i in x :
#     print(i)
# print()
# for i in range(len(x)):
#     print(i)

matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for k in range(len(matrix[0])):
    res = [sub[k] for sub in matrix]
    print(res)