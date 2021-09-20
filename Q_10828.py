from sys import stdin

stack = []

# method
def stackMethod(operation):
  op = operation[0]
  if op == 'push':
    stack.append(int(operation[1]))
  elif op == 'pop':
    print(stack.pop() if stack else -1)
  elif op == 'size':
    print(len(stack))
  elif op == 'empty':
    print(0 if stack else 1)
  elif op == 'top':
    print(stack[-1] if stack else -1)

# operation
n = int(stdin.readline())
for i in range(n):
  operation = list(stdin.readline().split())
  stackMethod(operation)
