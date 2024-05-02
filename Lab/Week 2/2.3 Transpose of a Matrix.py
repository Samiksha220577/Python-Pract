# matrix=[list(map(int,i.split()))for i in input().split(',')]
# print('matrix')
# for k in range(len(matrix[0])):
#     res = [sub[k] for sub in matrix]
#     print(res)
# -----------------------------------
x=[]
[r1,c1]=list(map(int,input().split(',')))
for i in range(r1):
    u=list(map(int,input().split(',')))
    x.append(u)
mat=[[0]*r1 for i in range (c1)]
for i in range(c1):
    for j in range(r1):
        mat[i][j]=x[j][i]
# for i in mat:
#     for j in i[:-1]:
#         print(j,end=',')
#     print(i[-1])

for i in mat:
     print(*i,sep=', ')











#1 2,3 4,5 6