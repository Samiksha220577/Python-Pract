# open_list = ["[","{","("]
# close_list = ["]","}",")"]
# mystring=input()
# print(mystring)
# # def check(mystring):
# for i in open_list:
#     print(i)
# 
# Check for balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
inp=input()
# Function to check parentheses
def check(myStr):
    stack = []
    for char in myStr:
        if char in open_list:
            stack.append(char)
            print(stack)
            print(char)
        elif char in close_list:
            if not stack or close_list.index(char) != open_list.index(stack.pop()):
                return "Unbalanced"
    return "Balanced" if not stack else "Unbalanced"

# Test cases
print(check(inp))

