front = 0
rear = 0

# Get the maximum size of the queue from the user
mymax = int(input())


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


def size(queue):
    x = len(queue)
    print(x)


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
        print(*queue, sep=' ')
        # print(queue[0::])
        # print("Queue elements are:")
        # for i in range(front, rear):
        #     print(queue[i])


# Driver code
queue = createQueue()

values = input()
cmd = values.split(",")
# print('List : ', cmd)
# print(cmd)

val = input()
inp = val.split(",")
# print('List : ', cmd)
# print(inp)

queue = createQueue()  # Create an empty queue

i=0
while i < mymax:
    # print('index',i)
    elem = cmd[i]
    # print('elem',elem)


# print('end loop 1')

# for elem in cmd:
#     # print (cmd.index(elem))
    if elem == "add":
        # print(inp[i])
        item = inp[i]
        add(queue, item)
    elif elem == "size":
        print(len(queue))
    elif elem == "dequeue":
        dequeued_item = dequeue(queue)

    elif elem == "print":
        display(queue)
    else:
        print("Invalid command")
    i = i + 1