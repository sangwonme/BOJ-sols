import heapq

# input
n, l = list(map(int, input().split()))
data = list(map(int, input().split()))

# heap : data and origin idx
heap = []
ans = []
for i in range(len(data)):
    heapq.heappush(heap, (data[i], i))
    if len(heap) > l:
        while heap[0][1] <= i - l:
            heapq.heappop(heap)
    ans.append(heap[0][0])

# print ans
for a in ans:
    print(a, end=' ')