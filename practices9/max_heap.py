# Practice 9. Max Heap
import sys
INSERT = 'I'
DELETE = 'D'
MAXIMUM = 'M'
MAX_CAPACITY = 1000
INT_MIN = -sys.maxsize

class MaxHeap:
  def __init__(self, num=MAX_CAPACITY):
    self.elements = [0] * num
    self.count = 0
    self.capacity = num

  # Given the index i of element, return the index of that element's parent in the heap
  def parent(self, i):
    return (i - 1) // 2
  
  # Given the index i of element, return the index of that element's left child in the heap
  def left(self, i):
    left = 2 * i + 1
    return -1 if left > self.count else left
  
  # Given the index i of element, return the index of that element's right child in the heap
  def right(self, i):
    right = 2 * i + 1
    return -1 if right > self.count else right

  # Insert a given element elem into the heap
  # If the insertion fails, immediately terminate the program with the error message.
  def insertElement(self, elem):
      if self.count >= self.capacity:
        raise Exception("full heap")
      i = self.count
      p = self.parent(i)
      while i > 0 and self.elements[p] < elem:
        self.elements[i] = self.elements[p]
        i = p
        p = self.parent(i)
      self.elements[i] = elem
      self.count += 1
      
  # Return the maximum of the heap if it exists
  # Otherwise, terminate program with an error
  def maximum(self):
    if self.count == 0:
      raise Exception("no elements")
    return self.elements[0]

  # Delete the maximum from the heap and return the maximum
  # If deletion fails, terminate program with an error
  def deleteMaximum(self):
    if self.count == 0:
      raise Exception("no elements")
    largest = self.elements[0]
    self.elements[0] = self.elements[self.count - 1]
    self.count -= 1
    self.maxHeapify(0)
    return largest

  def maxHeapify(self, i):
      l = self.left(i)
      r = self.right(i)
      if l != -1 and self.elements[l] > self.elements[i]:
        largest = l
      else:
        largest = i
      if r != -1 and self.elements[r] > self.elements[largest]:
        largest = r
      if largest != i:
        temp = self.elements[i]
        self.elements[i] = self.elements[largest]
        self.elements[largest] = temp
        self.maxHeapify(largest)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  h = MaxHeap()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == INSERT:
        if len(words) != 2:
          raise Exception("INSERT: invalid input")
        i = int(words[1])
        # Call the insertion method
        h.insertElement(i)
        # If the insertion succeeds, write every element in the array into output file.
        outFile.write(' '.join(map(str, h.elements[:h.count])) + '\n')

      elif op == DELETE:
        # Call the deletion method
        h.deleteMaximum()
        # If the deletion succeeds, write every element in the array into output file.
        outFile.write(' '.join(map(str, h.elements[:h.count])) + '\n')

      elif op == MAXIMUM:
        # Call the function to get the maximum
        maximum = h.maximum()
        # If getting the maximum succeeds, write the maximum into output file.
        outFile.write(str(maximum) + '\n')
        
      else:
        raise Exception("Undefined operator")
        