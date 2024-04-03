input_str = input("Enter a list of lists of integers separated by commas, where each list is separated by spaces: ")
list_str = input_str.split(',')
print(list_str)
a = [list(map(int, sublist.split())) for sublist in list_str]
print(a)
# sublist_sum = [sum(sublist) for sublist in lists]
# print(sublist_sum)
# print('coustomer',sublist_sum.index(max(sublist_sum))+1,'hax maximum money',max(sublist_sum))




a=[[1,2,3],[2,3,4]]
b=a[0]
print(b)
total1=0
total2=0
for i in b:
    print(i)
    total1+=i
print("total1 is:", total1)
c=a[1]
print(c)
for j in c:
    print(j)
    total2+=j
print("total2 is:",total2)
if total1>total2:
    print("the first counstmer is rich:", total1)
elif total2>total1:
    print("the second counstmer is rich:", total2)
elif total1==total2:
    print("both the coustmers are equally rich:", total1)