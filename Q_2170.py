# input
n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))

# sort by starting pt
data.sort(key = lambda x: x[0])

# connected if next start point place on left of the current end point
start, end = data[0]
length = 0
for i in range(1, len(data)):
  x, y = data[i]
  if x <= end:
    end = max(y, end)
  else:
    length += (end - start)
    start, end = x, y
length += (end - start)

print(length)