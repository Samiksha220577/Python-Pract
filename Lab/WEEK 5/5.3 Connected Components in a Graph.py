def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def count_connected_components(n, e, edges):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        print(u,v)

    visited = {i: False for i in range(1, n+1)}
    count = 0
    for node in range(1, n+1):
        if not visited[node]:
            dfs(graph, visited, node)
            count += 1

    return count

n, e = map(int, input().split())
edges = []
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

print(count_connected_components(n, e, edges))