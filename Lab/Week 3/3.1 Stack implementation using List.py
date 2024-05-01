# class Stack:
#     def __init__(self, max_size=5):
#         self.stack = []
#         self.max_size = max_size
#         self.top = -1
#
#     def is_empty(self):
#         return self.top == -1
#
#     def push(self, item):
#         if not self.is_full():
#             self.stack.append(item)
#             self.top += 1
#         else:
#             print("Stack is full. Cannot push.")
#
#     def pop(self):
#         if not self.is_empty():
#             self.top -= 1
#             return self.stack.pop()
#         else:
#             print("Stack is empty. Cannot pop.")
#
#     def is_full(self):
#         return self.top == self.max_size - 1
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[self.top]
#         else:
#             print("Stack is empty. Cannot peek.")
#
#     def display(self):
#         if not self.is_empty():
#             print(self.stack[::-1])
#         else:
#             print("Stack is empty.")
#
# stack = Stack()
# while True:
#     print("1.Push")
#     print("2.Pop")
#     print("3.Display")
#     print("4.Quit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         item = int(input("Enter the item to push: "))
#         stack.push(item)
#     elif choice == 2:
#         stack.pop()
#     elif choice == 3:
#         stack.display()
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice. Please try again.")



# size = int(input("enter size"))
# stack = []
#
# def push(stack, item):
#     if len(stack) == size:
#         print("stack overflow")
#         print(stack)
#     else:
#         stack.append(item)
#         print(stack)
# print(stack)
#
#
# def pop():
#     if len(stack) == 0:
#         print("stack overflow")
#         print(stack)
#     else:
#         stack.pop()
#         print(stack)
#
#
# def display():
#     print(stack)
#
#
# def peek():
#     n = len(stack)
#     print(stack[n - 1])
#     print(stack)
#
# print("menu 1.push 2.pop 3.display 4.peek 5.exit")
# while 1:
#     ch = int(input("enter the choice"))
#     if ch == 1:
#         item = int(input("enter element"))
#         push(stack, item)
#     elif ch == 2:
#         pop()
#     elif ch == 3:
#         display()
#     elif ch == 4:
#         peek()
#     else:
#         print("enter valid input")
#         exit(0)
# -----------------------------------------------
size=int(input())
stack=[]
def push(stack,item):
    if len(stack)==size:
        print('stackoverflow')
        print(stack)
print(stack)

def pop():
    if len(stack)==0:
        print('stackoverflow')
        print(stack)
    else:
        stack.pop()
        print(stack)
def display():
    print(stack)
def peek():
    n=len(stack)
    print(stack[n-1])
    print(stack)
print("menu 1.push 2.pop 3.display 4.peek 5.exit")
while True:
    ch=int(input())
    if ch==1:
        item=int(input("enter element"))
        push(stack,item)
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        peek()
    else:
        print('enter valid input')
        exit(0)