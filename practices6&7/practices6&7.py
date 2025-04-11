# Practices 6&7. Binary Search Tree Operations
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'
SEARCH = 'S'
INSERT = 'I'
DELETE = 'D'
INORDER = 'N'
PREORDER = 'R'
POSTORDER = 'O'

# Node implementation
class TreeNode:
  def __init__(self, k, l=None, r=None):
    self.key = k
    self.left = l
    self.right = r

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # Return True if tree is empty; False otherwise
  def isEmpty(self):
    return self.root == None

  # Given a sequence arr of integers, start index l, the end index r, 
  # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
  # Return the root node of the tree
  def arrayToBST(self, arr, l, r): # time complexity: O(n)
    # Practice 5
    for i in range(len(arr)-1):  # time complexity: O(n)
      if arr[i] > arr[i+1]:
        return None
    if l > r:
      return None
    mid = (l + r) // 2
    root = TreeNode(arr[mid])
    root.left = self.arrayToBST(arr, l, mid - 1)
    root.right = self.arrayToBST(arr, mid + 1, r)
    return root

  # Return the node with the minimum value 
  def findMin(self): # time complexity: O(n)
    # Practice 5
    if not self.root:
      return None
    current = self.root
    while current.left:
      current = current.left
    return current

  # Return the node with the maximum value 
  def findMax(self): # time complexity: O(n)
    # Practice 5
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

  # Given a query, search for the node whose key is equal to query.
  # If the node exists, return the key
  # Otherwise, return nullptr  
  def search(self, query): # time complexity: O(n)
    # Practice 6
    current = self.root
    def s(current, query): # time complexity: O(n)
      if current is None:
        return None
      if current.key == query:
        return current
      elif query < current.key:
        return s(current.left, query)
      else:
        return s(current.right, query)
    return s(current, query)
  
  # Given an output file, write the keys of all the nodes 
  # visited in inorder traversal
  def writeInorder(self, outFile): # time complexity: O(n)
    # Practice 6
    def inorder(node): # time complexity: O(n)
      if node is not None:
        inorder(node.left)
        outFile.write(str(node.key) + " ")
        inorder(node.right)
    inorder(self.root)
    outFile.write("\n")
    
  # Given an output file, write the keys of all the nodes 
  # visited in preorder traversal
  def writePreorder(self, outFile): # time complexity: O(n)
    # Practice 6
    def preorder(node): # time complexity: O(n)
      if node is not None:
        outFile.write(str(node.key) + " ")
        preorder(node.left)
        preorder(node.right)
    preorder(self.root)
    outFile.write("\n")
    
  # Given an output file, write the keys of all the nodes 
  # visited in postorder traversal
  def writePostorder(self, outFile): # time complexity: O(n)
    # Practice 6
    def postorder(node): # time complexity: O(n)
      if node is not None:
        postorder(node.left)
        postorder(node.right)
        outFile.write(str(node.key) + " ")
    postorder(self.root)
    outFile.write("\n")

  # If node with key k alreay exists in the tree, do nothing
  # Otherwise, insert new node with key k 
  def insertNode(self, k): # time complexity: O(n)
    # Practice 7
    def insert(current, k): # time complexity: O(n)
      if current is None:
        return TreeNode(k)
      elif k < current.key:
        current.left = insert(current.left, k)
      elif k > current.key:
        current.right = insert(current.right, k)
      return current
    self.root = insert(self.root, k)

  # If deletion fails, immediately terminate the program
  # Otherwise, delete the node with key k
  def deleteNode(self, k): # time complexity: O(n)
    # Practice 7
    def delete(current, k): # time complexity: O(n)
      if current is None:
        return current
      if k < current.key:
        current.left = delete(current.left, k)
      elif k > current.key:
        current.right = delete(current.right, k)
      else:
        if current.left is None:
          return current.right
        elif current.right is None:
          return current.left
        successor = current.right
        while successor.left:
          successor = successor.left
        current.key = successor.key
        current.right = delete(current.right, successor.key)
      return current       
    self.root = delete(self.root, k)

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
      elif op == SEARCH:
        if len(words) != 2:
          raise Exception("SEARCH: invalid input")
        k = int(words[1])
        # Practice 6. Call the function for search
        found = tree.search(k)
        if found:
          outFile.write(str(found.key) + "\n")
        else:
          raise Exception("Search failed")
      elif op == INORDER:
        # Practice 6. Call the function for inorder traversal
        tree.writeInorder(outFile)
      elif op == PREORDER:
        # Practice 6. Call the function for preorder traversal
        tree.writePreorder(outFile)
      elif op == POSTORDER:
        # Practice 6. Call the function for postorder traversal
        tree.writePostorder(outFile)
      elif op == INSERT:
        if len(words) != 2:
          raise Exception("INSERT: invalid input")
        k = int(words[1])
        # Practice 7. Call the function for insertion
        tree.insertNode(k)
        outFile.write(f"{INSERT} {k}\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        k = int(words[1])
        # Practice 7. Call the function for deletion
        found = tree.search(k)
        if not found:
          raise Exception("Delete failed")
        tree.deleteNode(k)
        outFile.write(f"{DELETE} {k}\n")
      else:
        raise Exception("Undefined operator")
        
