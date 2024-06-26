# # def adjacency_list(n, edges):
# #     adjacency = {i: [] for i in range(n)}
# #     for i in edges:
# #         v1, v2 = i
# #         adjacency[v1].append(v2)
# #         adjacency[v2].append(v1)  # Add this line to make the graph undirected
# #     return adjacency
# #
# # def dfs(visited, adjacency, node):
# #     stack = [node]
# #     while stack:
# #         vertex = stack.pop()
# #         if vertex not in visited:
# #             visited.append(vertex)
# #             print(vertex, end=' ')
# #         for neighbor in sorted(adjacency[vertex], reverse=True):
# #             if neighbor not in visited:
# #                 stack.append(neighbor)
# #
# # n, e = list(map(int, input().split(' ')))
# # edges = []
# # for i in range(e):
# #     edge = tuple(map(int, input().split(' ')))
# #     edges.append(edge)
# # visited = []
# # start = int(input())
# # adjacency = adjacency_list(n, edges)
# # dfs(visited, adjacency, start)
# #
# #
# # # test cases
# # # <input type="hidden" id="ts_i_0" value="4 6
# # # 0 1
# # # 0 2
# # # 1 2
# # # 2 0
# # # 2 3
# # # 3 3
# # # 1" hidden="">
# # # <input type="hidden" id="ts_o_0" value="1 2 0 3
# # # " hidden="">
# # # <input type="hidden" id="ts_i_1" value="4 6
# # # 2 0
# # # 0 2
# # # 1 2
# # # 0 1
# # # 3 3
# # # 1 3
# # # 2" hidden="">
# # # <input type="hidden" id="ts_o_1" value="2 0 1 3" hidden="">
# # # <input type="hidden" id="ts_i_2" value="5 5
# # # 0 1
# # # 0 2
# # # 1 3
# # # 1 4
# # # 3 4
# # # 0" hidden="">
# # # <input type="hidden" id="ts_o_2" value="0 1 3 4 2" hidden="">
# # # <input type="hidden" id="ts_i_3" value="3 2
# # # 0 1
# # # 1 2
# # # 0" hidden="">
# # # <input type="hidden" id="ts_o_3" value="0 1 2
# # # " hidden="">
# # # <input type="hidden" id="ts_i_4" value="6 7
# # # 0 1
# # # 0 2
# # # 1 3
# # # 3 4
# # # 4 5
# # # 2 4
# # # 5 1
# # # 0" hidden="">
# # # <input type="hidden" id="ts_o_4" value="0 1 3 4 5 2
# # # " hidden="">
# # ---------------------------------
# # def adjacency_list(n, edges):
# #     adjacency = {i: [] for i in range(n)}
# #     for v1, v2 in edges:
# #         adjacency[v1].append(v2)
# #         adjacency[v2].append(v1)  # Make the graph undirected
# #     return adjacency
# #
# # def dfs(visited, adjacency, node):
# #     stack = [node]
# #     while stack:
# #         vertex = stack.pop()
# #         if vertex not in visited:
# #             visited.append(vertex)
# #             print(vertex, end=' ')
# #         for neighbor in sorted(adjacency[vertex], reverse=True):
# #             if neighbor not in visited:
# #                 stack.append(neighbor)
# #
# # n, e = list(map(int, input().split()))
# # edges = [tuple(map(int, input().split())) for _ in range(e)]
# # start = int(input())
# # adjacency = adjacency_list(n, edges)
# # dfs([], adjacency, start)
# # Python3 program to print DFS traversal
# # from a given graph
# from collections import defaultdict
#
#
# # This class represents a directed graph using
# # adjacency list representation
# class Graph:
#
#     # Constructor
#     def __init__(self):
#
#         # Default dictionary to store graph
#         self.graph = defaultdict(list)
#
#     # Function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     # A function used by DFS
#     def DFSUtil(self, v, visited):
#
#         # Mark the current node as visited
#         # and print it
#         visited.add(v)
#         print(v, end=' ')
#
#         # Recur for all the vertices
#         # adjacent to this vertex
#         for neighbour in self.graph[v]:
#             if neighbour not in visited:
#                 self.DFSUtil(neighbour, visited)
#
#     # The function to do DFS traversal. It uses
#     # recursive DFSUtil()
#     def DFS(self, v):
#
#         # Create a set to store visited vertices
#         visited = set()
#
#         # Call the recursive helper function
#         # to print DFS traversal
#         self.DFSUtil(v, visited)
#
#
# # Driver's code
# if __name__ == "__main__":
#     n, e = list(map(int, input().split()))
#     g = Graph()
#     for _ in range(e):
#         u, v = list(map(int, input().split()))
#         g.addEdge(u, v)
#     start = int(input())
#     print("Following is Depth First Traversal (starting from vertex {})".format(start))
#     g.DFS(start)
# ----------------------------
# nv, ne = map(int,input().split(' '))
# edges=[]
# el = list(map(str, input().split(' ')))
# for i in range(len(el)):
#     k=[]
#     for j in el[i]:
#         if j.isdigit():
#             k.append(int(j))
#     edges.append(k)
# adj_list={v:[] for v in range(nv)}
# for v1,v2 in edges:
#     adj_list[v1].append(v2)
# vertex=0
# for i in range(len(adj_list)):
#     if len(adj_list[i])%2 == 1:
#         vertex = i
#         break
# visited=list()
# visited.append(vertex)
# n=int(input())
# while(n<nv+1):
#     for i in adj_list[vertex]:
#         if i not in visited:
#             vertex = i
#             visited.append(vertex)
#             n=n+1
#         for i in visited[:-1]:
#             print(i, end=' ')
#         print(visited[-1], end='')
# ----------------------------
# nv, ne = map(int, input('enter no of vertices and edges').split())
# edges = []
# for _ in range(ne):
#     edges.append(list(map(int, input('enter edge').split())))
# adj_list = {v: [] for v in range(nv)}
# for v1, v2 in edges:
#     adj_list[v1].append(v2)
# vertex = 0
# for i in range(len(adj_list)):
#     if len(adj_list[i]) % 2 == 1:
#         vertex = i
#         break
# visited = [vertex]
# n = int(input('enter start vertex'))
# while n < nv + 1:
#     for i in adj_list[vertex]:
#         if i not in visited:
#             vertex = i
#             visited.append(vertex)
#             n += 1
#             break
# for i in visited:
#     print(i, end=' ')
# ----------------------------
nv, ne = map(int, input('Enter the number of vertices and edges: ').split())
edges = []
for _ in range(ne):
    edges.append(list(map(int, input('Enter edge: ').split())))
adj_list = {v: [] for v in range(nv)}
for v1, v2 in edges:
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

start_vertex = int(input('Enter the start vertex: '))

visited = set()
stack = [start_vertex]
while stack:
    vertex = stack.pop()
    if vertex not in visited:
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in sorted(adj_list[vertex], reverse=True):
            if neighbor not in visited:
                stack.append(neighbor)