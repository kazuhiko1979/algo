from typing import List


def counting_sort(numbers: List[int]) -> List[int]:
    max_number = max(numbers)
    counts = [0] * (max_number + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1
    # print(counts)

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    # print(counts)

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [4, 3, 6, 2, 3, 4, 7]
    print(counting_sort(nums))

