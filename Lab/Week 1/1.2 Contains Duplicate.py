#
# x=input("enter elements")
# numbers = x.split()
# count=0
# list = [int(num) for num in numbers]
# z=len(list)
# x=set(list)
# print(x)
# k=len(x)
# if z==k:
#     print("false")
# else:
#     print("true")
# x= list(map(int,input().split(',')))
# print(x)
# -------------------------------------------------
# reinprep
nums=list(map(int,input().split(',')))
count=0
x=set(nums)
if len(nums)==len(x):
    print('false')
else:
    print('true')