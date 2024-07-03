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