import math

# input
n = int(input())
t = []
for i in range(n):
    start, end = map(int, input().split())
    t.append([start, end])
    
# test case
for i in range(n):
    distance = t[i][1] - t[i][0]
    rt = int(math.sqrt(distance))
    res = 0
    # case 1 : rt^2 == distance -> idx = rt * 2 - 1
    if rt**2 == distance:
        res = rt*2 - 1
    # case 2 : rt^2 < dist <= rt^2 + rt -> idx = rt * 2
    elif (rt**2 < distance and distance <= rt**2 + rt):
        res = rt*2
    # case 3 : rt^2 + rt < dist <= (rt+1)^2 -> idx = rt * 2 + 1
    elif (rt**2 + rt < distance and (rt+1)**2):
        res = rt*2 + 1
    print(res)
    