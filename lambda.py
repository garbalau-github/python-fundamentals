# Lambda: Anonymous Functions in Python

# addTen = lambda x: x + 10

# Works like this
def addTenFunc(x):
    return x + 10


# Usage
arr = [1, 2, 3, 4, 5]
new_arr = map(lambda x: x + 10, arr)
print(list(new_arr))  # [11, 12, 13, 14, 15]
