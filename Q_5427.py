from collections import deque

# direction arr
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# test case
t = int(input())
for test_case in range(t):
  # input
  w, h = map(int, input().split())
  data = list(list(input()) for _ in range(h))
  visited = [[False for i in range(w)] for j in range(h)]
  # find fire and start points
  fire = deque()
  start = [0, 0]
  for i in range(h):
    for j in range(w):
      if data[i][j] == '*':
        fire.append([i, j])
      elif data[i][j] == '@':
        start = [i, j]
  # bfs
  x, y = start
  queue = deque([[x, y, 0]])
  visited[x][y] = True
  result, current_dist = 'IMPOSSIBLE', -1
  while queue:
    x, y, dist = queue.popleft()
    # if endpoint return dist + 1
    if x == 0 or x == h-1 or y == 0 or y == w-1:
      result = dist + 1
      break
    # fire move
    fire_cnt, current_dist = [len(fire), dist] if dist > current_dist else [0, current_dist]
    for fire_point in range(fire_cnt):
      fx, fy = fire.popleft()
      for i in range(4):
        nfx, nfy = fx + dx[i], fy + dy[i]
        if not(0 <= nfx < h and 0 <= nfy < w):
          continue
        if data[nfx][nfy] == '.' or data[nfx][nfy] == '@':
          data[nfx][nfy] = '*'
          fire.append([nfx, nfy])
    # me move
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not (0 <= nx < h and 0 <= ny < w):
        continue
      if not visited[nx][ny] and data[nx][ny] == '.':
        queue.append([nx, ny, dist + 1])
        data[nx][ny] = '@'
        visited[nx][ny] = True

  # print
  print(result)