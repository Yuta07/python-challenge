import random

list = random.sample(range(20), k = 20)
print(list)

def insertionSort(data, limit):
    for i in range(1, limit):
        x = data[i]
        j = i

        while j > 0 and data[j - 1] > x:
            data[j] = data[j - 1]
            
            j -= 1
        
        data[j] = x

    return data

result = insertionSort(list, len(list))
print(result)