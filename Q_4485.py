import heapq

# direction arr
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# while input != 0
n, problem = int(input()), 1
while n != 0:
  # input
  data = list(list(map(int, input().split())) for _ in range(n))

  # init distance array
  distance = [[int(1e9) for i in range(n)] for j in range(n)]
  distance[0][0] = data[0][0]
  # dijkstra
  heap = []
  heapq.heappush(heap, [distance[0][0], 0, 0])
  while heap:
    dist, x, y = heapq.heappop(heap)
    if dist > distance[x][y]:
      continue
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not(0 <= nx < n and 0 <= ny < n):
        continue
      cost = dist + data[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(heap, [cost, nx, ny])

  # print ans
  print('Problem ' + str(problem) + ': ' + str(distance[n-1][n-1]))
  # next input
  n = int(input())
  problem += 1