# input
N = int(input())

# odd case
if N % 2 == 1:
    print(0)
# normal case
else:
    n = N // 2
    cache = [0 for _ in range(30 // 2 + 1)]
    cache[0] = 1
    for i in range(n+1):
        for j in range(1, i+1):
            cache[i] += (3 if j == 1 else 2) * cache[i-j]
    print(cache[n])