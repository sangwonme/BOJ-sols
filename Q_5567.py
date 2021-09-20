# input
n = int(input())
data = [[] for _ in range(n + 1)]
m = int(input())
for i in range(m):
  a, b = map(int, input().split())
  data[a].append(b)
  data[b].append(a)

# find friend's list
invite_list = []
for friend in data[1]:
  invite_list.append(friend)
  for second_friend in data[friend]:
    if second_friend != 1:
      invite_list.append(second_friend)

# remove duplicates
invite_list = list(dict.fromkeys(invite_list))
print(len(invite_list))