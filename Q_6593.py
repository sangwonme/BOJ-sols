from collections import deque

# dir
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# input
l, r, c = list(map(int, input().split()))
while l != 0:
    data = []
    for _ in range(l):
        data.append([list(input()) for _ in range(r)])
        _ = input()
    
    # find start, end
    start, end = [-1, -1, -1], [-1, -1, -1]
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if data[i][j][k] == 'S': 
                    start = [i, j, k]
                    break
                
    # bfs
    res = -1
    queue = deque([[start[0], start[1], start[2], 0]])
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    visited[start[0]][start[1]][start[2]] = True
    while queue:
        x, y, z, dist = queue.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            # boundary check
            if (nx < 0 or l <= nx) or (ny < 0 or r <= ny) or (nz < 0 or c <= nz):
                continue
            # visited check
            if visited[nx][ny][nz]:
                continue
            # path check
            if data[nx][ny][nz] == '#':
                continue
            # enqueue
            if data[nx][ny][nz] == 'E':
                res = dist + 1
                break
            else:
                visited[nx][ny][nz] = True
                queue.append([nx, ny, nz, dist+1])
    
    # print ans and new input
    if res == -1:
        print('Trapped!')
    else:
        print('Escaped in ' + str(res) + ' minute(s).')
    l, r, c = list(map(int, input().split()))