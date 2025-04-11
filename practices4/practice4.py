# Practice 4. Palindromes and Balance
import sys

# Return True if string is a palindrome; False otherwise
def isPalindrome(string): # input : string to check if it is a palindrome or not
  return string == string[::-1] # output : True if it is a palindrome or False it is not
# time complexity : O(n)
# O(n) + O(n) = O(n)
# if string is same with the string that is returned, it returns True
  
# Return True if brackets are balanced in string; False otherwise
def balance(string):  # input : string to check if it is a balanced or not
  stack = []
  brackets = {')': '(', '}': '{', ']': '['}
  for char in string: # loop for each character in string
    if char in brackets.values(): # '(' or '{' or '['
      stack.append(char)
    elif char in brackets: # ')' or '}' or ']'
      if len(stack) != 0 and stack[-1] == brackets[char]:
        stack.pop()
      else:
        return False
  return len(stack)==0  # if stack is empty, it returns True
# output : True if the brackets are balanced or False they are not
# time complexity : O(n)
# O(1) + O(1) + O(n) = O(n)
# When the parentheses are open, we add them to the stack, and when they are closed, we run a pop to determine true/false

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