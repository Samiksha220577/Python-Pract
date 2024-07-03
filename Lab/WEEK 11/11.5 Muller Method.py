# # Python3 Program to find root of
# # a function, f(x)
# import math;
#
# MAX_ITERATIONS = 10000;
#
#
# # Function to calculate f(x)
# def f(x):
#     # Taking f(x) = x ^ 3 + 2x ^ 2 + 10x - 20
#     return (1 * pow(x, 3) + 2 * x * x +
#             10 * x - 20);
#
#
# def Muller(a, b, c):
#     res = 0;
#     i = 0;
#
#     while (True):
#
#         # Calculating various constants
#         # required to calculate x3
#         f1 = f(a);
#         f2 = f(b);
#         f3 = f(c);
#         d1 = f1 - f3;
#         d2 = f2 - f3;
#         h1 = a - c;
#         h2 = b - c;
#         a0 = f3;
#         a1 = (((d2 * pow(h1, 2)) -
#                (d1 * pow(h2, 2))) /
#               ((h1 * h2) * (h1 - h2)));
#         a2 = (((d1 * h2) - (d2 * h1)) /
#               ((h1 * h2) * (h1 - h2)));
#         x = ((-2 * a0) / (a1 +
#                           abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
#         y = ((-2 * a0) / (a1 -
#                           abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
#
#         # Taking the root which is
#         # closer to x2
#         if (x >= y):
#             res = x + c;
#         else:
#             res = y + c;
#
#         # checking for resemblance of x3
#         # with x2 till two decimal places
#         m = res * 100;
#         n = c * 100;
#         m = math.floor(m);
#         n = math.floor(n);
#         if (m == n):
#             break;
#         a = b;
#         b = c;
#         c = res;
#         if (i > MAX_ITERATIONS):
#             print("Root cannot be found using",
#                   "Muller's method");
#             break;
#         i += 1;
#     if (i <= MAX_ITERATIONS):
#         print("The value of the root is",
#               round(res, 4));
#
#
# # Driver Code
# a = 0;
# b = 1;
# c = 2;
# Muller(a, b, c);
#
# # This code is contributed by mits
# ------------------------------------------------
# import math
#
# def f(x, eq):
#     return eval(eq)
#
# def Muller(a, b, c, eq, tol=1e-5, max_iter=1000):
#     for _ in range(max_iter):
#         fa = f(a, eq)
#         fb = f(b, eq)
#         fc = f(c, eq)
#         d1 = (fb - fc) / (b - c)
#         d2 = ((fb - fc) / (b - c) - (fa - fb) / (a - b)) / (c - b)
#         h = -2 * fc / (d1 + math.copysign(1, d1) * math.sqrt(d1**2 - 2 * fc * d2))
#         x = c + h
#         if abs(h) < tol:
#             return x
#         a, b, c = b, c, x
#     return x
#
# # Get equation and initial guesses from user
# eq = input("Enter the equation (e.g. x**3 + 2*x**2 + 10*x - 20): ")
# a = float(input("Enter the first initial guess: "))
# b = float(input("Enter the second initial guess: "))
# c = float(input("Enter the third initial guess: "))
#
# root = Muller(a, b, c, eq)
# print("The value of the root is", round(root, 4))
# ----------------------
# import cmath
#
#
# def f(x, coefficients):
#     return sum(coef * x ** i for i, coef in enumerate(coefficients))
#
#
# def muller(coefficients, x0, x1, x2, max_iter=100, tol=1e-6):
#     for _ in range(max_iter):
#         f0 = f(x0, coefficients)
#         f1 = f(x1, coefficients)
#         f2 = f(x2, coefficients)
#
#         h1 = x1 - x0
#         h2 = x2 - x1
#         delta1 = (f1 - f0) / h1
#         delta2 = (f2 - f1) / h2
#         a = (delta2 - delta1) / (h2 + h1)
#         b = a * h2 + delta2
#         c = f2
#
#         discriminant = cmath.sqrt(b ** 2 - 4 * a * c)
#         if abs(b + discriminant) > abs(b - discriminant):
#             root = x2 + (-2 * c) / (b + discriminant)
#         else:
#             root = x2 + (-2 * c) / (b - discriminant)
#
#         if abs(root - x2) < tol:
#             return root.real
#
#         x0, x1, x2 = x1, x2, root
#
#     raise ValueError("Root not found within given tolerance")
#
#
# def main():
#     # Reading user input
#     coefficients = list(map(float, input("Enter the coefficients of the equation separated by space: ").split()))
#     initial_guesses = list(map(float, input("Enter the three initial guesses separated by space: ").split()))
#     decimal_places = int(input("Enter the number of decimals to round the root to: "))
#
#     # Ensure we have exactly three initial guesses
#     if len(initial_guesses) != 3:
#         raise ValueError("Exactly three initial guesses are required")
#
#     x0, x1, x2 = initial_guesses
#
#     root = muller(coefficients, x0, x1, x2)
#     print(f"Root: {round(root, decimal_places)}")
#
#
# # Running the main function
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------
import cmath
import cmath


def f(x, coefficients):
    return sum(coef * x ** i for i, coef in enumerate(coefficients))


def muller(coefficients, x0, x1, x2, max_iter=100, tol=1e-6):
    for _ in range(max_iter):
        f0 = f(x0, coefficients)
        f1 = f(x1, coefficients)
        f2 = f(x2, coefficients)

        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f1 - f0) / h1
        delta2 = (f2 - f1) / h2
        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = f2

        discriminant = cmath.sqrt(b ** 2 - 4 * a * c)
        if abs(b + discriminant) > abs(b - discriminant):
            root = x2 + (-2 * c) / (b + discriminant)
        else:
            root = x2 + (-2 * c) / (b - discriminant)

        if abs(root - x2) < tol:
            return root.real

        x0, x1, x2 = x1, x2, root.real

    raise ValueError("Root not found within given tolerance")


def main():
    # Reading user input
    coefficients = list(map(float, input("Enter the coefficients of the equation separated by space: ").split()))
    initial_guesses = list(map(float, input("Enter the three initial guesses separated by space: ").split()))
    decimal_places = int(input("Enter the number of decimals to round the root to: "))

    # Ensure we have exactly three initial guesses
    if len(initial_guesses) != 3:
        raise ValueError("Exactly three initial guesses are required")

    x0, x1, x2 = initial_guesses

    root = muller(coefficients, x0, x1, x2)
    print(f"Root: {round(root, decimal_places)}")


# Running the main function
if __name__ == "__main__":
    main()

# Running the main function
if __name__ == "__main__":
    main()
