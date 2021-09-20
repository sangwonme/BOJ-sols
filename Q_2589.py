from collections import deque

# input
m, n = map(int, input().split())
map_data = [list(input()) for _ in range(m)]
visited = [[False for i in range(n)] for j in range(m)]

# direction 
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# init visited
def init():
  for i in range(m):
    for j in range(n):
      visited[i][j] = False

# bfs
def bfs(start):
  x, y = start
  distance, temp = 0, 0
  queue = deque([[x, y, temp]])
  visited[x][y] = True
  while queue:
    x, y, temp = queue.popleft()
    distance = max(distance, temp)
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not((0 <= nx < m) and (0 <= ny < n)):
        continue
      if map_data[nx][ny] == 'W':
        continue
      if not visited[nx][ny]:
        queue.append([nx, ny, temp + 1])
        visited[nx][ny] = True
  return distance

# find ans
distances = []
for i in range(m):
  for j in range(n):
    # optimize
    if (0 < i < m-1) and (map_data[i-1][j] == 'L') and (map_data[i+1][j] == 'L'):
      continue
    if (0 < j < n-1) and (map_data[i][j-1] == 'L') and (map_data[i][j+1] == 'L'):
      continue
    if map_data[i][j] == 'L':
      init()
      distances.append(bfs([i,j]))
print(max(distances))