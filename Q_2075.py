import heapq

# input
n = int(input())
heap = []
for _ in range(n):
    data = list(map(int, input().split()))
    for i in range(n):
        heapq.heappush(heap, data[i])
        if len(heap) > n:
            heapq.heappop(heap)

# answer
res = heapq.heappop(heap)
    
print(res)