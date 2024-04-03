# Program to add two matrices using nested loop

x= [[1, 2, 3],
     [4, 5, 6]]


y= [[9, 8],
     [6, 5],
     [3, 2]]

xrow=len(x)
xcol=len(x[0])
print(xrow,xcol)

yrow=len(y)
ycol=len(y[0])
print(yrow,ycol)

emp=[]
for i in range(max(xrow,yrow)):
     rowe=[]
     for j in range(max(xcol,ycol)):
          rowe.append(0)
     emp.append(rowe)
print(emp)