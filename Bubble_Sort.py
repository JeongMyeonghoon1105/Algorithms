arr = []

while True:
  data = input('입력 : ')
  
  if data == 'q' or data == 'Q':
    break
  else:
    arr.append(int(data))

temp = 0

for i in range(len(arr)):
  for index in range(len(arr)-1):
    if arr[index] > arr[index+1]:
      temp = arr[index+1]
      arr[index+1] = arr[index]
      arr[index] = temp

print('\n정렬 결과 :', end=' ')
print(arr)
