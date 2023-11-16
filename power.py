# Python code that searches a list of numbers for 2^5

# Now using Python's for-else construction and list index method to eliminate the explicit list-indexing logic

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for i, value in enumerate(L):
    if 2 ** X == value:
        print('at index', i)
        break
else:
    print(X, 'not found')



