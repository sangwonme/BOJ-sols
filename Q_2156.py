n = int(input())
data = list(int(input()) for _ in range(n))

dp = []
for i in range(len(data)):
  if i == 0:
    dp.append(data[0])
  elif i == 1:
    dp.append(data[1] + data[0])
  elif i == 2:
    max_sum = max(data[i] + data[i-1], data[i] + dp[i-2], dp[i-1])
    dp.append(max_sum)
  else:
    max_sum = max(data[i] + data[i-1] + dp[i-3], data[i] + dp[i-2], dp[i-1])
    dp.append(max_sum)

print(dp[-1])