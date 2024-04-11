# list=[1,2,3,4,5,6,7,8,9]
# print(list)
# # n=int(input('enter target:')
# n=10
# listx=[]
# for i in list:
#     for j in list:
#         if (i+j)==n :
#             listx.append((i,j))
#             # print(i,j)
# my_list = [tuple(sorted(s)) for s in listx]
#
# print(set(my_list))
# ------------------------------------------
nums = list(map(int, input().split()))
target = int(input())

def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

result = twoSum(nums, target)
if result:
    for i in result:
        print(i, end="")
else:
    print("No two sum solution")
# ---------------------------------------
# nums=list(map(int,input().split()))
# target=int(input())
#
# def twoSum(nums, target):
#     for i in nums:
#         for j in nums:
#             if nums[i]+nums[j] == target:
#                 return [i,j]
# result=twoSum(nums, target)
# print(result)
# for i in result:
#     print(i,end="")