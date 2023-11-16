# Python code for generating first 10 Fibonacci numbers

# defining a function "generate_fibonacci" to generate first n Fibonacci numbers

def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers

# defining a function "main" to print the result

def main():
    n = 10  # Number of Fibonacci numbers to generate
    fibonacci_numbers = generate_fibonacci(n)

    print("First {} Fibonacci numbers:".format(n))
    for number in fibonacci_numbers:
        print(number)

if __name__ == "__main__":
    main()
