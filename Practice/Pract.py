arr=[1,2,3,4,5,6,7,8,9]
target=int(input("Enter the"))
def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return 1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
result=binarysearch(arr,target)
if result!=-1:
    print("found")
else:
    print("not found")