# Check for balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
    stack = []
    for char in myStr:
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            if not stack or close_list.index(char) != open_list.index(stack.pop()):
                return "Unbalanced"
    return "Balanced" if not stack else "Unbalanced"

# Test cases
print(check("{[]{()}}")) # Balanced
print(check("{{}{}(]")) # Unbalanced