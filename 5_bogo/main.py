# Big O notation Example

def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)


def func3(numbers):
    for num in numbers:
        print(num)


def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <=1:
        return
    func4(n/2)


def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()


func5([1, 2, 3, 4, 5])










