from collections import deque

while True:
    # input
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
    
    # simulation
    else:
        data = [list(input()) for _ in range(h)]
        
        # init pos
        start = [-1, -1]
        dusts = []
        for i in range(h):
            for j in range(w):
                if data[i][j] == 'o' : start = [j, i]
                elif data[i][j] == '*' : dusts.append([j, i])
        
        # graph var : queue data = [x, y, dist, dust state : 0-dirty/1-clean]
        queue = deque([[start[0], start[1], 0, ''.join(['0']*len(dusts))]])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[{} for _ in range(w)] for _ in range(h)]
        
        # bfs
        res = -1
        while queue:
            x, y, dist, dust_state = queue.popleft()       
            # boundary check
            if x < 0 or x >= w or y < 0 or y >= h:
                continue
            # visited check
            if dust_state in visited[y][x]:
                continue
            # path check
            visited[y][x][dust_state] = True
            tile = data[y][x]
            if tile == '.':
                pass
            elif tile == 'x':
                continue
            elif tile == '*':
                dust_idx = dusts.index([x, y])
                tmp = list(dust_state)
                tmp[dust_idx] = '1'
                dust_state = ''.join(tmp)
                visited[y][x][dust_state] = True
                # end condition
                if dust_state == ''.join(['1']*len(dust_state)):
                    res = dist
                    break
            # go to next tile
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                queue.append([nx, ny, dist+1, dust_state])
            
        print(res)