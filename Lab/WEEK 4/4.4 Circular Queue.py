# class CircularQueue():
#
#     # constructor
#     def __init__(self, size):  # initializing the class
#         self.size = size
#         # initializing queue with None
#         self.queue = [None for i in range(size)]
#         self.front = self.rear = -1
#
#     def is_full(self):
#         return (self.rear + 1) % self.size == self.front
#
#     def is_empty(self):
#         return self.front == -1
#
#     def enqueue(self, data):
#         if self.is_full():
#             print("Queue is full")
#             return
#         self.rear = (self.rear + 1) % self.size
#         self.queue[self.rear] = data
#         if self.front == -1:
#             self.front = self.rear
#
#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty")
#             return
#         data = self.queue[self.front]
#         if self.front == self.rear:
#             self.front = self.rear = -1
#         else:
#             self.front = (self.front + 1) % self.size
#         return data
#
#     def display(self):
#         if self.is_empty():
#             print("Queue is empty")
#             return
#         print("Queue: ", end="")
#         i = self.front
#         while i != self.rear:
#             print(self.queue[i], end=" ")
#             i = (i + 1) % self.size
#         print(self.queue[i])
#
# # Driver Code
# ob = CircularQueue(5)
# ob.enqueue(14)
# ob.enqueue(22)
# ob.enqueue(13)
# ob.enqueue(-6)
# ob.display()
# print("Deleted value = ", ob.dequeue())
# print("Deleted value = ", ob.dequeue())
# ob.display()
# ob.enqueue(9)
# ob.enqueue(20)
# ob.enqueue(5)
# ob.display()
# --------------------------------------------------------
class CircularQueue():
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [None for _ in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Circular Queue is full\n")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1): # condition for empty queue
            print ("Circular Queue is empty\n")
        elif (self.front == self.rear):
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if(self.front == -1):
            print ("No elements in Circular Queue")
        elif (self.rear >= self.front):
            print("Elements in Circular Queue are:",
                                              end = " ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
        else:
            print ("Elements in Circular Queue are:",
                                               end = " ")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
        print ()

# Driver Code
ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
