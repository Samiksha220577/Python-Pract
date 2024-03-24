# a=int(input('enter x:'))
# b=int(input('enter y:'))
# print(a+b)
# x = int(input("Enter no"))
# if x == 1:
#     print("monday")
# elif x == 2:
#     print("tuesday")
# elif x == 3:
#     print("wednesday")
# elif x == 4:
#     print("thusday")
# elif x == 5:
#     print("friday")
# elif x == 6:
#     print("saturday")
# else x == 7:
#     print("sunday")
#-------------------------------------------------------------
# #roman to int
# def romantoint(s):
#     m={
#         'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000,
#     }
#     ans=0
#     for i in range(len(s)):
#         if i<len(s)-1 and m[s[i]]<m[s[i+1]]:
#             ans -= m[s[i]]
#         else:
#             ans += m[s[i]]
#     return ans
# s=input("Enter roman number")
# print(romantoint(s))
#---------------------------------------------------------
