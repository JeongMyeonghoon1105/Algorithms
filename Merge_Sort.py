# 합병 정렬 함수
def merge(arr):
  result = []
  
  if len(arr) > 1:
    left = merge(arr[:len(arr)//2])
    right = merge(arr[len(arr)//2:])
    
    count = 0; lf = 0; rf = 0
    while count < len(arr):
      if lf == len(left):
        result.append(right[rf])
        rf = rf + 1
      elif rf == len(right):
        result.append(left[lf])
        lf = lf + 1
      elif left[lf] > right[rf]:
        result.append(right[rf])
        rf = rf + 1
      else:
        result.append(left[lf])
        lf = lf + 1
      count = count + 1

  else:
    result.append(arr[0])

  return result

# 메인 실행 흐름
arr = []

while True:
  data = input('입력 : ')
  
  if data == 'q' or data == 'Q':
    break
  else:
    arr.append(int(data))

print('\n정렬 결과 :', end=' ')
print(merge(arr))