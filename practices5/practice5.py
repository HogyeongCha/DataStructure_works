# Practice 5. Binary Search Tree
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'

# Node implementation
class TreeNode:
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # Return True if tree is empty; False otherwise
  def isEmpty(self):
    return self.root == None

  # Given a sequence arr of integers, start index l, the end index r, 
  # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
  # Return the root node of the tree
  def arrayToBST(self, arr, l, r):
    # I used the following method to know that the array is sorted, but it has too much time-complexity, so I used this code to do so.
    # if arr != sorted(arr):
    #   return None
    for i in range(len(arr)-1): # It takes O(n) time-complexity.
      if arr[i] > arr[i+1]:
        return None
    # I didn't want to include the sorting code here, but I did it to do not touch the main function.

    if l > r: # It takes O(n) time-complexity. -> It is called whenever this recursive function runs (n * O(n) -> O(n^2))
      return None
    mid = (l + r) // 2
    root = TreeNode(arr[mid])
    root.left = self.arrayToBST(arr, l, mid - 1)  # arrayToBST is called recursively
    root.right = self.arrayToBST(arr, mid + 1, r)
    return root
# Finally, this recursive function takes O(n^2) time-complexity.
# If the sorting function is on the out of this recursive function, it can takes only O(n) time-complexity maybe.

  # Return the node with the minimum value 
  def findMin(self):  # It takes O(logn) time-complexity because this BST is balanced.
    # For the case of unbalanced BST, It takes O(n) time-complexity to find the minimum value.
    if not self.root:
      return None
    current = self.root
    while current.left:
      current = current.left
    return current

  # Return the node with the maximum value
  def findMax(self):  # likewise, O(logn)
    if not self.root:
      return None
    current = self.root
    while current.right:
      current = current.right
    return current

  def _getHeight(self, curr):
    if not curr:
      return 0
    return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

  def _printSpaces(self, n, curr):
    for i in range(int(n)):
      print("  ", end="")
    if not curr:
      print(" ", end="")
    else:
      print(str(curr.key), end="")

  def printTree(self):
    if not self.root:
      return 
    q = deque()
    q.append(self.root)
    temp = deque()
    cnt = 0
    height = self._getHeight(self.root) - 1
    nMaxNodes = 2**(height + 1) - 1
    while cnt <= height:
      curr = q.popleft()
      if len(temp) == 0:
        self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
      else:
        self._printSpaces(nMaxNodes / (2**cnt), curr)
      if not curr:
        temp.append(None)
        temp.append(None)
      else:
        temp.append(curr.left)
        temp.append(curr.right)
      if len(q) == 0:
        print("\n")
        q = temp
        temp = deque()
        cnt += 1
        

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  tree = BinarySearchTree()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == BUILD:
        data = [int(s) for s in words[1:]]
        tree.root = tree.arrayToBST(data, 0, len(data) - 1)
        if tree.root:
          outFile.write(BUILD + "\n")
          tree.printTree()
        else:
          raise Exception("BUILD: invalid input")
      elif op == FIND_MIN:
        found = tree.findMin()
        if not found:
          raise Exception("FindMin failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == FIND_MAX:
        found = tree.findMax()
        if not found:
          raise Exception("FindMax failed")
        else:
          outFile.write(str(found.key) + "\n")
      else:
        raise Exception("Undefined operator")
        
