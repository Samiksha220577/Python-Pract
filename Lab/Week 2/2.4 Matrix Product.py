x=[list(map(int,i.split()))for i in input().split(',')]
print('matrix-1')
for i in x:
    print(i)
pro=1
for row in x:
    for ele in row:
        pro *=ele
print('product',pro)



#1 4 5,7 3,4,46 7 3