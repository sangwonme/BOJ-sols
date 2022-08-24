# input
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# make dp arr
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# fill the dp arr
for i in range(1, N+1):
    cur_w, cur_v = items[i-1]
    for j in range(1, K+1):
        if cur_w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur_w] + cur_v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])