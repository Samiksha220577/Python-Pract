#adjacency matrix non directed non weighted
nv=int(input('enter no of vertices'))
ne=int(input('enter number of edges'))
vertices=[]
for i in range (nv):
    v=int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges=[]
for i in range (ne):
    e=tuple(map(int,input('enter edges').split()))
    edges.append(e)
print(edges)

adj_mat=[[0]*nv for x in range (nv)]
# print (adj_mat)
for e in edges:
    adj_mat[e[0]][e[1]]=1
    adj_mat[e[1]][e[0]]=1
    v1,v2=e
    # adj_mat[v1][v2]=1
    # adj_mat[v2][v1]=1
    # adj_mat[vertices.index(v1)][vertices.index(v2)]+=1
    # adj_mat[vertices.index(v2)][vertices.index(v1)] += 1
print(adj_mat)
for j in adj_mat:
    print(j)


#adjacency matrix directed
nv = int(input('enter no of vertices'))
ne = int(input('enter number of edges'))
vertices = []
for i in range(nv):
    v = int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    e = tuple(map(int, input('enter edges').split()))
    edges.append(e)
print(edges)

adj_mat = [[0] * nv for x in range(nv)]
# print (adj_mat)
for e in edges:
    adj_mat[e[0]][e[1]] = 1

    v1, v2 = e
    # adj_mat[v1][v2]=1
    # adj_mat[v2][v1]=1
    # adj_mat[vertices.index(v1)][vertices.index(v2)]+=1
    # adj_mat[vertices.index(v2)][vertices.index(v1)] += 1
print(adj_mat)
for j in adj_mat:
    print(j)

#adjacency matrix weighted
nv = int(input("Enter the number of vertices: "))
ne = int(input("Enter the number of edges: "))

# Create a list of vertices
vertices = []
for i in range(nv):
    v = input("Enter vertex {}: ".format(i+1))
    vertices.append(v)

# Create a list of edges with weights
edges = []
for i in range(ne):
    edge = tuple(input("Enter edge {} and its weight: ".format(i+1)).split())
    edges.append((edge[0], edge[1], int(edge[2])))

# Create an adjacency matrix with weights
adj_matrix = [[0]*nv for _ in range(nv)]

# Populate the adjacency matrix with weights
for edge in edges:
    v1, v2, weight = edge
    i1 = vertices.index(v1)
    i2 = vertices.index(v2)
    adj_matrix[i1][i2] = weight
    adj_matrix[i2][i1] = weight

# Print the adjacency matrix with weights
for row in adj_matrix:
    print(row)
##

nv=int(input("enter number of vertices"))
ne=int(input("enter number of edges"))
vertices=[]
for i in range(nv):
    v=int(input("enter the vertices"))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    edge=tuple(map(int, input("enter an edge").split()))
    edges.append(edge)
print(edges)
adj_mat=[[0]*nv for x in range(nv)]
for e in edges:
    v1, v2= e
    if v1==v2:
        adj_mat[vertices.index(v1)][vertices.index(v2)]+=1
    else:
        adj_mat[vertices.index(v1)][vertices.index(v2)]+=1
        adj_mat[vertices.index(v2)][vertices.index(v1)]+=1
for j in adj_mat:
    print(j)

