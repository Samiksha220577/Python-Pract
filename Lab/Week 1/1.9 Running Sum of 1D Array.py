# inp=input("Enter numbers seperated by space")
# nums=inp.split()
# list = [int(num) for num in nums]
# print(list)
# sum=0
# x=[]
# for i in list:
#     sum=sum+i
#     x.append(sum)
# print(x)
# ------------------------------------
# reinprep
inp=list(map(int,input().split(',')))
sum=0
x=[]
for i in inp:
    sum=sum+i
    x.append(sum)
print(*x,sep=', ')


