def transpose_graph(graph):
    transpose = {i: [] for i in range(len(graph))}
    for i in range(len(graph)):
        for j in graph[i]:
            transpose[j].append(i)
    return transpose

# Input graph
rng=int(input())
for i in range(rng):
    graph
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: []
}

# Find transpose graph
transpose = transpose_graph(graph)

# Print transpose graph
for i in range(len(transpose)):
    print(i, ":", transpose[i])