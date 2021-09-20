import heapq

# input
n, m = map(int, input().split())
data = list(list(map(int, list(input()))) for _ in range(m))

# direction
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dijkstra - set distance, push start
distance = [[int(1e9) for i in range(n)] for j in range(m)]
heap = []
heapq.heappush(heap, [0, 0, 0])
distance[0][0] = 0
# dijkstra
while heap:
  dist, x, y = heapq.heappop(heap)
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if not (0 <= nx < m and 0 <= ny < n):
      continue
    cost = dist + data[nx][ny]
    if cost < distance[nx][ny]:
      heapq.heappush(heap, [cost, nx, ny])
      distance[nx][ny] = cost

print(distance[m-1][n-1])
