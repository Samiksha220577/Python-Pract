# input_str = input("Enter a list of lists of integers separated by commas, where each list is separated by spaces: ")
# list_str = input_str.split(',')
# print(list_str)
# lists = [list(map(int, sublist.split())) for sublist in list_str]
# print(lists)
# sublist_sum = [sum(sublist) for sublist in lists]
# print(sublist_sum)
# print('coustomer',sublist_sum.index(max(sublist_sum))+1,'hax maximum money',max(sublist_sum))



li=list(map(str,input().split(",")))
m=[]
for i in li:
    x=list(map(int,i.split()))
    y=sum(x)
    m.append(y)
print(max(m))