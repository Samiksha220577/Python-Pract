# n, m = map(int, input().split())
#
# white_edges = set()
# for i in range(m):
#     u, v = map(int, input().split())
#     white_edges.add((u, v))
#     white_edges.add((v, u))
#
# count = 0
# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         for k in range(j+1, n+1):
#             if ((i, j) in white_edges and (j, k) in white_edges and (i, k) in white_edges) or \
#                ((i, j) not in white_edges and (j, k) not in white_edges and (i, k) not in white_edges):
#                 count += 1
#
# print(count)
#-------------------------
# n, m = map(int, input().split())
#
# white_edges = [0] * (n + 1)
# for i in range(m):
#     u, v = map(int, input().split())
#     white_edges[u] += 1
#     white_edges[v] += 1
#
# count = 0
# # for i in range(1, n + 1):
# #     for j in range(i + 1, n + 1):
# #         if white_edges[i] == white_edges[j]:
# #             count += 1
#
#
# if (
#     # If the edge between i and j is white, and the edge between j and k is white, and the edge between i and k is white
#     (i, j) in white_edges and (j, k) in white_edges and (i, k) in white_edges
# ) or (
#     # Or, if the edge between i and j is not white, and the edge between j and k is not white, and the edge between i and k is not white
#     (i, j) not in white_edges and (j, k) not in white_edges and (i, k) not in white_edges
# ):
#     # If the edges are all the same color, increment the count
#     count += 1
# print(count)
# ----------------------------------------------
# def count_Triplets(A, N):
#     count = 0
#     A.sort()
#     for i in range(N):
#         for j in range(i + 1, N):
#             for k in range(j + 1, N):
#                 if A[i] + A[j] == A[k]:
#                     count = count + 1
#
#     return count
#
#
# A = [1, 2, 3, 4, 5]
# N = 5
# print(count_Triplets(A, N))
# -------------------------------------
# n, m = map(int, input().split())
#
# white_edges = set()
# for i in range(m):
#     u, v = map(int, input().split())
#     white_edges.add((u, v))
#     white_edges.add((v, u))
#
# count = 0
# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         for k in range(j+1, n+1):
#             if ((i, j) in white_edges and (j, k) in white_edges and (i, k) in white_edges) or\
#                ((i, j) not in white_edges and (j, k) not in white_edges and (i, k) not in white_edges):
#                 count += 1
#
# print(count)
# ---------------------------------------------------------
n, m = map(int, input().split())

white_edges = set()
for i in range(m):
    u, v = map(int, input().split())
    white_edges.add((u, v))
    # white_edges.add((v, u))

count = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            print(i,j,k)
            if ((i, j) in white_edges and (j, k) in white_edges and (i, k) in white_edges) or\
               ((i, j) not in white_edges and (j, k) not in white_edges and (i, k) not in white_edges):
                count += 1
                print('count',count)
                print( )

# print(count)
