# input
n, l, r = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]

# simulation by dfs
iteration = 0
while True:
    # init graph vars
    visited = [[False for _ in range(n)] for _ in range(n)]
    stack = []
    areas = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    isMove = False
     
    # dfs for each area
    for i in range(n):
        for j in range(n):
            area = []
            stack.append([i,j])
            area.append([i,j])
            total = data[i][j]
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    dif = abs(data[x][y] - data[nx][ny])
                    if l <= dif and dif <= r:
                        stack.append([nx, ny])
                        area.append([nx, ny])
                        isMove = True
                        visited[nx][ny] = True
                        total += data[nx][ny]
            areas.append([area, total])
    
    # end condition
    if not isMove:
        break
    # update population
    else:
        iteration += 1
        while areas:
            area, total = areas.pop()
            for i in range(len(area)):
                data[area[i][0]][area[i][1]] = total // len(area)
    
print(iteration)