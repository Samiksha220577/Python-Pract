# list=[1,2,3,4,5,6,7,8,9]
# print(list)
# n=int(input('enter target:'))
# for i in list:
#     for j in list:
#         if (i+j)==n:
#             print(i,j)



list=[1,2,3,4,5,6,7,8,9]
print(list)
n=int(input('enter target:'))
lst=[]
for i in list:
    for j in list:
        if (i+j)==n:
            print(i,j)

