import heapq
nv,ne = map(int,input().split(', '))
edges = []
for i in range(ne):
    edge = tuple(map(int,input().split(', ')))
    edges.append(edge)
adj_list = {v:[] for v in range(nv)}
for w, v1, v2 in edges:
    adj_list[v1].append((w,v2))
    adj_list[v2].append((w,v1))

start = 0
mst = prim(adj_list, start)
tot = 0
for e in mst:
    tot += e[0]
print(tot)


def prim(adj_list, start):
    mst = []
    visited = set()
    heap = [(0, start)]

    while heap:
        w, d = heapq.heappop(heap)
        if d not in visited:
            visited.add(d)
            mst.append((w,d))
            for w, n in adj_list[d]:
                if n not in visited:
                    heapq.heappush(heap,(w,n))
    return mst
