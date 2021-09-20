from collections import deque

# input
r, c = map(int, input().split())
data = list(list(input()) for _ in range(r))

# find s, d, * pos while input
s, d, water_queue = [0, 0], [0, 0], deque()
for i in range(r):
  for j in range(c):
    s = [i, j] if data[i][j] == 'S' else s
    d = [i, j] if data[i][j] == 'D' else d
    if data[i][j] == '*':
      water_queue.append([i, j])

# direction arr
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
x, y = s
path_queue = deque([[x, y, 0]])
visited = [[False for i in range(c)] for j in range(r)]
visited[x][y] = True
have_path, dist = False, -1
while path_queue:
  x, y, current_dist = path_queue.popleft()
  # check if arrived
  if d == [x, y]:
    have_path, dist = True, current_dist
    break
  # water action
  if dist < current_dist:
    dist = current_dist
    it = len(water_queue)
    for _ in range(it):
      wx, wy = water_queue.popleft()
      for i in range(4):
        nwx, nwy = wx + dx[i], wy + dy[i]
        if not(0 <= nwx < r and 0 <= nwy < c):
          continue
        if not data[nwx][nwy] == 'D' and not data[nwx][nwy] == '*' and not data[nwx][nwy] == 'X':
          data[nwx][nwy] = '*'
          water_queue.append([nwx, nwy])
  # find path for 4 directions
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if not(0 <= nx < r and 0 <= ny < c):
      continue
    if not data[nx][ny] == '*' and not data[nx][ny] == 'X' and not visited[nx][ny]:
      path_queue.append([nx, ny, current_dist + 1])
      visited[nx][ny] = True

# print ans
print(dist if have_path else 'KAKTUS')