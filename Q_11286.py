from sys import stdin
import heapq

# input
n = int(input())

# heap
heap = []
for i in range(n):
  x = int(stdin.readline())
  if x == 0:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  else:
    heapq.heappush(heap, (abs(x), x))