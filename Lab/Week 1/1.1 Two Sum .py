list=[1,2,3,4,5,6,7,8,9]
print(list)
# n=int(input('enter target:')
n=10
listx=[]
for i in list:
    for j in list:
        if (i+j)==n :
            listx.append((i,j))
            # print(i,j)
my_list = [tuple(sorted(s)) for s in listx]

print(set(my_list))
