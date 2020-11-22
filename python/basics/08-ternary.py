# Ternary operations
x = 1 if 1 % 2 == 0 else 2  # x == 2

# Using tuple
x = ('💩', '🎆')[1 > 2]  # x == 💩

# Using dictionary
x = {False: '🎈', True: '🧨'}[1]  # x == '🧨'

# 0 and 1 indexes have nothing to do with indexed access
# of dictonary.
try:
    x = {False: '🎈', True: '🧨', 'Another index': '🎀'}[2]
except KeyError as e:
    # Will be executed
    print('x has no key of ', e)

# Using lambda
x = (lambda: 3, lambda: 4)[False]  # x() == 3

# Adding any more than 2 choises will fallback to index lookup
x = (lambda: 3, lambda: 4, lambda: 5)[2]  # x() == 5
