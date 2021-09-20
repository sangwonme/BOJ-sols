from sys import stdin

# input
s = stdin.readline().rstrip('\n')
t = stdin.readline().rstrip('\n')

# make s from t
res = 0
for i in range(len(t)):
  if t[-1] == 'A':
    t = t[:-1]
  elif t[-1] == 'B':
    t = t[:-1]
    t = t[::-1]
  if s == t:
    res = 1
    break

print(res)