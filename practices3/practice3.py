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
    self.size = 0
    
  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def addStudent(self, newID, newName):
    if self.find(newID):
      return False
    
    newStudent = Student(newID, newName)
    if self.isEmpty() or newID < self.head.id:
      newStudent.next = self.head
      self.head = newStudent
    else:
      prve = None
      current = self.head
      while current and current.id < newID:
        prve = current
        current = current.next
      
      newStudent.next = current
      prve.next = newStudent
    
    self.size += 1
    return True
  
  def deleteStudent(self, queryID):
    prev, curr = None, self.head
    while curr and curr.id!= queryID:
      prev, curr = curr, curr.next

    if not curr:
      return False
    
    if not prev:
      self.head = curr.next
    else:
      prev.next = curr.next
    
    self.size -= 1
    return True

  def find(self, queryID):
    curr = self.head
    while curr:
      if curr.id == queryID:
        return curr
      curr = curr.next
    return None

  def write(self, outFile):
    result = []
    curr = self.head
    while curr:
      result.append(f"{curr.id} {curr.name}")
      curr = curr.next
    outFile.write(" ".join(result) + "\n")

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
          raise Exception("Find: invalid input")
        i = int(words[1])
        found = course.find(i)
        if not found:
          outFile.write("Search failed\n")
        else:
          outFile.write(str(found.id) + " " + found.name + "\n")
      else:
        raise Exception("Undefined operator")