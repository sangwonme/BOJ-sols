# input
n = int(input())

# leave prime-numbers only
prime_numbers = [True for _ in range(n)]
for i in range(len(prime_numbers)):
    if i == 0:
        prime_numbers[i] = False
    elif prime_numbers[i]:
        j = 2
        while j * (i+1) <= n:
            prime_numbers[j*(i+1)-1] = False
            j += 1

# get sum - two pointers
start, end, tmp = 1, 1, 2
cnt = 0
while start < n and end < n:
    # case 1 : sum is smaller than n
    if tmp < n:
        while end < n:
            end += 1
            if end == n:
                break
            if prime_numbers[end]:
                tmp += (end + 1)
                break
    # case 2 : sum is bigger than n
    elif tmp > n:
        tmp -= (start + 1)
        while start < n:
            start += 1
            if start == n or prime_numbers[start]:
                break
    # case 3 : sum is equal to n
    else:
        cnt += 1
        while end < n:
            end += 1
            if end == n:
                break
            if prime_numbers[end]:
                tmp += (end + 1)
                break

print(cnt)