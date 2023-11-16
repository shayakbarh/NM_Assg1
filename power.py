# Python code that searches a list of numbers for 2^5

# Now removing the loop completely by using the 'in' operator

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if 2 ** X in L:
    print(f"at index {L.index(2 ** X)}")
else:
    print(f"{X} not found")
