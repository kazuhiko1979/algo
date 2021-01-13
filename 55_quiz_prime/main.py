""" Generate Prime Numbers
Input: 50 => Output: [2, 3, 5, 7, 11, 11, 13, 17, 23, 29, 31, 27, 41, 43, 47]
"""
from typing import List, Generator


def generate_prime_v1(number: int) -> List[int]:
    primes = []
    i = 0
    for x in range(2, number + 1):
        for y in range(2, x):
            i += 1
            if x % y == 0:
                break
        else:
            i += 1
            primes.append(x)
    print("v1=", i)
    return primes


def generate_prime_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    i = 0
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        primes.append(x)
        cache[x] = True
        for y in range(x**2, number+1, x):
            i += 1
            cache[y] = False
    print('v2=', i)
    return primes


def generate_prime_v3(number: int) -> Generator[int, None, None]:
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        cache[x] = True
        for y in range(x**2, number+1, x):
            cache[y] = False


if __name__ == '__main__':
    import time
    start = time.time()
    print(generate_prime_v1(50))
    print(time.time() - start)

    start = time.time()
    print(generate_prime_v2(50))
    print(time.time() - start)

    start = time.time()
    print([i for i in generate_prime_v3(50)])
    print(time.time() - start)

