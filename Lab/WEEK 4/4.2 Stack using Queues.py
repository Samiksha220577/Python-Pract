# from queue import Queue
#
# class MyStack:
#     def __init__(self):
#         self.q1 = Queue()
#         self.q2 = Queue()
#
#     def push(self, x: int) -> None:
#         self.q2.put(x)
#         while not self.q1.empty():
#             self.q2.put(self.q1.get())
#         self.q1, self.q2 = self.q2, self.q1
#
#     def pop(self) -> int:
#         if self.q1.empty():
#             return None
#         return self.q1.get()
#
#     def top(self) -> int:
#         if self.q1.empty():
#             return None
#         return self.q1.queue[0]
#
#     def empty(self) -> bool:
#         return self.q1.empty()
#
# # Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())  # returns 2
# print(obj.pop())  # returns 2
# print(obj.empty())  # returns False
# ----------------------------------
# class MyStack:
#
#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []
#
#     def push(self, x: int) -> None:
#         # Move all elements from queue1 to queue2
#         while self.queue1:
#             self.queue2.append(self.queue1.pop(0))
#         # Add the new element to queue1
#         self.queue1.append(x)
#         # Move all elements back to queue1
#         while self.queue2:
#             self.queue1.append(self.queue2.pop(0))
#
#     def pop(self) -> int:
#         return self.queue1.pop(0)
#
#     def top(self) -> int:
#         return self.queue1[0]
#
#     def empty(self) -> bool:
#         return len(self.queue1) == 0
#
# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()
#
# -----------------------------
# Static implementation of linear queue
front = 0
rear = 0
mymax = 5

# Function to create a queue
def createQueue():
    return []  # empty list

# Function to check if the queue is empty
def isEmpty(queue):
    return len(queue) == 0

# Function to add an element to the queue
def enqueue(queue, item):
    global rear
    if rear < mymax:
        queue.append(item)
        rear += 1
    else:
        print("Queue is full")

# Function to remove an element from the queue
def dequeue(queue):
    global front
    if isEmpty(queue):
        print("Queue is empty")
    else:
        item = queue.pop(0)
        front += 1
        return item

# Function to display the queue
def display(queue):
    if isEmpty(queue):
        print("Queue is empty")
    else:
        print("Queue elements are:")
        for i in range(front, rear):
            print(queue[i])

# Driver code
queue = createQueue()
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the element to be inserted: "))
        enqueue(queue, item)
    elif choice == 2:
        dequeued_item = dequeue(queue)
        if dequeued_item is not None:
            print(f"Dequeued element is {dequeued_item}")
    elif choice == 3:
        display(queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
# ---------------------------------------------------
length=int(input())
ope=list(map(str, input().split(', ')))
num=list(map(str, input().split(', ')))
list1=[]
for i in range(len(ope)):
    if ope[i]=='add':
        if (len(list1)==length):
            print('queue is full')
        else:
            list1.append(num[i])
    elif ope[i]=='size':
        print(len(list1))
    elif ope[i]=='pop':
        list1.pop()
    elif ope[i]=='print':
        z=[]
        for i in range(len(list1)):
            z.append(list1.pop())
        for j in z:
            print(j,end=' ')
