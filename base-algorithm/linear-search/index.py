print('Num: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
print('input Num...')

def linearSearch(target: str):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in list:
        print(list[i], target)

        if list[i] == int(target):
            return i

targetNum: int = input('>> ')
result: int = linearSearch(targetNum)

print('array num is', result)