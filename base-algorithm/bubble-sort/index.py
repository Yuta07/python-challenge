import random

list = random.sample(range(20), k = 20)
print(list)

def bubbleSort(data, limit):
  for i in range(limit):
    for j in range(1, limit - i):
      if data[-j] < data[-j - 1]:
        data[-j], data[-j - 1] = data[-j - 1], data[-j]
  
  return data

result = bubbleSort(list, len(list))
print(result)