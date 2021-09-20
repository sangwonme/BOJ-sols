from collections import deque

# input
n, m = map(int, input().split())

# graph
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

# input graph info
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

# topology sort
res = []
queue = deque()
# insert node w/ indegree 0
for i in range(1, n + 1):
  if indegree[i] == 0:
    queue.append(i)
# sort
while queue:
  cur = queue.popleft()
  res.append(cur)
  for nxt in graph[cur]:
    indegree[nxt] -= 1
    if indegree[nxt] == 0:
      queue.append(nxt)

# print
for num in res:
  print(num, end = ' ')