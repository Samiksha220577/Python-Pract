inp=input("Enter numbers seperated by space")
nums=inp.split()
list = [int(num) for num in nums]
print(list)
x=int(input("Enter numer"))
for i in list:
    list.remove(x)
print(list)