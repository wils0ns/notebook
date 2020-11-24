from functools import reduce

# built-in functions

print('Hi!')
eval("print('Hi!')")

# Define custom functions


def my_func():
    """
    my_func is a function that takes no arguments and does nothing.
    Use triple-double-quotes blocks to write a docstring.
    """


def example(): pass  # This function does nothing and has no docstring.


def real_func():
    """
    This function only executes something and returns None.
    Functions in python always returns None, by default.
    """
    print('Hello from real func!')


return_from_real_func = real_func()
print(return_from_real_func is None)  # True


def sum(a: float, b: float) -> float:
    """Adds b to a

    And has a stupid, unnecessary docstring in google docstring format

    In the function signature, we are using type annotations
    for the sake of examplifying its usage.

    Args:
        a (float): A number
        b (float): The number to be added

    Returns:
        float: the result of the sum of a + b
    """
    return a+b


print(sum(1, 2))


def better_sum(*n):
    """Adds any number of numbers (specified by any amount of positional arguments)

    Args:
        *n: one or more numbers to be added.
    Returns:
        float: the sum of all numbers
    """
    return reduce(lambda x, y: x+y, n)


print(better_sum(1, 2, 3, 4, 5))


def stronger(a, b, times=2):
    """
    Prints `a` statement that a is stronger than `b`.
    The `times` argument is optional since it has a default value

    Args:
        a (str): The stronger
        b (str): The weaker
        times (int, optional): How many times `a` is stronger than `b`. Defaults to `2`.
    """
    print(f'{a} is {times} times stronger than {b}')


stronger('Filipe', 'Wilson')
stronger('Filipe', 'Wilson', 10)
stronger('Filipe', 'Wilson', times=15)
stronger(b='Filipe', a='Wilson', times=25)


def address_to_dict(**elements):
    return elements


print(address_to_dict(
    street='6 copse view',
    zip_code='OX11 9FP',
    country='UK'
))

# print(address_to_dict(1, 2, 3)) fails with TypeError
# because the function takes no positional arguments


def print_all(*args, **kwargs):
    print('Positional arguments passed:', ','.join(map(str, args)))

    print('Keyword arguments passed:')
    for k, v in kwargs.items():
        print(f'{k}={v}')


print_all(1, 'Filipe', '🎭', name='Wilson', emoji='🎄')


def multi_return(x, y):
    # multiple return values are packages into tuple
    return x**2, y**2


x = multi_return(2, 3)
print(isinstance(x, tuple))  # prints True


# Nested functions

def pairs_between(x, y):

    def _evens():
        return [i for i in range(x, y) if i % 2 == 0]

    def _odds():
        return [i for i in range(y, x, -1) if i % 2 != 0]

    return zip(_evens(), _odds())


print(list(pairs_between(0, 10)))


# `global` vs `local` vs `nonlocal` scopes

gx = 1  # global variable


def a():
    # gx is lookup within local scope, but not found
    # moves on to lookup at the global scope
    print(gx)


a()  # prints 1


def b():
    # defining a local variable
    gx = 2
    print(gx)


b()  # prints 2

# global variable not mutated
print(gx)  # prints 1


def c():
    # binding gx from global scope so it can be mutated
    global gx
    gx = 3
    print(gx)


c()  # prints 3
print(gx)  # prints 3
gx = 4
print(gx)  # prints 4


def d():
    gx = 1

    def d1():
        # refernce the gx from `d` local scope
        nonlocal gx
        gx = 3
    d1()
    print(gx)


d()  # prints 3
print(gx)  # prints 4


# Non-literal variables are passed as reference

y = [1, 2, 3]
z = {0: 'a', 1: 'b'}


def e(n):
    n[0] = '🎄'


e(y)
print(y[0])  # prints 🎄

e(z)
print(z[0])  # prints 🎄


def call(f):
    """Anything can be passed as an argument"""
    return f()


call(a)  # prints 4
call(b)  # prints 2
