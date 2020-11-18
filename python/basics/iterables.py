# List

x = [1, 2, 3]  # list
x = {1, 1, 2, 2, 3, 3}  # set: Unique list of values
print(x, len(x))  # {1,2,3} 3
x = (1, 2, 3)  # Tuple: immutable list

# List expressions

x = [i for i in range(1, 4)]
print(x)  # [1,2,3]

x = [a+b for a in [1, 2, 3] for b in [1, 2, 3]]  # for inside for
print(x)

x = [a[0]+a[1] for a in zip([1, 2, 3], [1, 2, 3])]
print(x)  # 2, 4, 6

x = [a[0]+a[1] for a in zip([1, 2, 3], [1, 2, 3][::-1])]
print(x)  # 4, 4, 4

x = [i for i in range(5) if i % 2 == 0]
print(x)

x = {a for a in [0, 1, 2, 3, 4, 5] for b in [2, 5] if a % b == 0}
print(x)

x = [i for i in map(lambda x: x**2, range(5))]
print(x)


# Dictionary

x = {
    'name': 'Sam',
    'age': 27,
    'address': {
        'street': 'Purple street, 123',
        'zipcode': 'OX11 9ED',
    },
    'favorite foods': {
        1: 'Pizza',
        2: 'Chocolate'
    },
    'friends': ['Ann', 'Bob', 'Alice']
}

print(len(x))
print(x.keys())
print(x.values())
print(x.items())
