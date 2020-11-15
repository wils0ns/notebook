from time import perf_counter
from functools import wraps
from typing import Callable
from time import sleep


def timer(func: Callable) -> Callable:
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"{func.__name__!r} executed in {run_time:.4f} secs")
        return value
    return wrapper


@timer
def main():
    print('Hello')
    print('ZzZ...')
    sleep(1)
    print('World.')


if __name__ == '__main__':
    main()
