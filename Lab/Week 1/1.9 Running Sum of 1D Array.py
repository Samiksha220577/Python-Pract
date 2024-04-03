inp=input("Enter numbers seperated by space")
nums=inp.split()
list = [int(num) for num in nums]
print(list)
sum=0
x=[]
for i in list:
    sum=sum+i
    x.append(sum)
print(x)