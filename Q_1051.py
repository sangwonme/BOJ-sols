# input
n, m = map(int, input().split())
data = list(list(map(int, input())) for _ in range(n))

# search
result = 1
for size in range(min(n,m), 1, -1):
  for i in range(n - size + 1):
    for j in range(m - size + 1):
      if data[i][j] == data[i][j + size - 1] == data[i + size - 1][j] == data[i + size - 1][j + size - 1]:
        result = size**2
        break
    else:
      continue
    break
  else:
    continue
  break
print(result)