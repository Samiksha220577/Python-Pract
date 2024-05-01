# exp=input().split()
# stack=[]
# operators=['+','-','*','/']
# for i in exp:
#     if i not in operators:
#         stack.append(i)
#     if i in operators:
#         num=int(stack.pop())
#         n=int(stack.pop())
#         if i =='+':
#             stack.append(n+num)
#         elif i =='-':
#             stack.append(n-num)
#         elif i =='*':
#             stack.append(n*num)
#         elif i =='/':
#             stack.append(n/num)
# print(stack[0])
# -----------------------------------------------------------
# exp = input().split()
# stack = []
# operators = ['+', '-', '*', '/']
# for i in exp:
#     if i not in operators:
#         stack.append(i)
#     if i in operators:
#         num = int(stack.pop())
#         n = int(stack.pop())
#         if i == '+':
#             stack.append(n + num)
#         elif i == '-':
#             stack.append(n - num)
#         elif i == '*':
#             stack.append(n * num)
#         elif i == '/':
#             stack.append(n / num)
# print(stack[0])

# -----------------------------------------------------------
# exp = input().split()
# stack = []
# operators = ['+', '-', '*', '/']
# for i in exp:
#     if i not in operators:
#         stack.append(i)
#     if i in operators:
#         num = float(stack.pop())
#         n = float(stack.pop())
#         if i == '+':
#             stack.append(n + num)
#         elif i == '-':
#             stack.append(n - num)
#         elif i == '*':
#             stack.append(n * num)
#         elif i == '/':
#             stack.append(round((n /round(num,1)),1))
# print(stack[0])
# -----------------------------------------------------------
# exp = input().split()
# stack = []
# operators = ['+', '-', '*', '/']
# for i in exp:
#     if i not in operators:
#         stack.append(i)
#     if i in operators:
#         num =(stack.pop())
#         if isinstance(num, int):
#             num=int(num)
#         elif isinstance(num, float):
#             num=float(num)
#
#         n = (stack.pop())
#         if isinstance(n, int):
#             n = int(n)
#         elif isinstance(n, float):
#             n = float(n)
#
#         if i == '+':
#             stack.append(n + num)
#         elif i == '-':
#             stack.append(n - num)
#         elif i == '*':
#             stack.append(n * num)
#         elif i == '/':
#             stack.append(round((n /round(num,1)),1))
# print(stack[0])
# -----------------------------
exp = input().split()
stack = []
operators = ['+', '-', '*', '/']
for i in exp:
    if i not in operators:
        stack.append(i)
    if i in operators:
        num = int(stack.pop())
        n = int(stack.pop())
        if i == '+':
            stack.append(n + num)
        elif i == '-':
            stack.append(n - num)
        elif i == '*':
            stack.append(n * num)
        elif i == '/':
            stack.append(n / num)
print(round((stack[0]),1))
