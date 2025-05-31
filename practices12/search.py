# Practice 12. Search
import sys
BINARY_SEARCH = 'B'
PERFECT_SQUARE = 'P'

class searchSolution:
  def __init__(self, arr=[]):
    self.arr = arr
  def addArr(self, arr):
    self.arr = arr
  def binarySearch(self, start, finish, target):
    if start > finish:
      return 'N'
    mid = (start + finish) // 2
    if self.arr[mid] == target:
      return mid
    if self.arr[mid] < target:
      return self.binarySearch(mid + 1, finish, target)
    elif self.arr[mid] > target:
      return self.binarySearch(start, mid - 1, target)
  def perfectSquare(self, num):
    self.arr=[i*i for i in range(0, num + 1)]
    found = self.binarySearch(0, len(self.arr) - 1, num)
    if found != 'N':
      if self.arr[found] == num:
        return True
    return False

if __name__ == "__main__":
  S = searchSolution()
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      line = lines[i]
      words = line.split()
      op = words[0]
      if op == BINARY_SEARCH:
        if len(words) != 3:
          raise Exception("BINARY_SEARCH: invalid input")
        size, x = int(words[1]), int(words[2])
        outFile.write(line)
        arr = list(map(int, lines[i+1].split()))
        S.addArr(arr)
        outFile.write(str(S.binarySearch(0, len(arr) - 1, x)) + '\n')
        i += 1
      elif op == PERFECT_SQUARE:
        if len(words) != 2:
          raise Exception("PERFECT_SQUARE: invalid input")
        x = int(words[1])
        outFile.write(('T' if S.perfectSquare(x) else 'F') + '\n')
      else:
        raise Exception("Undefined operator")
      i += 1