
# lst = []
#
# n = int(input("Enter number of elements : "))
#
# for i in range(0, n):
#     ele = int(input())
#     lst.append(ele)
#
# print(lst)
#
# x = int(input("Enter number: "))
# def search(lst, x):
#     for i in range(len(lst)):
#         if lst[i] == x:
#             print("Number present")
#             break
#     else:
#         print("Number not present")
#
# search(lst, x)
#------------------------------------------------
# arr=[]
# n=int(input("Enter number of"))
# for i in range(0,n):
#     ele=int(input("Enter no"))
#     arr.append(ele)
# print(arr)
#
# x=int(input("no to be found"))
# def search(arr, x):
#     for i in range(len(arr)):
#
#         if arr[i] == x:
#             return i
#
#     return -1
# result=search(arr, x)
# if result != -1:
#     print("present")
# else:
#     print("not present")
#

#-------------------------------------------------------
#binary search
# arr=[1,2,3,4,5,6,7,8,9]
# target=int(input("Enter the"))
# def binarysearch(arr,target):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return 1
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# result=binarysearch(arr,target)
# if result!=-1:
#     print("found")
# else:
#     print("not found")
#________________________________________________
