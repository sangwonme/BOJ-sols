from collections import deque

# input
n, m = list(map(int, input().split()))
data = [list(map(int, list(input()))) for _ in range(n)]

# bfs var : queue = (x, y, dist, broken)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([[0, 0, 1, False]])
visited = [[[False, False] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True

# bfs
res = -1
while queue:
    x, y, dist, broken = queue.popleft()
    # corner case
    if n == 1 and m == 1:
        res = 1
        continue    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # boundary check
        if (nx < 0 or n <= nx) or (ny < 0 or m <= ny):
            continue
        # visited check
        if visited[nx][ny][int(broken)]:
            continue
        # end condition
        if nx == n-1 and ny == m-1:
            res = dist + 1
            queue.clear()
            break
        # case 1 : path
        if data[nx][ny] == 0:
            queue.append([nx, ny, dist+1, broken])
            visited[nx][ny][int(broken)] = True
        # case 2 : wall
        elif data[nx][ny] == 1:
            if broken:
                continue
            else:
                queue.append([nx, ny, dist+1, True])
                visited[nx][ny][1] = True

print(res)