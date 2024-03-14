nv=int(input("enter number of vertices"))
ne=int(input("enter number of edges"))
vertices=[]
for i in range(nv):
    v=input("enter the vertices")
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    edge=tuple(input("enter an edge").split())
    w=tuple(input("enter weight"))
    edges.append(edge,w)
print(edges)
adj_list={ver:[] for ver in vertices}
for e in edges:
    v1,v2=e
    adj_list[v1].append(v2,w)
    adj_list[v2].append(v1,w)
print(adj_list)