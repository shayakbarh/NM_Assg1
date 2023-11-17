# Factorial calculation Using Python, but with the factorial function from SciPy 

from scipy.special import factorial
n = 5   # here I want to calculate factorial of 5
result = factorial(n)
print(f"Factorial of {n} is {result}")