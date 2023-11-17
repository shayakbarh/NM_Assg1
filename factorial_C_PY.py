# Factorial calculation Using Python, but writing the factorial function in C

import ctypes

# Load the C library
factorial_lib = ctypes.CDLL('./factorial.so')  # Replace with the actual path to the compiled shared object file

# Define the Python wrapper for the factorial function
def factorial(n):
    return factorial_lib.factorial(n)

# Example usage
n = 6
result = factorial(n)
print(f"Factorial of {n} is {result}")