
# Modifying the function to take keyword arguments with default values
def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly

# Call the function with specific keyword arguments
result = adder(ugly=1, good=5)

# Print the result
print("Sum: ", result)



