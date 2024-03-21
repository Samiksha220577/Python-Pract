

# --------------------------------------------------------

a=[1,2,3,4,5,6,7,8]
print(a)
target=int(input("Enter target"))
def binary(a,target):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if target==a[mid]:
            return 1
        elif a[mid]>target:
            low=mid+1
        else:
            high=mid-1
    return -1
result=binary(a,target)
if result==-1:
    print("found")
else:
    print("not found")
