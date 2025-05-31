# Practice 13. Sorting 
import sys
MERGE_SORT = 'M'
QUICK_SORT = 'Q'

def readInput(line, size):
  words = line.split()
  assert(len(words) == size)
  arr = [int(word) for word in words]
  return arr

def merge(arr, left, mid, right):
  L = arr[left:mid+1]
  R = arr[mid+1:right+1]
  i = j = 0
  k = left
  while i < len(L) and j < len(R):
    if L[i] >= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1
  while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1

def merge_sort(arr, left, right):
  if left < right:
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def partition(arr, low, high):
  x = arr[high]
  left, right = low, high
  while left < right:
    while left < right and arr[left] > x:
      left += 1
    while left < right and arr[right] <= x:
      right -= 1
    if left < right:
      arr[left], arr[right] = arr[right], arr[left]
  arr[high] = arr[left]
  arr[left] = x
  return left

def quick_sort(arr, left, right):
  if left < right:
    p = partition(arr, left, right)
    quick_sort(arr, left, p-1)
    quick_sort(arr, p+1, right)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      words = lines[i].split()
      op = words[0]
      if len(words) != 2:
        raise Exception("Error: invalid input")
      size = int(words[1])
      i += 1
      arr = readInput(lines[i], size)
      if op == MERGE_SORT:
        if len(words) != 2:
          raise Exception("MERGE_SORT: invalid input")
        merge_sort(arr, 0, size - 1)
        outFile.write(' '.join(map(str, arr)) + '\n')
      elif op == QUICK_SORT:
        if len(words) != 2:
          raise Exception("QUICK_SORT: invalid input")
        quick_sort(arr, 0, size - 1)
        outFile.write(' '.join(map(str, arr)) + '\n')
      else:
        raise Exception("Undefined operator")
      i += 1

