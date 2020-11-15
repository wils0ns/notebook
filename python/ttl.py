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
