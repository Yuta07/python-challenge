import math

print('Num: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
print('input Num...')

def binarySearch(target: str):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    head = 0
    tail = len(list)
    count = 0

    while True:
        center: int = math.floor((head + tail) / 2)
        count += 1

        if list[center] == int(target):
            print('count', count)

            return center
        else:
            if list[center] < int(target):
                head = center + 1
            else:
                tail = center - 1

targetNum: int = input('>> ')
result: int = binarySearch(targetNum)

print('array num is', result)