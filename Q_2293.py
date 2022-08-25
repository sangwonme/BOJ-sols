# input
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# sort, delete bigger than K
coins.sort()
coins = [x for x in coins if x <= K]

# dp
dp = [1] + [0 for _ in range(K)]
for coin in coins:
    for k in range(1, K+1):
        dp[k] += dp[k-coin] if k-coin >= 0 else 0

print(dp[-1])