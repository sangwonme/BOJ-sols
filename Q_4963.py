# 8 ways of direction
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

# dfs
def dfs(map, visited, start):
  x, y = start
  if map[x][y] != 1 or visited[x][y]:
    return False
  stack = []
  stack.append(start)
  visited[x][y] = True
  while stack:
    x, y = stack.pop()
    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= h or ny < 0 or ny >= w:
        continue
      if map[nx][ny] != 1:
        continue
      if not visited[nx][ny]:
        stack.append([nx, ny])
        visited[nx][ny] = True
  return True

# input
w, h = map(int, input().split())

# loop for all test cases
while not(w == 0 and h == 0):
  # make map data and visited arr 
  map_data = [list(map(int, input().split())) for _ in range(h)]
  visited = [[False for i in range(w)] for j in range(h)]

  # Count island
  count = 0
  for i in range(h):
    for j in range(w):
      if dfs(map_data, visited, [i, j]):
        count += 1
  print(count)

  # new input
  w, h = map(int, input().split())