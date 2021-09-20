from sys import stdin

# input
line = stdin.readline().rstrip('\n')
while line != '.':
  # stack for parentheses(=1), brackets(=2)
  stack = []
  res = 'yes'
  for char in line:
    # for open case
    if char == '(' or char == '[':
      stack.append(ord(char) // 10)
    # for close case
    elif char == ')' or char == ']':
      if not stack:
        res = 'no'
        break
      if stack.pop() != ord(char) // 10:
        res = 'no'
        break
  print(res)
  # new input
  line = stdin.readline().rstrip('\n')
    
