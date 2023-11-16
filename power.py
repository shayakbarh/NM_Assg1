
powers_of_2 = []
X = 5

# Generate powers of 2 using a for loop and append method
for i in range(X + 1):
    powers_of_2.append(2 ** i)

# Check if 2**X is in the generated list
if 2 ** X in powers_of_2:
    print(f"at index {powers_of_2.index(2 ** X)}")
else:
    print(f"{X} not found")

