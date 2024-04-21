# class MyQueue:
#
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def push(self, x: int) -> None:
#         # Push the new element to stack1
#         self.stack1.append(x)
#
#     def pop(self) -> int:
#         # If stack2 is empty, move all elements from stack1 to stack2
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         # Pop the top element from stack2
#         return self.stack2.pop()
#
#     def peek(self) -> int:
#         # If stack2 is empty, move all elements from stack1 to stack2
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         # Return the top element of stack2
#         return self.stack2[-1]
#
#     def empty(self) -> bool:
#         # Return true if both stacks are empty, false otherwise
#         return not self.stack1 and not self.stack2
#
# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()
# ------------------------------------------------------------------
# class MyQueue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def push(self, x: int) -> None:
#         while len(self.stack1) != 0:
#             self.stack2.append(self.stack1.pop())
#         self.stack1.append(x)
#         while len(self.stack2) != 0:
#             self.stack1.append(self.stack2.pop())
#
#     def pop(self) -> int:
#         if len(self.stack1) == 0:
#             return None
#         return self.stack1.pop()
#
#     def peek(self) -> int:
#         if len(self.stack1) == 0:
#             return None
#         return self.stack1[-1]
#
#     def empty(self) -> bool:
#         return len(self.stack1) == 0
#
# # Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)
# print(obj.peek())  # returns 1
# print(obj.pop())  # returns 1
# print(obj.empty())  # returns False
# -----------------------------------------

class MyQueue(object):
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
    # Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)
    # Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()
	# Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
	# Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk