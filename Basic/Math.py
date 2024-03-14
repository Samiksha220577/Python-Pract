def create_incidence_matrix(vertices, edges):
    matrix = [[0]*len(edges) for _ in range(len(vertices))]
    for i, edge in enumerate(edges):
        v1, v2 = edge
        matrix[vertices.index(v1)][i] = 1
        matrix[vertices.index(v2)][i] = 1
    return matrix



vertices = []
for i in range(int(input('enter no of vertices'))):
    v = int(input('enter vertex'))
    vertices.append(v)

edges = []
for i in range(int(input('enter number of edges'))):
    e = tuple(map(int, input('enter edge').split()))
    edges.append(e)

matrix = create_incidence_matrix(vertices, edges)
print(matrix)