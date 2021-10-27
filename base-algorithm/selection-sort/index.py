print('Num: [10, 3, 19, 12, 24, 15, 26, 7, 4, 9, 20]')

list = [10, 3, 19, 12, 24, 15, 26, 7, 4, 9, 20]
min = 0

for i in range(len(list)):
  min = i
  
  if i > len(list):
    break

  for j in range(i + 1, len(list)):
    if list[min] > list[j]:
      min = j
    
  list[i], list[min] = list[min], list[i]

print(list)