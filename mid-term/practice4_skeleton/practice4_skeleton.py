# Practice 4. Palindromes and Balance
import sys
from collections import deque

###################################
def isPalindrome(string):
  stack = []
  for s in string:
    stack.append(s)
  for s in string:
    if stack.pop() != s:
      return False
  return True

def balance(string):
  opening = ['(', '{', '[']
  closing = [')', '}', ']']
  match = {}
  for i, ch in enumerate(closing):
    match[ch] = opening[i]
  stack = []
  for ch in string:
    if ch in opening:
      stack.append(ch)
    elif ch in closing:
      if len(stack) == 0 or stack[-1] != match[ch]:
        return False
      stack.pop()
  return len(stack) == 0
###################################

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == 'P':
        if len(words) != 2:
          raise Exception("PALINDROME: invalid input")
        ret = "T" if isPalindrome(words[1]) else "F"
        outFile.write(ret+"\n")
      elif op == 'B':
        if len(words) != 2:
          raise Exception("BALANCE: invalid input")
        ret = "T" if balance(words[1]) else "F"
        outFile.write(ret+"\n")
      else:
        raise Exception("Undefined operator")

        
