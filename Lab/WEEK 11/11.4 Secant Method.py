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