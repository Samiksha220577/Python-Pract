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
    edges.append(edge)

print(edges)
inc_mat=[[0]*ne for i in range(nv)]
for e in edges:
    v1,v2=e
    print('e',e)
    print('v1',v1)
    print('v2',v2)
    print('vertex v1',[vertices.index(v1)])
    print('vertex v2',[vertices.index(v2)])
    print('edge',[edges.index(e)])
    print(edges.index(e))
    inc_mat[vertices.index(v1)][edges.index(e)]=1
    print(edges.index(e))
    inc_mat[vertices.index(v2)][edges.index(e)]=1
    print()
for j in inc_mat:
    print(j)
