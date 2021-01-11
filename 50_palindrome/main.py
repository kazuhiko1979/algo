"""
1.  Check palindrome
aba => True
abc => False
racecar => True

2. Find palindrome
abcracecarbda => cec, aceca, racecar

racecar
"""

# s = 'test'
# print(s == ''.join(reversed(s)))
# print(s == s[::-1])


def is_palindrome(strings: str) -> bool:
    len_strings = len(strings)
    if not len_strings:
        return False
    if len_strings == 1:
        return True

    start, end = 0, len_strings - 1
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True

from typing import Generator


def find_palindrome(strings: str, left: int, right: int) -> Generator[str, None, None]:
    # result = []
    while 0 <= left and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        # aba, left 0, right 2
        # racecar

        # result.append(strings[left: right+1])

        yield strings[left: right+1]

        left -= 1
        right += 1

    # return result


def find_all_palindrome(strings: str) -> Generator[str, None, None]:
    # result = []
    len_strings = len(strings)
    if not len_strings:
        yield
        # return result
    if len_strings == 1:
        yield strings
        # result.append(strings)

    # aba
    # abba
    for i in range(1, len_strings - 1):
        yield from find_palindrome(strings, i-1, i)
        yield from find_palindrome(strings, i-1, i+1)

        # [result.append(s) for s in find_palindrome(strings, i-1, i)]
        # [result.append(s) for s in find_palindrome(strings, i-1, i+1)]

    # return result


if __name__ == '__main__':
    for s in find_all_palindrome('jabaafafajreajfa;jra'):
        print(s)














