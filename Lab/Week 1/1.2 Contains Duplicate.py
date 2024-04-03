
x=input("enter elements")
numbers = x.split()
count=0
list = [int(num) for num in numbers]
z=len(list)
x=set(list)
print(x)
k=len(x)
if z==k:
    print("false")
else:
    print("true")
