from collections import deque

# input
f, s, g, u, d = map(int, input().split())

# visited arr. let 0 idx out of range
visited = [False for _ in range(f + 1)]
visited[0] = True

# bfs
queue = deque([[s, 0]])
visited[s] = True
result = -1
while queue:
  current, cost = queue.popleft()
  # endpoint
  if current == g:
    result = cost
    break
  # go up or down
  if current + u <= f and not visited[current + u]:
    queue.append([current + u, cost + 1])
    visited[current + u] = True
  if current - d > 0 and not visited[current - d]:
    queue.append([current - d, cost + 1])
    visited[current - d] = True

# print ans
print(result if result != -1 else 'use the stairs')