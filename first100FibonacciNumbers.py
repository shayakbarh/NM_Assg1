""" 
    Python code for generating first 100 Fibonacci numbers 
    and checking how long it takes to run.
"""

import fibonacci_module
import timeit


def main():
    n = 100  # Number of Fibonacci numbers to generate


    # Measure the execution time using timeit
    start_time = timeit.default_timer()
    fibonacci_numbers = fibonacci_module.generate_fibonacci_numbers(n)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time


    print("First {} Fibonacci numbers:".format(n))
    for number in fibonacci_numbers:
        print(number)

    print("\nExecution Time: {} seconds".format(execution_time))




if __name__ == "__main__":
    main()
