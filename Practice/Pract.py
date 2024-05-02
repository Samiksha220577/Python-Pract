x=[1,2,3]
inp=input('enter type ')
# ------------------------------------
# push
def pushing(x,item):
    # item=int(input('enter item to be pushed'))
    x.append(item)
    print(x[::-1])
# item=int(input("Enter no to push"))

# push(x,item)
# --------------------------
def popi(x):
    x.pop()
    print(x[::-1])
# -------------------------------
# top
def top(x):
    print(x[0])

if inp=='pop':
    popi(x)

if inp=='push':
    item=int(input('enter item '))
    pushing(x,item)

