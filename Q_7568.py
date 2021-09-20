# input
n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))
rank = [1] * n

# check the rank for n times
for i in range(n):
  pivot = data[i]
  for j in range(n):
    tmp = data[j]
    if pivot[0] < tmp[0] and pivot[1] < tmp[1]:
      rank[i] += 1

# print
for num in rank:
  print(num, end = ' ')