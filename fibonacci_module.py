# fibonacci_module.py

def generate_fibonacci_numbers(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers

# def get_n_fibonacci_numbers(n):
#     return generate_fibonacci(n)
