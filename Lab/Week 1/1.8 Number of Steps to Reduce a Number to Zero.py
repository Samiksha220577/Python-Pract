x=int(input())
count=0
while x>0:
    if(x%2!=0):
        x=x-1
        # print (x)
        count+=1
    else:
        x=x//2
        count+=1

print(count)