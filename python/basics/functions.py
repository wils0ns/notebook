# built-in functions

print('Hi!')
eval("print('Hi!')")

# Define custom functions


def my_func():
    """
    my_func is a function that takes no arguments and does nothing.
    Use triple-double-quotes blocks to write a docstring.
    """
    pass


def example(): pass  # This function does nothing and has no docstring.


def real_func():
    """
    This function only executes something and returns None.
    Functions in python always returns None, by default.
    """
    print('Hello from real func!')


return_from_real_func = real_func()
print(return_from_real_func is None)


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
    _sum = 0
    for i in n:
        _sum += i
    return _sum


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
