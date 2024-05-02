x=[list(map(int,i.split()))for i in input().split(',')]
print('matrix-1')
for i in x:
    print(i)
y=[list(map(int,i.split()))for i in input().split(',')]
print('matrix-2')
for i in y:
    print(i)
print()

pro = [[0] * len(y[0]) for _ in range(len(x))]
# for i in pro:
#     print(i)

# iterate through rows of X
for i in range(len(x)):
   # iterate through columns of Y
   for j in range(len(y[0])):
        # iterate through rows of Y
       for k in range(len(y)):
           pro[i][j] += x[i][k] * y[k][j]

for r in pro:
    print(r)

# 1 2 3,4 5 6
# 10 11,20 21,30 31
# --------------------------------
x=[]
[r1,c1]=list(map(int,input().split(',')))
for i in range(r1):
    u=list(map(int,input().split(',')))
    x.append(u)
print(x)
y=[]
[r2,c2]=list(map(int,input().split(',')))
for i in range(r2):
    v=list(map(int,input().split(',')))
    y.append(v)
row1=len(x)
col1=len(x[0])
row2=len(y)
col2=len(y[0])
if col1==row2:
    prod=[[0]*col2 for i in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                prod[i][j]+=x[i][k]*y[k][j]
print(prod)
# 3,3
# 1,7,3
# 3,5,6
# 6,8,9
# 3,4
# 1,1,1,2
# 6,7,3,0
# 4,5,9,1








