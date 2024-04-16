exp=input().split()
stack=[]
operators=['+','-','*','/']
for i in exp:
    if i not in operators:
        stack.append(i)
    if i in operators:
        num=int(stack.pop())
        n=int(stack.pop())
        if i =='+':
            stack.append(n+num)
        elif i =='-':
            stack.append(n-num)
        elif i =='*':
            stack.append(n*num)
        elif i =='/':
            stack.append(n/num)
print(stack[0])