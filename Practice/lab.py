#input list 1
input_str = input("Enter list1  of lists of integers separated by commas, where each list is separated by spaces: ")
list_str = input_str.split(',')
# print(list_str)
list1 = [list(map(int, sublist.split())) for sublist in list_str]
print(list1)
matrix1columns=len(list1[0])
mat1row=len(list1)


#input list 2
inputli  = input("Enter list1  of lists of integers separated by commas, where each list is separated by spaces: ")
liststr = inputli.split(',')
# print(list_str)
list2 = [list(map(int, sublist.split())) for sublist in liststr]
print(list2)
matrix2columns=len(list2[0])
mat2row=len(list2)

#creating empty matrix
fin=[]
for i in range(max(mat1row,mat2row)):
    rowa=[]
    for j in range(max(matrix1columns,matrix2columns)):
        rowa.append(0)
    fin.append(rowa)
print(fin)
#multiplication
