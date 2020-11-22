def uni(s: int, e: int, values_only=True):
    for i in range(s, e):
        if values_only:
            yield chr(i)
        else:
            yield r'\u{}'.format(i), chr(i)


chess = uni(9812, 9823)
print(type(chess).__name__ == 'generator')
print(tuple(chess))


def a():
    yield 1
    yield 2


x = a()
print(next(x))
print(next(x))
