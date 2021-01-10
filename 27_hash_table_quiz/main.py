# 指定したパラメータになるよう、
# リスト内から足し合わせた数字を表示させる
"""
1. Input: [11, 2, 5, 9, 10, 3], 12  => Output: (2, 10) or None
2. Input: [11, 2, 5, 9, 10, 3], 20  => Output: (11, 9) or None ex ) 11 + 9 = 2 + 5 + 10 + 3
"""
from typing import List, Tuple, Optional


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)

    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return

    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)


if __name__ == '__main__':
    l = [11, 2, 5, 9, 10, 3]
    # l = [11, 2]
    t = 12
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 10, 3]
    print(get_pair_half_sum(l))


