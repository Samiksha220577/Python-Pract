nodes=int(input('no of nodes'))
edgesno=int(input('no of edges'))
edges=[]
for i in range(edgesno):
    edge=list(map(int, input("Enter edges,seperated by comma: ").split(',')))
    edges.append(edge)
# for i in edges:
#     print(i)
arr=[]
for v1,v2 in edges:
    # print(v1)
    arr.append(v1)
    set1=set(arr)
    # print(set1)
    x=len(set1)
    # print(x)
syn=nodes-x
print(syn)