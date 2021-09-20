from collections import deque

# input
m, n, h = map(int, input().split())
tomato = []
for i in range(h):
  layer = []
  for j in range(n):
    layer.append(list(map(int, input().split())))
  tomato.append(layer)

# bfs vars
unripen_tomatos = 0
queue = deque()

# directions
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# push ripen tomatos
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k] == 1:
        queue.append([i, j, k, 0])
      elif tomato[i][j][k] == 0:
        unripen_tomatos += 1

# bfs
count = 0
while(queue):
  x, y, z, count = queue.popleft()
  for i in range(6):
    nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
    if not(0 <= nx < h) or not(0 <= ny < n) or not(0 <= nz < m):
      continue
    if tomato[nx][ny][nz] != 0:
      continue
    queue.append([nx, ny, nz, count + 1])
    tomato[nx][ny][nz] = 1
    unripen_tomatos -= 1

# print answer
if unripen_tomatos != 0:
  print(-1)
else:
  print(count)

