import sys
ADD = 'A'
DELETE = 'D'
FIND = 'F'

class Student:
  def __init__(self, i, n, p=None):
    self.id = i
    self.name = n
    self.next = p

class Course:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def addStudent(self, newID, newName):
    if self.find(newID):
      return False
    newStudent = Student(newID, newName)
    if self.isEmpty():
      self.head = newStudent
      self.tail = newStudent
    else:
      self.tail.next = newStudent
      self.tail = newStudent
    self.size += 1
    return True

  def deleteStudent(self, queryID):
    if self.isEmpty():
      return False
    prev = None
    curr = self.head
    while curr:
      if curr.id == queryID:
        if prev:
          prev.next = curr.next
        else:
          self.head = curr.next
        if curr == self.tail:
          self.tail = prev
        self.size -= 1
        return True
      prev = curr
      curr = curr.next
    return False

  def find(self, queryID):
    if self.isEmpty():
      return False
    curr = self.head
    while curr:
      if curr.id == queryID:
        return curr
      curr = curr.next
    return False

  def write(self, outFile):
    if not self.isEmpty():
      curr = self.head
      while curr:
        outFile.write(str(curr.id) + " " + curr.name + "\n")
        curr = curr.next
    outFile.write("\n")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  course = Course()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == ADD:
        if len(words) != 3:
          raise Exception("ADD: invalid input")
        i, n = int(words[1]), words[2]
        if course.addStudent(i, n):
          course.write(outFile)
        else:
          outFile.write("Addition failed\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        if course.deleteStudent(i):
          course.write(outFile)
        else:
          outFile.write("Deletion failed\n")
      elif op == FIND:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        found = course.find(i)
        if not found:
          outFile.write("Search failed\n")
        else:
          outFile.write(str(found.id) + " " + found.name + "\n")
      else:
        raise Exception("Undefined operator")
        
