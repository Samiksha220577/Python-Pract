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