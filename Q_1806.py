# input
n, s = list(map(int, input().split()))
data = list(map(int, input().split()))

# two-pointers
start = 0
end = 0
tmp = data[0]
ans = 999999

# simulate
while start < len(data) and end < len(data):
    # case 1 : sum(tmp) larger than s
    if tmp >= s:
        ans = min(ans, end-start+1)
        tmp -= data[start]
        start += 1
    # case 2 : sum(tmp) smaller than s
    else: 
        end += 1
        tmp += data[end] if end < len(data) else 0

# print ans
print(ans if ans != 999999 else 0)