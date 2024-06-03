lst=[1,2,3,4,5,6,7,8]
x=[]
for i in range(len(lst)):
    x.append(lst.pop())

# print(x)
for j in x:
    print(j, end=' ')