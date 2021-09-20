N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
visited = [[False for i in range(N)] for j in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Find max height
max_height = max(map(max, graph))

# initialize visted arr
def init():
  for i in range(N):
    for j in range(N):
      visited[i][j] = False

# DFS by iteration
def dfs(x, y, height):
  if graph[x][y] <= height or visited[x][y]:
    return False
  stack = []
  stack.append((x,y))
  visited[x][y] = True
  while stack:
    (vx, vy) = stack.pop()
    for i in range(4):
      (nx, ny) = (vx + dx[i], vy + dy[i])
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        pass
      elif graph[nx][ny] <= height:
        pass
      elif not visited[nx][ny]:
        stack.append((nx,ny))
        visited[nx][ny] = True
  return True

# Find max_count
count = [0 for i in range(max_height)]
for height in range(max_height):
  for i in range(N):
    for j in range(N):
      if dfs(i, j, height):
        count[height] += 1
  init()
print(max(count))