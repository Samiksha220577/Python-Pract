# inp=input("Enter number")
# nums=inp.split()
# list = [int(num) for num in nums]
# # print(list)
#
#
#
# # list=[1,2,3]
# s=''
# for i in list:
#     s+=str(i)#in string 1+2=12
# x=int(s)
# z=x+1
# # print(z)
#
#
# dig=[]
# while z>0:
#     dig.append(z%10)
#     z//=10
#
# print(dig[::-1])
# ------------------------------------------

# def plus_one(digits):
#     n=len(digits)
#     for i in range(n-1,-1,-1):
#         digits[i]+=1
#         if digits[i]==10:
#             digits[i]=0
#         else:break
#         if digits[0]==0:
#             digits.insert(0,1)
#     return digits
# digits=list(map(int,input().split()))
# result=plus_one(digits)
# print(result)
# print(*result,sep=", ")
# --------------------------------------------
# reinprep
inp=input()
nums=inp.split(',')
list = [int(num) for num in nums]
# print(list)



# list=[1,2,3]
s=''
for i in list:
    s+=str(i)#in string 1+2=12
x=int(s)
z=x+1
# print(z)


dig=[]
while z>0:
    dig.append(z%10)
    z//=10

print(*dig[::-1],sep=', ')
