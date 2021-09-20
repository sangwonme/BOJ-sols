from sys import stdin
from collections import deque

queue = deque()

# method
def queueMethod(operation):
  op = operation[0]
  if op == 'push':
    queue.append(int(operation[1]))
  elif op == 'pop':
    print(queue.popleft() if queue else -1)
  elif op == 'size':
    print(len(queue))
  elif op == 'empty':
    print(0 if queue else 1)
  elif op == 'front':
    print(queue[0] if queue else -1)
  elif op == 'back':
    print(queue[-1] if queue else -1)

# operation
n = int(stdin.readline())
for i in range(n):
  operation = list(stdin.readline().split())
  queueMethod(operation)
