inp=input("Enter number")
nums=inp.split()
list = [int(num) for num in nums]
print(list)



# list=[1,2,3]
s=''
for i in list:
    s+=str(i)#in string 1+2=12
x=int(s)
z=x+1
print(z)


dig=[]
while z>0:
    dig.append(z%10)
    z//=10

print(dig[::-1])