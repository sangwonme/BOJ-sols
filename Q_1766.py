import heapq

# input
n, m = list(map(int, input().split()))

# graph : (left to ready, next problems)
problems = [[0, []] for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    problems[b][0] += 1
    problems[a][1].append(b)

# init enqueue
queue = []
for i in range(1, n+1):
    if problems[i][0] == 0:
        heapq.heappush(queue, i)

# topological sort
ans = []
while queue:
    current_problem = heapq.heappop(queue)
    ans.append(current_problem)
    next_problems = problems[current_problem][1]
    for next in next_problems:
        problems[next][0] -= 1
        if problems[next][0] == 0:
            heapq.heappush(queue, next)

for num in ans:
    print(num, end=' ')