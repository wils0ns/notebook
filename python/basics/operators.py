# Arithmetic operators

print(1+1)
print(1-1)
print(1*1)
print(3/2)
print(3//2)  # Floor division
print(3 % 2)  # Modulus
print(3**2)  # Exponentiation

# Comparison operators

print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 >= 1)
print(1 < 1)
print(1 <= 1)

# Logic operators

# Result: False, because `and` requires both sentences to be True
print(True and False)
# Result: True, because `or` requires at least one of the sentences to be True
print(True or False)

# Assigment operators

x = 1
x += 1  # x = x+1
x -= 1  # x = x-1
x *= 1  # x = x*1
x /= 1  # x = x / 1
x **= 1  # x = x ** 1

# Variable unpacking

x, y, z = (1, 2, 3)
print(x, y, z)

x = [1, 2, 3]
print(x[0], x[1], x[2])
print(*x, sep='🌹')

# Identity Operators

print(True is False)  # False
print(True is not False)  # True

# Membership Operators

print(1 in [1, 2, 3])  # True
print(1 in [4, 5, 6])  # False
