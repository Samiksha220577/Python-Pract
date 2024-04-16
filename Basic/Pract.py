x=[]
open=["{","[","("]
close=["}","]",")"]
inp=input()
for i in inp:
    if i in open:
        x.append(i)
    # print(x)
    if i in close:
        pos = close.index(i)
        ahh=x[-1]
        print(pos)
        print(open.index(ahh))
        # if pos==open.index(ahh):




