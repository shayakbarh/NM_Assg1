# Python code that searches a list of numbers for 2^5

# Now eliminate the found flag and the final if statement by using the Python's while else construction

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(X, 'not found')

