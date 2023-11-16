
# Defining the adder function that adds an arbitrary number of arguments
def adder(*x):
    return sum(x)

# Calling  the generalized adder function
result = adder(1, 2, 3, 4, 5)

# Printing the result
print("Sum = ", result)



