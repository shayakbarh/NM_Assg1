""" 
    Python code for generating first 100 Fibonacci numbers 
"""

import fibonacci_module

def main():
    n = 100  # Number of Fibonacci numbers to generate
 
    fibonacci_numbers = fibonacci_module.generate_fibonacci(n)
   


    print("First {} Fibonacci numbers:".format(n))

    print(fibonacci_numbers)
    


if __name__ == "__main__":
    main()
