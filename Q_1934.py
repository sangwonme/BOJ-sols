# test case input
t = int(input())

# gcd fun
def gcd(a, b):
  x, y = min(a, b), max(a, b)
  while y % x != 0:
    tmp = y % x
    y, x = x, tmp
  return x

for test_case in range(t):
  a, b = map(int, input().split())
  print(int(a * b / gcd(a, b)))