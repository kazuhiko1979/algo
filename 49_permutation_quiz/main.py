# from itertools import permutations
#
# for r in permutations([1, 2, 3]):
#     print(r)
from typing import List, Iterator, Generator


def all_perms(elements: List[int]) -> Iterator[List[int]]:

    # result = []
    # first = elements[0:1]
    # rest = elements[1:]

    # [1, 2, 3]
    # [2, 3]
    # [3]

    # if len(elements) <= 1:
    #     # [[3]]
    #     return [elements]

    if len(elements) <= 1:
        yield elements

    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == '__main__':
    for p in all_perms([1, 2, 3]):
        print(p)
