import heapq
heap = []

# input
n = int(input())
for i in range(n):
  heapq.heappush(heap, int(input()))

# pop 2 element at front, sum and push
result = 0
while len(heap) > 1:
  x, y = heapq.heappop(heap), heapq.heappop(heap)
  result += x + y
  heapq.heappush(heap, x + y)
print(result)