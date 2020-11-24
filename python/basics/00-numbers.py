# See data models for more info:
# https://docs.python.org/3/reference/datamodel.html

# Integers (int)
print(1+1)  # prints 2

# Booleans (bool)
print(True)  # prints True
print(False)  # prints False

# Booleans, for all intents and purposes, are like integers,
# except when converting to string

print(True + 1)  # prints 2
print(False * 2)  # prints 0
print(str(True))  # prints 'True'

# Real (float)
print(0.5 + .5 + 1.5)  # prints 2.5

# Complex (complex)
c1 = 0.5 + 0.5j
c2 = complex(1, 0.5)


print(c1.real, c1.imag)  # prints 1 0.5
print(c1 + c2 == 1.5+1j)  # prints True
