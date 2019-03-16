__notes__ = '''

Simple binary search and bubble sort implementation in python

'''


from random import randint as rint

''' Start of Function Definitions '''

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  while left < right:
    mid = left + (right - left) // 2
    if arr[mid] > target:
      right = mid -1
    elif arr[mid] < target:
      left = mid + 1
    else:
      left = mid
      break
  if arr[left] == target:
    return (left, target)
  else:
    return (None, target)

def bubble_sort(arr):
  _arr = arr[:]
  for i in range(0, len(_arr)):
    for j in range(0, len(_arr)-1-i):
      if _arr[j] > _arr[j+1]:
        _arr[j], _arr[j+1] = _arr[j+1], _arr[j]
  return _arr

''' End of Function Definitions '''

''' Start Data Initializations '''

bsearch_test = [_ * 2 for _ in range(100)]
test_elements = [rint(1, 100) for _ in range(10)]

''' End Data Initializations '''

''' Print to stdout values of data '''
print(bsearch_test)
print(test_elements)

sorted_elements = bubble_sort(test_elements)
found = binary_search(bsearch_test, 21)

print(sorted_elements)
print(found)

''' End of program '''
