# Data input
n, m = map(int, input().split())
data = list(map(int, input().split()))

# start, end value init
start = min(data)
end = int(1e9)

# binary search
while start < end:
  mid = (start + end) // 2
  count, temp = 1, 0
  # for each tape, accumulate its length until it exceed mid
  for x in data:
    if x > mid:
      count = m + 1
      break
    temp += x
    if temp > mid:
      count += 1
      temp = x
  if count > m:
    start = mid + 1
  else:
    end = mid

# print ans
print(start)
