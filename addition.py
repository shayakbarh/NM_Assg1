
# Defining the adder function that adds two numbers

def adder(x,y):
    return x + y

# Calling the adder function with different types of arguments

result_string = adder("Navy", "Nagar")
result_list = adder([1, 2, 3], [4, 5, 6])
result_float = adder(2.12, 4.57)

# Using print statement to see the results
print("\nAddition of two strings: ", result_string)

print("\nAddition of two lists: ", result_list)

print("\nAddition of two floats: ", result_float)