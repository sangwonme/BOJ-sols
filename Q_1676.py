# input
n = int(input())

# count prime factor : 2, 5
twos, fives = 0, 0
for i in range(1, n+1):
  tmp = i
  while tmp % 2 == 0:
    tmp /= 2
    twos += 1
  while tmp % 5 == 0:
    tmp /= 5
    fives += 1

# print min(twos, fives) i.e. tens(zeros)
print(min(twos, fives))