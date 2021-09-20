n, m = map(int, input().split())

# dp : combinations
dp = [[0 for i in range(n+1)] for j in range(n+1)]

# dp array
dp[1][0], dp[1][1] = 1, 1
for i in range(2,n+1):
  for j in range(i+1):
    if(j == 0):
      dp[i][j] = 1
    else:
      dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[n][m])