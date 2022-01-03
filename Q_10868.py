# input
n, m = list(map(int, input().split()))
data = [int(input()) for _ in range(n)]
query = [list(map(int, input().split())) for _ in range(m)]

# segment tree
tree = [0] * (len(data) * 4)

# init tree
def initTree(start, end, index):
    if start == end:
        tree[index] = data[start]
        return tree[index] 
    mid = (start + end) // 2
    tree[index] = min(initTree(start, mid, index*2), initTree(mid+1, end, index*2+1))
    return tree[index]


# find min
def findMin(start, end, index, left, right):
    if end < left or right < start:
        return 1000000001
    if left <= start and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return min(findMin(start, mid, index*2, left, right), findMin(mid+1, end, index*2+1, left, right))

# find ans
initTree(0, len(data)-1, 1)
for q in query:
    print(findMin(0, len(data)-1, 1, q[0]-1, q[1]-1))