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









