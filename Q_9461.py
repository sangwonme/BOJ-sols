# input
t = int(input())
n = list(int(input()) for _ in range(t))
p = [0] * (max(n) + 1)

# caculate sequence in range of max(n)
hexagon = [1, 0, 1, 0, 1, 0]
for i in range(len(p)):
  if i == 0:
    continue
  elif i == 1:
    p[i] = 1
  else:
    max_length = max(hexagon)
    max_idx = hexagon.index(max_length)
    p[i] = max_length
    hexagon[max_idx] = 0
    hexagon[(max_idx + 1) % 6] += max_length
    hexagon[(max_idx - 1) % 6] += max_length

# print answer
for i in n:
  print(p[i])
