# Factorial calculation Using Python, but with the factorial function from SciPy and finding its execution time

from scipy.special import factorial
import timeit
from scipy.special import factorial
import timeit
# Function to calculate factorial using SciPy
def calculate_factorial(n):
    return factorial(n)
if __name__ == "__main__":
    n = 5 # Example: Calculate factorial of 5
    elapsed_time = timeit.timeit(lambda: calculate_factorial(n), number=100000)
    result = calculate_factorial(n)
    print(f"Factorial of {n} is {result}")
    print(f"Time taken: {elapsed_time:.10f} seconds")