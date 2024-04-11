# inp=input("Enter numbers seperated by space")
# nums=inp.split()
# list = [int(num) for num in nums]
# print(list)
# x=int(input("Enter numer"))
# for i in list:
#     list.remove(x)
# print(list)




num=list(map(int,input().split()))
val=int(input())
l1=[]
l2=[]
l3=[]
for i in range(len(num)):
    if num[i]==val:
        l2.append("_")
    else:
        l1.append(num[i])
l3=l1+l2
print(str(len(l1)))