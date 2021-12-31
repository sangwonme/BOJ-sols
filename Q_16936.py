# input
n = int(input())
b = list(map(int, input().split()))

# get exp of base (for this problem 2, 3)
def getExp(num, base):
    exp = 0
    while(num % base == 0):
        num = num // base
        exp += 1
    return exp

# exp of base 3 is neg because it should sorted in descending order
exps = [(-getExp(b[i], 3), getExp(b[i], 2), b[i]) for i in range(n)]

# sort : descending of base 3, ascending of base 2
exps.sort() 
for i in range(n):
    print(exps[i][2], end=' ' if i != n-1 else '')