# # Static implementation of linear queue
# front = 0
# rear = 0
# mymax = 5
#
# def createQueue():
#     queue = [] #empty list
#     return queue
#
# def isEmpty(queue):
#     # Return True if the queue is empty.
#     return len(queue) - front == 0
#
# def enqueue(queue,item): # insert an element into the queue
#     if (rear == mymax-1):
#         print("Queue is Full!!")
#     else:
#         queue.insert(rear,item)
#         rear += 1
#
# def dequeue(queue): #remove an element from the queue
#     if (front == rear):
#         print("Queue is Empty!!")
#     else:
#         front += 1
#         return queue[front-1]
#
# # Driver code
# queue = createQueue()
# while True:
#     print("1.Enqueue")
#     print("2.Dequeue")
#     print("3.Display")
#     print("4.Quit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         item = int(input("Enter the item to be inserted: "))
#         enqueue(queue,item)
#     elif choice == 2:
#         print("The dequeued item is: ", dequeue(queue))
#     elif choice == 3:
#         print("Queue: ", queue[front:rear])
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice")
# -------------------------------------------------------------
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
    else:print(queue[::-1])
        # print("Queue elements are:")
        # for i in range(front, rear):
        #     print(queue[i])

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
