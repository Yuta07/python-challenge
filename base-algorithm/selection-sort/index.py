import random

list = random.sample(range(20), k = 20)
print(list)

min = 0

def selectionSort(data, limit):
  for i in range(limit):
    min = i

    for j in range(i + 1, limit):
      if data[min] > data[j]:
        min = j
      
    data[i], data[min] = data[min], data[i]
  
  return data

result = selectionSort(list, len(list))
print(result)