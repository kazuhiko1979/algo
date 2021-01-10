# cock_tail sort

from typing import List


def cocktail_list(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


if __name__ == '__main__':
    import random
    list = [4, 1, 8, 5, 3, 7]
    nums = [random.randint(0, 1000) for i in range(10)]
    print(cocktail_list(nums))




