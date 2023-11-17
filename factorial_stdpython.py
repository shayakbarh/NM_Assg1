# Factorial calculation using standard python and finding its execution time 

import timeit
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
if __name__ == "__main__":
    n = 20 # Example: Compute factorial of 500
    print(f"Factorial of {n} is {factorial(n)}")
    elapsed_time = timeit.timeit(lambda: factorial(n), number=1000)
    print(f"Time taken: {elapsed_time:.10f} seconds")





