T = int(input())
test_cases = list(int(input()) for _ in range(T))

# moduler operator
def mod(x):
  return x % 1000000009

# dp array
dp = [0 for i in range(1000001)]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
  dp[i] = mod(dp[i-1]) + mod(dp[i-2]) + mod(dp[i-3])

# print result
for test_case in test_cases:
  print(mod(dp[test_case]))
