# input
m, n, k = map(int, input().split())

# make map
map_data = [[True for i in range(n)] for j in range(m)]
for domain in range(k):
  yi, xi, yf, xf = map(int, input().split())
  for x in range(xi, xf):
    for y in range(yi, yf):
      map_data[x][y] = False

# visited arr
visited = [[False for i in range(n)] for j in range(m)]

# direction case
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# dfs
def dfs(start):
  x, y = start
  stack = [start]
  count = 1
  visited[x][y] = True
  while stack:
    x, y = stack.pop()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      if visited[nx][ny] or not map_data[nx][ny]:
        continue
      stack.append([nx, ny])
      visited[nx][ny] = True
      count += 1
  return(count)

# find answer
answer = []
for i in range(m):
  for j in range(n):
    if not visited[i][j] and map_data[i][j]:
      answer.append(dfs([i, j]))

# print answer
answer.sort()
print(len(answer))
for num in answer:
  print(num, end=' ')