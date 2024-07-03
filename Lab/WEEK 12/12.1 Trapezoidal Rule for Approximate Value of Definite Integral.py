# def trapezoidal_rule(coefficients, interval, n):
#     a, b = interval
#     h = (b - a) / n
#     x = [a + i * h for i in range(n + 1)]
#     y = [eval(coefficients, {"x": xi}) for xi in x]
#     area = h * ((y[0] + y[-1]) / 2 + sum(y[1:-1]))
#     return area
#
# coefficients = input()
# interval = list(map(float, input().split()))
# n = int(input())
#
# print(trapezoidal_rule(coefficients, interval, n))
# -------------------------------------------------------
# def calculate_coefficient(x, coefficients):
#     result = 0
#     for degree, coefficient in enumerate(coefficients):
#         result += coefficient * (x ** degree)
#     return result
#
# def trapezoidal_rule(coefficients, a, b, n):
#     h = (b - a) / n
#     x = [a + i * h for i in range(n + 1)]
#     y = [calculate_coefficient(xi, coefficients) for xi in x]
#     area = h * ((y[0] + y[-1]) / 2 + sum(y[1:-1]))
#     return area
#
# coefficients = list(map(float, input("Enter coefficients of the equation (separated by space): ").split()))
# a, b = map(float, input("Enter the integral interval [a, b] (separated by space): ").split())
# n = int(input("Enter the number of sub intervals: "))
#
# result = trapezoidal_rule(coefficients, a, b, n)
# print("The approximate value of the definite integral is: ", result)
# --------------------------------------
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
for i in range(1,n+1):
    x.append(round(a+i*h,4))
y = []
for i in range(n+1):
    y.append(f_x(x[i]))
area = y[0] + y[-1]
for j in range(1, n):
    area += 2*y[j]
app = h*area/2
print(app)