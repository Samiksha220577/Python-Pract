x=[list(map(int,i.split()))for i in input().split(',')]
print('matrix-1')
for i in x:
    print(i)
y=[list(map(int,i.split()))for i in input().split(',')]
print('matrix-2')
for i in y:
    print(i)



for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            print(x[i][k]*y[k][j])

