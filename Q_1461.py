import math

# input
n, m = list(map(int, input().split()))
data = list(map(int, input().split()))

# pos & neg
pos = [x for x in data if x > 0]
neg = [abs(x) for x in data if x < 0]
pos.sort()
neg.sort()

# get max
max_dist = max(max(data), abs(min(data)))
only_max = (max(data) != abs(min(data)))

# answer
res = 0
for i in range(math.ceil(len(pos)/m)):
    dist = pos[len(pos)-1-m*i]
    res += dist if dist == max_dist else dist*2
for i in range(math.ceil(len(neg)/m)):
    dist = neg[len(neg)-1-m*i]
    res += dist if dist == max_dist else dist*2
if not only_max and (len(pos) > 0 and len(neg) > 0):
    res += max_dist
print(res)