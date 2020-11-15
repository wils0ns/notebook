from functools import lru_cache
from wrappers import timer


@lru_cache
def factorial(n: int) -> int:
    return n * factorial(n-1) if n else 1


@timer
def main():
    for i in range(1, 100):
        print(factorial(i))


if __name__ == '__main__':
    main()
