import random
from typing import List

list = random.sample(range(20), k = 20)
print(list) 

def partition(data: List[int], low: int, high: int):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
  
    data[i + 1], data[high] = data[high], data[i + 1]

    return i + 1

def quickSort(data: List[int], low: int, high: int):    
    if len(data) <= 1:
        return data          

    if low < high:
        posi = partition(data, low, high)
        quickSort(data, low, posi - 1)
        quickSort(data, posi + 1, high)
    
    return data

result = quickSort(list, 0, len(list) - 1)
print(result)
