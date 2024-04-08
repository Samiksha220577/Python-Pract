g = {
    'a': ['b', 'c', 'd'],
    'b': ['d', 'a', 'a'],
    'c': ['d', 'b', 'a'],
    'd': ['b', 'c', 'a'],

}
# for k in g:
#     print(k)
# print()
# print(len(g.keys()))
# print()
# print(g.values())
for i in g:
    # print([i],':',g[i],':',len(g[i]))

    print(i, ':', g[i], ':', len(g[i]), ":", end='')
    if len(g[i]) == (len(g.keys()) - 1):
        print('complete')
    else:
        print('not complete')
------------------
cubes = []
for i in range(7):
    cubes.append(i ** 3)
print("cubes of numbers from 0-6:", cubes)
cubes = [i ** 3 for i in range(7)]
print(cubes)

__________________________
list = [(x, y) for x in [10, 30, 50] for y in [20, 40, 60]]
# nested for loop
print(list)
output
[(10, 20), (10, 40), (10, 60), (30, 20), (30, 40), (30, 60), (50, 20), (50, 40), (50, 60)]
------------------------------------------------------------------------------
list = [(x, y) for x in [10, 20, 30] for y in [30, 10, 60] if x != y]
print(list)
[(10, 30), (10, 60), (20, 30), (20, 10), (20, 60), (30, 10), (30, 60)]

-___________________________________________________

list = [1, 2, 3, 4, 5, 6, 7, 8]
for index, i in enumerate(list):
    print(index, i)
output
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
-------
list = [1, 2, 3, 4, 5, 6, 7, 8]
for index, i in enumerate(list):
    print(index, i)
for i in enumerate(list):
    print(i[1])
    # values
    print(i[0])
    # index
___________________________________________________


def add(a, b):
    return a + b


print(add(1, 2))


def dis():
    print('hello')


dis()
_________________________________________________________
nums = [11, 16, 13, 21, 26]

for num in nums:

    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")
    ___________________________________________________________________

num = 7

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
_____________________________________________________________
# adjacency matrix\
nv = int(input('enter no of vertices'))
ne = int(input('enter number of edges'))
vertices = []
for i in range(nv):
    v = int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    e = tuple(map(int, input('enter edges').split()))
    edges.append(e)
print(edges)

_________________________________________________________________________
# adjacency matrix

nv = int(input('enter no of vertices'))
ne = int(input('enter number of edges'))
vertices = []
for i in range(nv):
    v = int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    e = tuple(map(int, input('enter edges').split()))
    edges.append(e)
print(edges)

adj_mat = [[0] * nv for x in range(nv)]
# print (adj_mat)
for e in edges:
    # adj_mat[e[0]][e[1]]=1
    # adj_mat[e[1]][e[0]]=1
    v1, v2 = e
    adj_mat[v1][v2] = 1
    adj_mat[v2][v1] = 1
print(adj_mat)

output
enter
no
of
vertices5
enter
number
of
edges7
enter
vertices0
enter
vertices1
enter
vertices2
enter
vertices3
enter
vertices4
[0, 1, 2, 3, 4]
enter
edges0
1
enter
edges0
2
enter
edges0
3
enter
edges1
2
enter
edges2
3
enter
edges2
4
enter
edges3
4
[(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (2, 4), (3, 4)]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[0, 1, 1, 1, 0], [1, 0, 1, 0, 0], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0]]

_________________________________________________________________________
nv = int(input('enter no of vertices'))
ne = int(input('enter number of edges'))
vertices = []
for i in range(nv):
    v = int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    e = tuple(map(int, input('enter edges').split()))
    edges.append(e)
print(edges)

adj_mat = [[0] * nv for x in range(nv)]
# print (adj_mat)
for e in edges:
    # adj_mat[e[0]][e[1]]=1
    # adj_mat[e[1]][e[0]]=1
    v1, v2 = e
    # adj_mat[v1][v2]=1
    # adj_mat[v2][v1]=1
    adj_mat[vertices.index(v1)][vertices.index(v2)] = 1
    adj_mat[vertices.index(v2)][vertices.index(v1)] = 1
print(adj_mat)
for j in adj_mat:
    print(j)

    output
    "C:\SAMI\Python\Pycharm Project\pythonPract\.venv\Scripts\python.exe" "C:\SAMI\Python\Pycharm Project\pythonPract\Basic.py"
enter
no
of
vertices4
enter
number
of
edges4
enter
vertices1
enter
vertices2
enter
vertices3
enter
vertices4
[1, 2, 3, 4]
enter
edges1
2
enter
edges2
3
enter
edges3
4
enter
edges4
1
[(1, 2), (2, 3), (3, 4), (4, 1)]
[[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
[0, 1, 0, 1]
[1, 0, 1, 0]
[0, 1, 0, 1]
[1, 0, 1, 0]

Process
finished
with exit code 0
_________________________________________________________________________
# weighted adjacency matrixnv = int(input('enter no of vertices'))
ne = int(input('enter number of edges'))
vertices = []
for i in range(nv):
    v = int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    e = tuple(map(int, input('enter edges').split()))
    w = int(input('edge'))
    edges.append((e[0], e[1], w))
print(edges)

adj_mat = [[0] * nv for x in range(nv)]
# print (adj_mat)
for e in edges:
    v1, v2, w = e
    adj_mat[vertices.index(v1)][vertices.index(v2)] = w
    adj_mat[vertices.index(v2)][vertices.index(v1)] = w
print(adj_mat)
for j in adj_mat:
    print(j)

    output
    "C:\SAMI\Python\Pycharm Project\pythonPract\.venv\Scripts\python.exe" "C:\SAMI\Python\Pycharm Project\pythonPract\Math.py"
enter
no
of
vertices5
enter
number
of
edges7
enter
vertices0
enter
vertices1
enter
vertices2
enter
vertices3
enter
vertices4
[0, 1, 2, 3, 4]
enter
edges0
1
edge1
enter
edges0
2
edge5
enter
edges0
3
edge4
enter
edges1
2
edge2
enter
edges2
3
edge3
enter
edges1
4
edge7
enter
edges2
4
edge6
[(0, 1, 1), (0, 2, 5), (0, 3, 4), (1, 2, 2), (2, 3, 3), (1, 4, 7), (2, 4, 6)]
[[0, 1, 5, 4, 0], [1, 0, 2, 0, 7], [5, 2, 0, 3, 6], [4, 0, 3, 0, 0], [0, 7, 6, 0, 0]]
[0, 1, 5, 4, 0]
[1, 0, 2, 0, 7]
[5, 2, 0, 3, 6]
[4, 0, 3, 0, 0]
[0, 7, 6, 0, 0]

Process
finished
with exit code 0
___________________________________________________

##patterns
x = int(input('enter no'))
for i in range(x):
    for j in range(i + 1):
        print('# ', end='')
    print()
output
enter
no4
#
# #
# # #
# # # #
----------------------
x = int(input('enter no'))
for i in range(x):
    for j in range(x - i):
        print('# ', end='')
    print()
    output

enter
no4
# # # #
# # #
# #
#
-------------------------
x = int(input('enter no'))
for i in range(x):
    for j in range(x - i):
        print(j + 1, " ", end='')
    print()
    output
    enter
    no4
1
2
3
4
1
2
3
1
2
1
---------------------
x = int(input('enter no'))
for i in range(x):
    for j in range(i + 1):
        print(j + 1, ' ', end='')
    print()
    output
    enter
    no4
1
1
2
1
2
3
1
2
3
4
--------------------------
x = int(input('enter no'))
for i in range(x):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("# ", end='')

    print()
output
enter
no4
#
# #
# # #
# # # #
--------------
x = int(input('enter no'))
for i in range(x):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(4 - i):
        print("# ", end='')

    print()
    output
enter
no4
# # # #
# # #
# #
#
--------------------------
nv = int(input('enter no of vertices'))
ne = int(input('enter number of edges'))
vertices = []
for i in range(nv):
    v = int(input('enter vertices'))
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    e = tuple(map(int, input('enter edges').split()))
    edges.append(e)
print(edges)

adj_mat = [[0] * nv for x in range(nv)]
# print (adj_mat)
for e in edges:
    adj_mat[e[0]][e[1]] = 1
    adj_mat[e[1]][e[0]] = 1
    v1, v2 = e
    # adj_mat[v1][v2]=1
    # adj_mat[v2][v1]=1
    # adj_mat[vertices.index(v1)][vertices.index(v2)]+=1
    # adj_mat[vertices.index(v2)][vertices.index(v1)] += 1
print(adj_mat)
for j in adj_mat:
    print(j)

output
"C:\SAMI\Python\Pycharm Project\pythonPract\.venv\Scripts\python.exe" "C:\SAMI\Python\Pycharm Project\pythonPract\Math.py"
enter
no
of
vertices4
enter
number
of
edges9
enter
vertices1
enter
vertices2
enter
vertices3
enter
vertices4
[1, 2, 3, 4]
enter
edges1
4
enter
edges1
4
enter
edges1
2
enter
edges1
2
enter
edges1
2
enter
edges2
3
enter
edges2
4
enter
edges3
4
enter
edges3
4
[(1, 4), (1, 4), (1, 2), (1, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 4)]
[[0, 3, 0, 2], [3, 0, 1, 1], [0, 1, 0, 2], [2, 1, 2, 0]]
[0, 3, 0, 2]
[3, 0, 1, 1]
[0, 1, 0, 2]
[2, 1, 2, 0]

Process
finished
with exit code 0
----------------
my_dict = {}

x = int(input("Enter the number of key-value pairs: "))

for i in range(x):
    key = input("Enter the key: ")

    value = input("Enter the value: ")

    my_dict[key] = value

print(my_dict)
for i in range(x):
    key = list(my_dict.keys())[i]
    value = list(my_dict.values())[i]
    print(key, '->', value)
    ------------------
    # eulers circuit non directed
    nv = int(input("enter number of vertices"))
ne = int(input("enter number of edges"))
vertices = []
for i in range(nv):
    v = input("enter the vertices")
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    edge = tuple(input("enter an edge").split())
    edges.append(edge)
print(edges)
adj_list = {ver: [] for ver in vertices}
for e in edges:
    v1, v2 = e
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
print(adj_list)

--------------------------
# eulers circuit directed
nv = int(input("enter number of vertices"))
ne = int(input("enter number of edges"))
vertices = []
for i in range(nv):
    v = input("enter the vertices")
    vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
    edge = tuple(input("enter an edge").split())
    edges.append(edge)
print(edges)
adj_list = {ver: [] for ver in vertices}
for e in edges:
    v1, v2 = e
    adj_list[v1].append(v2)
    # adj_list[v2].append(v1)
print(adj_list)
------------------------------------------------------------------------
# degree sequence
import sys

deg_seq = [7, 6, 6, 4, 4, 3, 2, 2]
seq = sorted(deg_seq, reverse=True)
# if reverse=True is not given it normally gives in ascending order[2, 2, 3, 4, 4, 6, 6, 7] if given it will give decending order
print(seq)
if sum(seq) % 2 != 0:
    print(deg_seq, 'is invalid degree sequence')
    sys.exit()
while True:
    first_ele = seq.pop(0)
    for i in range(first_ele):
        seq[i] -= 1
    seq = sorted(seq, reverse=True)
    print('seq', seq)
    if -1 in seq:
        print('invalid sequence')
        sys.exit()
    if not (any(seq)):
        print(deg_seq, 'is a valid degree sequence')
        sys.exit()

_________________________________________________________________________
g = {
    'a': ['b', 'c', 'd'],
    'b': ['d', 'a', 'a'],
    'c': ['d', 'b', 'a'],
    'd': ['b', 'c', 'a'],

}
# for k in g:
#     print(k)
# print()
# print(len(g.keys()))
# print()
# print(g.values())
for i in g:
    # print([i],':',g[i],':',len(g[i]))

    print(i, ':', g[i], ':', len(g[i]), ":", end='')
    if len(g[i]) == (len(g.keys()) - 1):
        print('complete')
    else:
        print('not complete')
------------------
cubes=[]
for i in range(7):
    cubes.append(i**3)
print("cubes of numbers from 0-6:",cubes)
cubes=[i**3 for i in range(7)]
print (cubes)


__________________________
list=[(x,y)for x in[10,30,50]for y in [20,40,60]]
print(list)
output
[(10, 20), (10, 40), (10, 60), (30, 20), (30, 40), (30, 60), (50, 20), (50, 40), (50, 60)]
