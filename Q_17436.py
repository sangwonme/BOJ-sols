# input
n, m = map(int, input().split())
prime = list(map(int, input().split()))

# inclusion-exculsion principle
res = 0
for i in range(1, 2**n):
    # select numbers
    indices = list(bin(i)[2:])
    indices = ['0'] * (n-len(indices)) + indices
    q = 1
    for j in range(n):
        q *= prime[j] if bool(int(indices[j])) else 1
    # inclusion
    if sum(map(int, indices)) % 2 == 1:
        res += m // q
    # exclusion
    else :
        res -= m // q

print(res)
