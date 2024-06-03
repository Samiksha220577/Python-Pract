# lst=list(map(str, input().split(',')))
# z=[]
# for i in lst:
#     for j in range(lst.index(i)+1,len(lst)):
#         # print(i,lst[j])
#         if i>lst[j]:
#             z.append(lst[j])
#
#         else:
#             z.append('-1')
# print(z)
# -----------------------------------------
def next_greater_element(arr):
    nge = [-1] * len(arr)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                nge[i] = arr[j]
                break

    return nge

arr = list(map(int, input().split(',')))
result = next_greater_element(arr)
print(', '.join(map(str, result)))