from collections import deque

# test case
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    data = list(map(int, input().split()))
    
    # graph : left, children[], time
    graph = [[0, [], 0] for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int, input().split()))
        graph[x-1][1].append(y)
        graph[y-1][0] += 1
    end = int(input())
    
    # enque
    queue = deque()
    for i in range(n):
        if graph[i][0] == 0:
            graph[i][2] = data[i]
            queue.append(i)
    
    # topological sort
    res = 0
    while queue:
        node = queue.popleft()
        _, children, time = graph[node]
        if node == end-1:
            res = time
            break
        for idx in children:
            child = idx-1
            graph[child][0] -= 1
            graph[child][2] = max(graph[child][2], time)
            if graph[child][0] == 0:
                graph[child][2] += data[child]
                queue.append(child)
                
    print(res)