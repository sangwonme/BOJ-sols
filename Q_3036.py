# input
n = int(input())
data = list(map(int, input().split()))

# gcd
def gcd(a, b):
  small, big = [a, b] if a < b else [b, a]
  while big % small != 0:
    tmp = big % small
    big, small = small, tmp
  return small

# print
for i in range(1, n):
  divider = gcd(data[0], data[i])
  print(str(int(data[0]/divider)) + '/' + str(int(data[i]/divider)))
