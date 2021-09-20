import heapq

# input
x = int(input())

# sticks
sticks = [64]
while sum(sticks) != x:
  tmp = heapq.heappop(sticks)
  if tmp / 2 + sum(sticks) >= x:
    heapq.heappush(sticks, tmp / 2)
  else:
    heapq.heappush(sticks, tmp / 2)
    heapq.heappush(sticks, tmp / 2)
print(len(sticks))