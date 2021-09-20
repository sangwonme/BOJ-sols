import heapq
from sys import stdin
n = int(stdin.readline())
heap = []

# max heap by negative value
for i in range(n):
  x = int(stdin.readline())
  if x == 0:
    print(-heapq.heappop(heap) if heap else 0)
  else:
    heapq.heappush(heap, -x)