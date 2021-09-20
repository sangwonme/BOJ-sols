# input
k = int(input())

# stack : pop if input is 0
stack = []
for i in range(k):
  n = int(input())
  if n == 0 and stack:
    stack.pop()
  elif n != 0:
    stack.append(n)

# print ans
print(sum(stack))
