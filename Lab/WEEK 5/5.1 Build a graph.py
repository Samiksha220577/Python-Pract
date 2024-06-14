# nv, ne = map(int, input("Enter number of vertices and edges (separated by comma): ").split(','))
# print(nv,ne)
# edges=[]
# for i in range(ne):
#     edge=list(map(int, input("Enter edges,seperated by comma: ").split(',')))
#     edges.append(edge)
# # for edge in edges:
#
# # print(edges)
# # ADJACENCY MATRIX
# adj_mat=[[0]*nv for x in range (nv)]
# # print (adj_mat)
# for e in edges:
#     adj_mat[e[0]][e[1]]=1
#     adj_mat[e[1]][e[0]]=1
#     v1,v2=e
#
# # print(adj_mat)
# for j in adj_mat:
#     for i in j[:-1]:
#         print(i,end=", ")
#     print(j[-1])
# # ADJACENCY LIST
#
# # ADJACENCY LIST
# # adj_list = [[] for _ in range(nv)]  #adj_list = [[], [], [], [], []]
# # for e in edges:
# #     adj_list[e[0]].append(e[1])
# #     adj_list[e[1]].append(e[0])
# adj_list = {v:[] for v in range(nv)}
# for v1,v2 in edges:
#     adj_list[v1].append(v2)
#     adj_list[v2].append(v1)
#
#
# print("Adjacency List:")
# for i in range(nv):
#     print("Vertex", i, ":", adj_list[i])
# ---------------------------------------------
# def create_adjacency_list(vertices, edges):
#     # Initialize an empty adjacency list
#     adjacency_list = [[] for _ in range(vertices)]
#
#     # Populate the adjacency list based on the edges
#     for _ in range(edges):
#         u, v = map(int, input().split())
#         adjacency_list[u].append(v)
#         adjacency_list[v].append(u)  # Since it's an undirected graph
#
#     return adjacency_list
#
# def main():
#     # Input: Number of vertices and edges
#     vertices, edges = map(int, input().split())
#
#     # Create the adjacency list
#     adjacency_list = create_adjacency_list(vertices, edges)
#
#     # Output: Adjacency Matrix
#     print("Adjacency Matrix")
#     for row in adjacency_list:
#         print(*row)
#
#     # Output: Adjacency List
#     print("Adjacency List")
#     for vertex, neighbors in enumerate(adjacency_list):
#         print(f"{vertex}: {', '.join(map(str, neighbors))}")
#
# if __name__ == "__main__":
#     main()
# #
# ---------------------------------------------
# nv, ne = map(int, input("Enter number of vertices and edges (separated by comma): ").split(','))
# print(nv, ne)
#
# edges = []
# for i in range(ne):
#     edge = list(map(int, input("Enter edges, separated by comma: ").split(',')))
#     edges.append(edge)
#
# # ADJACENCY MATRIX
# # adj_mat = {i: {j: 1 if (i, j) in edges or (j, i) in edges else 0 for j in range(nv)} for i in range(nv)}
# adj_mat = [[1 if [i, j] in edges or [j, i] in edges else 0 for j in range(nv)] for i in range(nv)]
# print("Adjacency Matrix:")
# # for i in range(nv):
# #     for j in range(nv):
# #         print(adj_mat[i][j], end=", ")
# #     print()
# for j in adj_mat:
#     for i in j[:-1]:
#         print(i,end=", ")
#     print(j[-1])
#
# # ADJACENCY LIST
# adj_list = {v: [] for v in range(nv)}
# for v1, v2 in edges:
#     adj_list[v1].append(v2)
#     adj_list[v2].append(v1)

# print("Adjacency List:")
# for i in range(nv):
#     print("Vertex", i, ":", adj_list[i])
# ------------------------------
nv, ne = map(int, input().split(','))


edges = []
for i in range(ne):
    edge = list(map(int, input().split(',')))
    edges.append(edge)

# ADJACENCY MATRIX
adj_mat = [[1 if [i, j] in edges or [j, i] in edges else 0 for j in range(nv)] for i in range(nv)]
print("Adjacency Matrix")
for j in adj_mat:
    for i in j[:-1]:
        print(i,end=", ")
    print(j[-1])

# ADJACENCY LIST
adj_list = {v: [] for v in range(nv)}
for v1, v2 in edges:
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

print("Adjacency List")
for i in range(nv):
    print( i, ":", list(set(sorted(adj_list[i]))))