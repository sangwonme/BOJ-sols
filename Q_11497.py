t = int(input())
for test_case in range(t):
  # input
  n = int(input())
  data = list(map(int, input().split()))

  # sort
  data.sort()

  # ans = max(data[i+2] - data[i])
  dif = []
  for i in range(n-2):
    dif.append(data[i+2] - data[i])
  print(max(dif))