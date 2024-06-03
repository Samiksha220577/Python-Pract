int=int(input("Enter a number: "))
# lst=[]
i=1
z=''
# while int>0:
#     r=int%2
#     # lst.append(r)
#     int=int//2
#
#     z=str(r)+z
#     print(z)

# if int==0:
#     print("0")
# else:
#     while i<=int:
#
#         r=int%2
#         int=int//2
#         z = str(r) + z
#         print(z)
#     int=int+1
for i in range(1, int+1):
    binary_str = ""
    while i > 0:
        remainder = i % 2
        i = i // 2
        binary_str = str(remainder) + binary_str
    print(binary_str)