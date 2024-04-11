# n=int(input())
# list=[]
# for i in range(1,n+1):
#     if (i % 3 == 0 and i % 5 == 0):
#         list.append('fizzbuzz')
#     elif(i%3==0):
#         list.append('fizz')
#     elif(i%5==0):
#         list.append('buzz')
#     else:
#         list.append(str(i))
# print(list)
# ------------------------------------
# num=int(input())
# em=[]
# def fizzBuzz(num):
#
#     for i in range(num):
#         if i%15==0:
#             em.append("fizzbuzz")
#         elif i%3==0:
#             em.append("fizz")
#         elif i%5==0:
#             em.append("buzz")
#         else:
#             em.append(str(i))
#     return em
# print(fizzBuzz(num))
# -------------------------------------------------------
n = int(input())

def fizzBuzz(n):
    answer = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

result = fizzBuzz(n)
print(" ".join(result))