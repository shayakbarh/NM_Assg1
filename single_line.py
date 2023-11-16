# single line Python code to print the first 10 Fibonacci numbers

from functools import reduce

# Using a lambda function to calculate Fibonacci numbers
fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])

# Print the first 10 Fibonacci numbers
print(fibonacci(10))
