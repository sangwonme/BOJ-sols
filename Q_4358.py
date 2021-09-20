from sys import stdin

# input & count
count = dict()
total = 0
tree = stdin.readline().rstrip('\n')
while tree != '':
  count[tree] = count.get(tree, 0) + 1
  total += 1
  tree = stdin.readline().rstrip('\n')

# sort
count_sorted = sorted(count.items())

# print fraction
for t in count_sorted:
  print(t[0], '%.4f' % (100 * int(t[1]) / total))