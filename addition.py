# Generalising the function to take an arbitrary number of keyword arguments
def adder(**x):
    return sum(x.values())

# Calling the generalised function with keyword arguments
result = adder(ugly=1, good=5, bad=3)

# Printing the result
print("Sum of the keyword arguments: ", result)




