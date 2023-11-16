"""
    Turning the file into a module that has a function that returns n Fibonacci numbers,
    where n is the function argument.
"""

# defining a function "generate_fibonacci" to generate first n Fibonacci numbers

def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers


