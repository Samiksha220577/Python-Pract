# import sys
# import heapq
#
# def prim(graph, start):
#     mst = []
#     visited = set()
#     edges = [(cost, start, to) for to, cost in graph[start].items()]
#     heapq.heapify(edges)
#
#     while edges:
#         cost, frm, to = heapq.heappop(edges)
#         if to not in visited:
#             visited.add(to)
#             mst.append((frm, to, cost))
#             for to_next, cost2 in graph[to].items():
#                 if to_next not in visited:
#                     heapq.heappush(edges, (cost2, to, to_next))
#
#     return mst
#
# def main():
#     num_vertices, num_edges = map(int, input().split())
#     graph = {i: {} for i in range(num_vertices)}
#
#     for _ in range(num_edges):
#         cost, frm, to = map(int, input().split())
#         graph[frm][to] = cost
#         graph[to][frm] = cost
#
#     mst = prim(graph, 0)
#     total_cost = sum(cost for _, _, cost in mst)
#     print("The final structure of the MST is as follows and the weight of the edges of the MST is", total_cost)
#     for frm, to, cost in mst:
#         print(f"Edge Weight {frm} - {to} {cost}")
#
# if __name__ == "__main__":
#     main()
#
# # --------------------------------------------------------------------
# # A Python3 program for
# # Prim's Minimum Spanning Tree (MST) algorithm.
# # The program is for adjacency matrix
# # representation of the graph
#
# # Library for INT_MAX
# import sys
#
#
# class Graph():
# 	def __init__(self, vertices):
# 		self.V = vertices
# 		self.graph = [[0 for column in range(vertices)]
# 					for row in range(vertices)]
#
# 	# A utility function to print
# 	# the constructed MST stored in parent[]
# 	def printMST(self, parent):
# 		print("Edge \tWeight")
# 		for i in range(1, self.V):
# 			print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
#
# 	# A utility function to find the vertex with
# 	# minimum distance value, from the set of vertices
# 	# not yet included in shortest path tree
# 	def minKey(self, key, mstSet):
#
# 		# Initialize min value
# 		min = sys.maxsize
#
# 		for v in range(self.V):
# 			if key[v] < min and mstSet[v] == False:
# 				min = key[v]
# 				min_index = v
#
# 		return min_index
#
# 	# Function to construct and print MST for a graph
# 	# represented using adjacency matrix representation
# 	def primMST(self):
#
# 		# Key values used to pick minimum weight edge in cut
# 		key = [sys.maxsize] * self.V
# 		parent = [None] * self.V # Array to store constructed MST
# 		# Make key 0 so that this vertex is picked as first vertex
# 		key[0] = 0
# 		mstSet = [False] * self.V
#
# 		parent[0] = -1 # First node is always the root of
#
# 		for cout in range(self.V):
#
# 			# Pick the minimum distance vertex from
# 			# the set of vertices not yet processed.
# 			# u is always equal to src in first iteration
# 			u = self.minKey(key, mstSet)
#
# 			# Put the minimum distance vertex in
# 			# the shortest path tree
# 			mstSet[u] = True
#
# 			# Update dist value of the adjacent vertices
# 			# of the picked vertex only if the current
# 			# distance is greater than new distance and
# 			# the vertex in not in the shortest path tree
# 			for v in range(self.V):
#
# 				# graph[u][v] is non zero only for adjacent vertices of m
# 				# mstSet[v] is false for vertices not yet included in MST
# 				# Update the key only if graph[u][v] is smaller than key[v]
# 				if self.graph[u][v] > 0 and mstSet[v] == False \
# 				and key[v] > self.graph[u][v]:
# 					key[v] = self.graph[u][v]
# 					parent[v] = u
#
# 		self.printMST(parent)
#
#
# # Driver's code
# if __name__ == '__main__':
# 	g = Graph(5)
# 	g.graph = [[0, 2, 0, 6, 0],
# 			[2, 0, 3, 8, 5],
# 			[0, 3, 0, 0, 7],
# 			[6, 8, 0, 0, 9],
# 			[0, 5, 7, 9, 0]]
#
# 	g.primMST()
#
#
# # Contributed by Divyanshu Mehta
# # -----------------------------------------------------
# import sys
#
# def prim(graph, start):
#     mst = []
#     visited = set()
#     edges = []
#
#     # Add all edges connected to the starting vertex
#     for to, cost in graph[start].items():
#         edges.append((cost, start, to))
#
#     # Sort edges by weight
#     edges.sort()
#
#     while edges:
#         cost, frm, to = edges.pop(0)
#
#         # Skip if the other endpoint is already visited
#         if to in visited:
#             continue
#
#         # Add the edge to the MST
#         mst.append((frm, to, cost))
#
#         # Add the new vertex to the visited set
#         visited.add(to)
#
#         # Add edges connected to the new vertex
#         for to_next, cost2 in graph[to].items():
#             if to_next not in visited:
#                 edges.append((cost2, to, to_next))
#
#     return mst
#
# def main():
#     # Read input
#     num_vertices, num_edges = map(int, input().split())
#     graph = {i: {} for i in range(num_vertices)}
#
#     for _ in range(num_edges):
#         cost, frm, to = map(int, input().split())
#         graph[frm][to] = cost
#         graph[to][frm] = cost
#
#     # Find the MST
#     mst = prim(graph, 0)
#
#     # Print output
#     total_cost = sum(cost for _, _, cost in mst)
#     print("The final structure of the MST is as follows and the weight of the edges of the MST is", total_cost)
#     for frm, to, cost in mst:
#         print(f"Edge Weight {frm} - {to} {cost}")
#
# if __name__ == "__main__":
#     main()
# --------------------------------------
# import heapq
#
# nv, ne = map(int, input().split(', '))
# edges = []
# for i in range(ne):
#     edge = tuple(map(int, input().split(', ')))
#     edges.append(edge)
#
# adj_list = {v: [] for v in range(nv)}
# for w, v1, v2 in edges:
#     adj_list[v1].append((w, v2))
#     adj_list[v2].append((w, v1))
#
# start = 0
# mst = prim(adj_list, start)
# tot = 0
# for w, v1, v2 in mst:
#     tot += w
# print(tot)
#
#
# def prim(adj_list, start):
#     mst = []
#     visited = set()
#     heap = [(0, start, start)]
#
#     while heap:
#         w, v1, v2 = heapq.heappop(heap)
#         if v2 not in visited:
#             visited.add(v2)
#             mst.append((w, v1, v2))
#             for w, n in adj_list[v2]:
#                 if n not in visited:
#                     heapq.heappush(heap, (w, v2, n))
#     return mst
# -----------------------------------------------------------
import heapq

nv, ne = map(int, input().split(', '))
edges = []
for i in range(ne):
    edge = tuple(map(int, input().split(', ')))
    edges.append(edge)

adj_list = {v: [] for v in range(nv)}
for w, v1, v2 in edges:
    adj_list[v1].append((w, v2))
    adj_list[v2].append((w, v1))
print(adj_list)
def prim(adj_list, start):
    mst = []
    visited = set()
    heap = [(0, start, start)]

    while heap:
        w, v1, v2 = heapq.heappop(heap)

        if v2 not in visited:
            visited.add(v2)
            mst.append((w, v1, v2))
            for w, n in adj_list[v2]:
                if n not in visited:
                    heapq.heappush(heap, (w, v2, n))
    return mst
start = 0
mst = prim(adj_list, start)
tot = 0
for w, v1, v2 in mst:
    tot += w
print(tot)


