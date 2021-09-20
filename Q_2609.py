# input
data = list(map(int, input().split()))

# gcd
x, y = sorted(data)
while y % x != 0:
  tmp = y % x
  y, x = x, tmp

# print res
print(x)
print(int(data[0] * data[1] / x))