# WEEK-1
# ----------------------------------------------------------------------------
# 1.1TWO SUM
class TwoSum:
    def __init__(self, list1, target):
        self.list1 = list1
        self.target = target

    def solution(self):
        length = len(list1)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if list1[i] + list1[j] == self.target:
                    new_list = i, j
                    return list(new_list)
        return -1


list1 = list(map(int, input().split(',')))
target = int(input())
obj = TwoSum(list1, target)
# print(obj.solution())

# list1 = [1, 2, 3, 4, 5]
print(*obj.solution(), sep=", ")
# ------------------------------------------------------------------------
# 1.2 CONTAINS DUPLICATE
nums=list(map(int,input().split(',')))
count=0
x=set(nums)
if len(nums)==len(x):
    print('false')
else:
    print('true')
# -----------------------------------------------

# 1.3 ROMAN TO INT
def romantoint(s):
    m={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    ans=0
    for i in range(len(s)):
        if i<len(s)-1 and m[s[i]]<m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    return ans
s=input()
print(romantoint(s))
# --------------------------------------------
inp=input()
nums=inp.split(',')
list = [int(num) for num in nums]
# print(list)



# list=[1,2,3]
s=''
for i in list:
    s+=str(i)#in string 1+2=12
x=int(s)
z=x+1
# print(z)


dig=[]
while z>0:
    dig.append(z%10)
    z//=10

print(*dig[::-1],sep=', ')
# -----------------------------------------
inp=input()
nums=inp.split(',')
list = [int(num) for num in nums]
# print(list)

# list=[3,3,3,2,2,2]
for i in list:
	# print('i',i)
	if list.count(i)>=len(list)/2:
		print(i)
		break
# -----------------------------------------
def maximumWealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth
# customers = 2
# accounts = [[1,2,3], [3,2,1]]
# Get the number of customers
customers = int(input())

# Initialize the accounts list
accounts = []

# Get the bank accounts for each customer
for i in range(customers):
    # Get the account balances for each customer as a list
    account_balances = list(map(int, input().split(',')))
    # Add the account balances list to the accounts list
    accounts.append(account_balances)

# Print the accounts list for verification
# print(accounts)

print(maximumWealth(accounts))
# -----------------------------------------
n = int(input())


answer = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        answer.append("FizzBuzz")
    elif i % 3 == 0:
        answer.append("Fizz")
    elif i % 5 == 0:
        answer.append("Buzz")
    else:
        answer.append(i)
print(*answer,sep=', ')
# ------------------------------------------
x=int(input())
count=0
while x>0:
    if(x%2!=0):
        x=x-1
        # print (x)
        count+=1

    else:
        x=x//2
        count+=1

print(count)
# --------------------------------------------
inp=list(map(int,input().split(',')))
sum=0
x=[]
for i in inp:
    sum=sum+i
    x.append(sum)
print(*x,sep=', ')
# ------------------------------------------------
nums=list(map(int,input().split(',')))
val=int(input())
index=0
for i in range(len(nums)):
    if (nums[i]!=val):
        nums[index]=nums[i]
        index+=1
print(index)
# -----------------------------------------------
# WEEK-2
n1=int(input())
m1=[]
for i in range(n1):
    k=[int(i) for i in input().split(',')]
    m1.append(k)
n2=int(input())
m2=[]
for i in range(n2):
    k=[int(i) for i in input().split(',')]
    m2.append(k)
add=[[m1[i][j] + m2[i][j]for j in range(n1)]for i in range(n1)]
for i in add:
    print(*i,sep=', ')
# ----------------------------------------
x=[]
[r1,c1]=list(map(int,input().split(',')))
for i in range(r1):
    u=list(map(int,input().split(',')))
    x.append(u)

y=[]
[r2,c2]=list(map(int,input().split(',')))
for i in range(r2):
    v=list(map(int,input().split(',')))
    y.append(v)
row1=len(x)
col1=len(x[0])
row2=len(y)
col2=len(y[0])
if col1==row2:
    prod=[[0]*col2 for i in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                prod[i][j]+=x[i][k]*y[k][j]
# print(prod)
for i in prod:
    print(*i,sep=', ')
# ----------------------------------------
x=[]
[r1,c1]=list(map(int,input().split(',')))
for i in range(r1):
    u=list(map(int,input().split(',')))
    x.append(u)
mat=[[0]*r1 for i in range (c1)]
for i in range(c1):
    for j in range(r1):
        mat[i][j]=x[j][i]
# for i in mat:
#     for j in i[:-1]:
#         print(j,end=',')
#     print(i[-1])

for i in mat:
     print(*i,sep=', ')
# ------------------------------------------------

x=[]
[r1,c1]=list(map(int,input().split(',')))
for i in range(r1):
    u=list(map(int,input().split(',')))
    x.append(u)
pro=1
for i in x:
    for j in i:
        pro=pro*j
print(pro)
# --------------------------------------------
# WEEK-3
# -------------------------
# Check for balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
inp=input()
# Function to check parentheses
def check(myStr):
    stack = []
    for char in myStr:
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            if not stack or close_list.index(char) != open_list.index(stack.pop()):#if not stack checks if stack is empty
                return "Unbalanced"
    return "Balanced" if not stack else "Unbalanced"

# Test cases
print(check(inp))
# ----------------------------------
num=list(input().split())
stack=[]
for i in num:
    if i=='*':
        a=stack.pop()
        b=stack.pop()
        stack.append(b*a)
    elif i=='+':
        a=stack.pop()
        b=stack.pop()
        stack.append(b+a)
    elif i=='-':
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)
    elif i=='/':
        a=stack.pop()
        b=stack.pop()
        stack.append(b/a)
    else:
        stack.append(int(i))
print(stack.pop())
# ----------------------------------------------------
# WEEK-4
# ---------------------------------------------------------
n=int(input())
if n==0:
    print('0')
else:
    for i in range(1, n+1):
        binary_str = ""
        while i > 0:
            remainder = i % 2
            i = i // 2
            binary_str = str(remainder) + binary_str
        print(binary_str)
# -----------------
def next_greater_element(arr):
    nge = [-1] * len(arr)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                nge[i] = arr[j]
                break

    return nge

arr = list(map(int, input().split(',')))
result = next_greater_element(arr)
print(', '.join(map(str, result)))
# ------------------------------
# WEEK-5
# -----------------------------------
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
# --------------------------------
nodes=int(input())
edgesno=int(input())
edges=[]
for i in range(edgesno):
    edge=list(map(int, input().split(' ')))
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
# -------------------------------------
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
# -----------------------------------------
n = int(input())

graph = {}
for i in range(n):
    line = input().split(": ")
    node = int(line[0])
    connections = line[1].strip().split(" ")
    graph[node] = [int(x) for x in connections if x != '']

transpose_graph = {}
for i in range(n):
    transpose_graph[i] = []

for node, connections in graph.items():
    for connection in connections:
        transpose_graph[connection].append(node)

for node, connections in transpose_graph.items():
    print(node, ":", connections)
# --------------------------------------------------
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
            if ((i, j) in white_edges and (j, k) in white_edges and (i, k) in white_edges) or\
               ((i, j) not in white_edges and (j, k) not in white_edges and (i, k) not in white_edges):
                count += 1

print(count)
# ----------------------------------------------
# WEEK-9
# ------------------------------------------------
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
no_vertices, no_edges = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(no_edges)]
adj_list = [[] for _ in range(no_vertices)]
for v1, v2 in edges_list:
    adj_list[v1].append(v2)
start_vertex = int(input())
bfs(adj_list, start_vertex)

# --------------------------------------------------
nv, ne = list(map(int,input().split()))
edges = []
for i in range(ne):
    edge = list(map(int,input().split()))
    edges.append(edge)
adj_list = {v:[] for v in range(nv)}
for v1, v2 in edges:
    adj_list[v1].append(v2)
start = int(input())
dfs = []
s = [start]
while(len(s)>0):
    ele = s.pop()
    if ele not in dfs:
        dfs.append(ele)
    for j in adj_list[ele][::-1]:
        if j not in dfs:
            s.append(j)
print(*dfs)
# --------------------------------------------------
# WEEK-10
# -----------------------------------
v,ne = map(int, input().split(', '))
vrt = []
ed = []
for x in range(v):
    vrt.append(x)
for x in range(ne):
    a,b,c = tuple(map(int, input().split(',')))
    ed.append((a,b,c))
mp={}
for x in range(v):
    mp[x]=x
wp={}
for a,b,c in ed:
    wp[b,c]=a
w=[]
for x in wp.values():
    w.append(x)
w.sort()
vis=[]
for x in w:
    c=0
    q=0
    for y in wp.items():
        i,j=y
        v1,v2=i
        if x==j:
            if mp[v1]!=mp[v2]:
                if i not in vis:
                    vis.append(i)
                for z in mp.items():
                    k,l=z
                    if q==0:
                        a=mp[v2]
                        q+=1
                    if  l==a:
                        mp[k]=mp[v1]
                        c+=1
        if c!=0:
            break
min_cost=0
for x in vis:
    for i,j in wp.items():
        if x==i:
            min_cost+=j
print(min_cost)
# -------------------------------------
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
# ----------------------------------------
# WEEK-11
# -----------------------------------------------
def f_x(x):
    ordr = len(c)
    fx = 0
    for i in range(ordr):
        fx += c[i]*x**(ordr-1-i)
    return(round(fx, dec))
c = list(map(int,input().split()))
a, b = map(int,input().split())
dec = int(input())
if f_x(a) < 0:
    prev = a
    nxt = b
else:
    prev = b
    nxt = a
while(True):
    x = (prev + nxt) / 2
    if f_x(x) < 0:
        prev = round(x,dec)
    else:
        nxt = round(x,dec)
    if prev == nxt:
        break
print(nxt)
# ---------------------------------------
import math

# Take input for coefficients (a, b, c, d)
a, b, c, d = map(float, input().split())

# Take input for boundary values of x
x1, x2 = map(float, input().split())

# Define the function to find the roots
def f(x):
    return a*x**3 + b*x**2 + c*x + d

# Define the derivative of the function
def f_prime(x):
    return 3*a*x**2 + 2*b*x + c

# Implement the Newton-Raphson method
def newton_raphson(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = x - f(x) / f_prime(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x

# Set the initial guess, tolerance, and maximum iterations
x0 = (x1 + x2) / 2
tol = 1e-6
max_iter = 100

# Solve the equation using the Newton-Raphson method
sol = newton_raphson(x0, tol, max_iter)

# Take input for rounding
r = int(input())

# Round the solution
sol = round(sol, r)

print(sol)
# ------------------------------------------------
def f_x(x):
    ordr = len(c)
    fx = 0
    dfx = 0
    for i in range(ordr):
        fx += c[i]*x**(ordr-1-i)
    for i in range(ordr-1):
        dfx += c[i]*(ordr-1-i)*x**(ordr-2-i)
    return([round(fx, dec),round(dfx, dec)])
c = list(map(int,input().split()))
a, b = map(int,input().split())
dec = int(input())
prev = (a + b) /2
while(True):
    f, df = f_x(prev)
    x = prev -  f / df
    nxt = round(x,dec)
    if prev == nxt:
        break
    else:
        prev = nxt
print(nxt)
# ----------------------------------------------------
def f_x(x):
    fx = 0
    n = len(z) - 1
    for i in range(len(z)):
        fx += z[i]*x**(n-i)
    return round(fx,dec)

z =list(map(int,input().split()))
a, b = list(map(int,input().split()))
p0 = a
p1 = b
dec = int(input())
while(True):
    root = (p0*f_x(p1) - p1*f_x(p0))/(f_x(p1)-f_x(p0))
    nxt = round(root,dec)
    if p1 == nxt:
        break
    else:
        p0 = p1
        p1 = nxt
print(nxt)
# ---------------------------------------
# Read coefficients of the polynomial from input
coeff = list(map(int, input().split()))

# Read initial guesses for the root
c, b, a = map(int, input().split())

# Read the number of decimal places for the result
rnd = int(input())


def fx(coeff, val):
    """
    Evaluate the polynomial at a given value.

    Args:
    coeff (list): Coefficients of the polynomial.
    val (int): Value at which to evaluate the polynomial.

    Returns:
    int: The result of evaluating the polynomial at the given value.
    """
    power = len(coeff) - 1
    eq = 0
    for i, coeff_i in enumerate(coeff):
        eq += coeff_i * (val ** power)
        power -= 1
    return eq


while True:
    # Calculate the differences in x and y values
    hi = a - b
    hi1 = b - c

    # Evaluate the polynomial at the current guesses
    fa = fx(coeff, a)
    fb = fx(coeff, b)
    fc = fx(coeff, c)

    # Calculate the differences in y values
    di = fa - fb
    di1 = fb - fc

    # Calculate the coefficients A and B for the quadratic equation
    A = (1 / (hi + hi1)) * ((di / hi) - (di1 / hi1))
    B = (di / hi) + (A * hi)

    # Calculate the root of the quadratic equation
    root = a - ((2 * fa) / (B + ((B ** 2 + 4 * A * fa) ** 0.5)))

    # Round the root to the desired number of decimal places
    newroot = round(root, rnd)

    # Check for convergence
    if newroot == a:
        print(newroot)
        break
    else:
        # Update the guesses for the next iteration
        c, b, a = b, a, newroot
# ---------------------------------------------
# WEEK-12
# ------------------------------------------------
def f_x(x):
    fx = 0
    p = len(z) - 1
    for i in range(len(z)):
        fx += z[i]*x**(p-i)
    return round(fx,4)
z = list(map(int,input().split()))
a, b = list(map(int,input().split()))
n = int(input())
h = (b-a)/n
x = [a]
for i in range(1,n+1):
    x.append(round(a+i*h,4))
y = []
for i in range(n+1):
    y.append(f_x(x[i]))
area = y[0] + y[-1]
for j in range(1, n):
    area += 2*y[j]
app = h*area/2
print(app)
# -----------------------------------------------
def f_x(x):
    fx = 0
    p = len(z) - 1
    for i in range(len(z)):
        fx += z[i]*x**(p-i)
    return round(fx,4)
z = list(map(int,input().split()))
a, b = list(map(int,input().split()))
n = int(input())
h = (b-a)/n
x = [a]
for i in range(1, n+1):
    x.append(round(a+i*h,4))
y = []
for i in range(n+1):
    y.append(f_x(x[i]))
area = y[0] + y[-1]
for j in range(1, n):
    if j%2:
        area += 4*y[j]
    else:
        area += 2*y[j]
app = h*area/3
print(round(app,4))
# -----------------------------------------------------
def f_x(x):
    fx = 0
    p = len(z) - 1
    for i in range(len(z)):
        fx += z[i]*x**(p-i)
    return round(fx,4)
z = list(map(int,input().split()))
a, b = list(map(int,input().split()))
n = int(input())
h = (b-a)/n
x = [a]
for i in range(1, n+1):
    x.append(round(a+i*h,4))
y = []
for i in range(n+1):
    y.append(f_x(x[i]))
area = y[0] + y[-1]
for j in range(1, n):
    if j%3==0:
        area += 2*y[j]
    else:
        area += 3*y[j]
app = 3*h*area/8
print(round(app,4))
# ------------------------------------------------------
# WEEK-13
# ------------------------------------------
def euler_method(x0, y0, h, x):
    y = y0
    while x0 < x:
        y = y + h * (x0 + y + x0 * y)
        x0 = x0 + h
    return round(y, 4)

x0 = int(input())
y0 = int(input())
h = float(input())
x = float(input())

print(euler_method(x0, y0, h, x))
# ------------------------------------------
def f_x(x,y):
    fx = -2*x*y**2
    return (round(fx,4))

x0 = int(input())
y0 = int(input())
x = float(input())

h = x - x0

k1 = h*f_x(x0,y0)
k2 = h*f_x(x0+h,y0+k1)

y = y0 + 0.5*(k1 + k2)

print(round(y,4))
# --------------------------------------