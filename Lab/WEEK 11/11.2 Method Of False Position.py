# import sympy as sp
#
# # Define the variable x
# x = sp.symbols('x')
#
# # Take input for coefficients (a, b, c, d)
# # a = float(input("Enter coefficient a: "))
# # b = float(input("Enter coefficient b: "))
# # c = float(input("Enter coefficient c: "))
# # d = float(input("Enter coefficient d: "))
# a,b,c,d=map(float,input('enter a b c d: ').split())
#
# # Define the polynomial equation
# eq = a*x**3 + b*x**2 + c*x + d
#
# print("The polynomial equation is:", eq)
#
# # Take input for boundary values of x
# # x1 = float(input("Enter lower bound x1: "))
# # x2 = float(input("Enter upper bound x2: "))
# x1,x2=map(float,input('enter x1 x2 : ').split())
#
# # Solve the equation numerically using nsolve
# sol = sp.nsolve(eq, x, (x1 + x2) / 2)  # initial guess is the midpoint of the interval
# r=int(input('rounding: '))
# # Round the solution to 4 decimal places
# sol = round(float(sol), r)
#
# print("The solution to the equation is:", sol)
# -------------------------------------------------------
import math

# Take input for coefficients (a, b, c, d)
a, b, c, d = map(float, input('Enter coefficients a, b, c, d separated by spaces: ').split())

# Take input for boundary values of x
x1, x2 = map(float, input('Enter lower bound x1 and upper bound x2 separated by spaces: ').split())

# Define the function to find the roots
def f(x):
    return a*x**3 + b*x**2 + c*x + d

# Define the derivative of the function
def f_prime(x):
    return 3*a*x**2 + 2*b*x + c

# Implement the Newton-Raphson method
def newton_raphson(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = x - f(x) / f_prime(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x

# Set the initial guess, tolerance, and maximum iterations
x0 = (x1 + x2) / 2
tol = 1e-6
max_iter = 100

# Solve the equation using the Newton-Raphson method
sol = newton_raphson(x0, tol, max_iter)

# Take input for rounding
r = int(input('Enter the number of decimal places to round the solution: '))

# Round the solution
sol = round(sol, r)

print("The solution to the equation is:", sol)