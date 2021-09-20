# input
n, m = map(int, input().split())

# get min value
min_package, min_single = 9999, 9999
for i in range(m):
  x, y = map(int, input().split())
  min_package = x if x < min_package else min_package
  min_single = y if y < min_single else min_single

# get Q, R
q, r = n // 6, n % 6

# 3 cases : all single, max package, overflow package
result = min(min_single * n, min_package * q + min_single * r, min_package * (q + 1))
print(result)