# Errors and Exceptions

# SyntaxError
# -> a = 5 print(a)
# -> print(5))

# NameError
# -> print(a)

# TypeError
# -> 5 + "Hello"

# ModuleNotFoundError
# -> import something

# FileNotFoundError
# -> f = open("something.txt")

# ValueError
# -> a = [1, 2, 3]
# -> a.remove(4)
# -> print(a)

# IndexError
# -> a = [1, 2, 3]
# -> print(a[3])

# KeyError
# -> a = {"name": "John"}
# -> print(a["age"])

# AttributeError
# -> a = 10
# -> print(a.append(5))

# Exception
# -> a = 5
# -> b = 0
# -> print(a / b)

# AssertionError: x is not positive
x = -5
assert (x >= 0), "x is not positive"

# AssertionError: x is not positive
try:
    a = 5 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
