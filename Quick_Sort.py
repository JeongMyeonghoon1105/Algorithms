def quick(pivot, arr):
  if len(arr) == 0:
    return 
  elif len(arr) == 1:
    return arr[0]
  
  i = 0
  j = pivot - 1
  temp = 0
  
  while (i <= j):
    # 교환
    if arr[i] > arr[pivot] and arr[j] < arr[pivot]:
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp
      
      i = i + 1
      j = j - 1

    # 증가 - 감소
    elif arr[i] <= arr[pivot] and arr[j] >= arr[pivot]:
      i = i + 1
      j = j - 1

    # 증가 - 정지
    elif arr[i] <= arr[pivot] and arr[j] < arr[pivot]:
      i = i + 1

    # 정지 - 감소
    elif arr[j] >= arr[pivot] and arr[i] > arr[pivot]:
      j = j - 1
    
  temp = arr[pivot]
  arr[pivot] = arr[i]
  arr[i] = temp
  pivot = i

  prev = quick(pivot-1, arr[:pivot])
  if prev != None:
    print(prev, end = ' ')
  
  print(arr[pivot], end = ' ')

  post = quick(len(arr[pivot+1:])-1, arr[pivot+1:])
  if post != None:
    print(post, end = ' ')

arr = []
data = ''

while True:
  data = input('입력 : ')
  
  if data == 'q' or data == 'Q':
    break
  else:
    arr.append(int(data))

pivot = len(arr) - 1
print('\n정렬 결과 :', end = ' ')
quick(pivot, arr)