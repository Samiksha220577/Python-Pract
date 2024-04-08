matrix=[list(map(int,i.split()))for i in input().split(',')]
print('matrix')
for k in range(len(matrix[0])):
    res = [sub[k] for sub in matrix]
    print(res)













#1 2,3 4,5 6