T = int(input())
test_cases = list(tuple(map(int, input().split())) for _ in range(T))
N = 30

# dp : combinations
dp = [[0 for i in range(N)] for j in range(N)]

# dp array
dp[1][0], dp[1][1] = 1, 1
for i in range(2,N):
  for j in range(i+1):
    if(j == 0):
      dp[i][j] = 1
    else:
      dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

# print result
for test_case in test_cases:
  (r, n) = test_case
  print(dp[n][r])
