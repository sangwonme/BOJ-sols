from collections import deque

T = int(input())

# direction of knight
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

# BFS
def bfs(visited, size, start, end):
  x, y = start
  queue = deque([start])
  visited[x][y] = True
  distance = 0
  while queue:
    for tmp in range(len(queue)):
      x, y = queue.popleft()
      if [x, y] == end:
        return distance
      for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= size or ny < 0 or ny >= size:
          continue
        if not visited[nx][ny]:
          queue.append([nx, ny])
          visited[nx][ny] = True
    distance += 1
  return 0 

# Print answer for each test cases
for test_case in range(T):
  l = int(input())
  visited = [[False for i in range(l)] for j in range(l)]
  start = list(map(int, input().split()))
  end = list(map(int, input().split()))
  print(bfs(visited, l, start, end))