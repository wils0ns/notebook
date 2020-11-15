# Python

## Table of contents

- [Custom Decorator](#custom-decorator)
- [Caching](#caching)
- [Enum](#enum)
- [Graph](#graph)

## Custom Decorator

```python
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
```

## Caching

Least recently used:

```python
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
```

Time to live:

```python
from time import sleep
import requests
from cachetools import cached, TTLCache

from wrappers import timer


@timer
@cached(cache=TTLCache(maxsize=10, ttl=3))
def get(url):
    return requests.get(url).json()


def main():

    for i in range(5):
        print(get('https://httpbin.org/get'))
        sleep(1)


if __name__ == '__main__':
    main()

```

## Enum

```python
from enum import Enum, auto


class PipelineSteps(Enum):
    CHECKOUT = auto()
    BUILD = auto()
    TEST = auto()
    SAST = auto()
    STAGE_DEPLOY = auto()
    PROD_DEPLOY = auto()
    DAST = auto()


def main():
    print('\n'.join(str(x) for x in PipelineSteps))


if __name__ == '__main__':
    main()
```

## Graph

```python
from graphlib import TopologicalSorter
from enums import PipelineSteps


def main():
    pipeline = {
        PipelineSteps.BUILD: {PipelineSteps.CHECKOUT},
        PipelineSteps.SAST: {PipelineSteps.BUILD},
        PipelineSteps.DAST: {PipelineSteps.STAGE_DEPLOY},
        PipelineSteps.STAGE_DEPLOY: {PipelineSteps.TEST},
        PipelineSteps.PROD_DEPLOY: {
            PipelineSteps.SAST,
            PipelineSteps.DAST,
        },
        PipelineSteps.TEST: {PipelineSteps.BUILD},
        PipelineSteps.CHECKOUT: {},
    }

    sorter = TopologicalSorter(pipeline)
    print('\n'.join(str(x) for x in sorter.static_order()))


if __name__ == '__main__':
    main()
```
