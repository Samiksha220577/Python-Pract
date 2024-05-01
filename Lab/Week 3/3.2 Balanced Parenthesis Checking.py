#
# # Check for balanced parentheses in an expression
# open_list = ["[","{","("]
# close_list = ["]","}",")"]
# inp=input()
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for char in myStr:
#         if char in open_list:
#             stack.append(char)
#         elif char in close_list:
#             if not stack or close_list.index(char) != open_list.index(stack.pop()):#if not stack checks if stack is empty
#                 return "Unbalanced"
#     return "Balanced" if not stack else "Unbalanced"
#
# # Test cases
# print(check(inp))
# ____________________________________________________________
# Python3 code to Check for
# balanced parentheses in an expression
# open_list = ["[","{","("]
# close_list = ["]","}",")"]
#
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"
#
#
# # Driver code
# string = "{[]{()}}"
# print(string,"-", check(string))
#
# string = "[{}{})(]"
# print(string,"-", check(string))
#
# string = "((()"
# print(string,"-",check(string))
# ------------------------------------------------
# exp=input()
# stack=[]
# for i in exp:
#     if i in '{([' or not stack:
#         stack.append(i)
#
#     else:
#         if (i==')'and stack[-1]=='(')or(i==']' and stack[-1]=='[')or(i=='}' and stack[-1]=='{'):
#             stack.pop()
#
#
# print('unbalanced') if stack else print('balanced')
# ----------------------------------------------------
