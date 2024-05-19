front = 0
rear = 0
mymax=int(input())

# Function to create a queue
def createQueue():
    return []  # empty list

# Function to check if the queue is empty
def isEmpty(queue):
    return len(queue) == 0

# Function to add an element to the queue
def add(queue, item):
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
def print(queue):
    if isEmpty(queue):
        print("Queue is empty")
    else:print(queue[::-1])
        # print("Queue elements are:")
        # for i in range(front, rear):
        #     print(queue[i])
def size(queue):
    size = 0
    for element in queue:
        size += 1

    print(size)
    # listsize = len(queue)
    # print(listsize)
# Driver code
queue = createQueue()
while True:
    print("1.add")
    print("2.Dequeue")
    print("3.print")
    print("4.size")
    print("5.Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the element to be inserted: "))
        add(queue, item)
    elif choice == 2:
        dequeued_item = dequeue(queue)
        if dequeued_item is not None:
            print(f"Dequeued element is {dequeued_item}")
    elif choice == 3:
        print(queue)
    elif choice == 4:
        size(queue)
    elif choice == 5:
        break
    else:
        print("Invalid choice")
