v, e = map(int, input("Enter number of vertices and edges (separated by comma): ").split(','))
print(v,e)

input_list = []
for i in range(e):
    x = list(map(int, input("Enter edge details (cost, vertex1, vertex2) separated by space: ").split(',')))
    input_list.append(x)

for i in range(len(input_list)):
    print(input_list[i])