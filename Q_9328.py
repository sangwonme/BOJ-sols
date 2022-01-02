from collections import deque

# test case
t = int(input())
for _ in range(t):
    cnt = 0
    
    # addKey ftn : add key to key list and return encoded key list
    def addKey(newkey, keys):
        decoded_keys = list(keys)
        decoded_keys[ord(newkey)-ord('a')] = '1'
        return ''.join(decoded_keys)
        
    # input
    h, w = map(int, input().split())
    data = [list(input()) for _ in range(h)]
    
    # init keys
    init_keys = ''.join(['0']*26)
    starting_keys = input()
    if starting_keys != '0':
        for i in range(len(starting_keys)):
            init_keys = addKey(starting_keys[i], init_keys)
        
    # graph vars
    queue = deque([])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[{} for _ in range(w)] for _ in range(h)]
    
    # find starting points by dfs
    starting_points = []
    visited_for_dfs = [[False for _ in range(w)] for _ in range(h)]
    stack = []
    
    # dfs
    def dfsFromPos(posX, posY):
        if data[posY][posX] != '*':
            if not visited_for_dfs[posY][posX]:
                if not (65 <= ord(data[posY][posX]) and ord(data[posY][posX]) <= 90):
                    stack.append([posX, posY])
                starting_points.append([posX, posY])
                queue.append([posX, posY, init_keys])
                visited_for_dfs[posY][posX] = True
        while stack:
            x, y = stack.pop()
            for j in range(4):
                nx, ny = x+dx[j], y+dy[j]
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                elif data[ny][nx] != '*' and not (65 <= ord(data[ny][nx]) and ord(data[ny][nx]) <= 90):
                    if not visited_for_dfs[ny][nx]:
                        stack.append([nx, ny])
                        visited_for_dfs[ny][nx] = True
        
    # update starting_points
    for i in range(w):
        dfsFromPos(i, 0)
        dfsFromPos(i, h-1)
    for i in range(h):
        dfsFromPos(0, i)
        dfsFromPos(w-1, i)
    
    # print(init_keys)
    # print(starting_points)
    
    # bfs
    while queue:
        x, y, current_keys = queue.popleft()
        # boundary check
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        # visited check
        elif current_keys in visited[y][x]:
            continue
        # path check
        else:
            tile = data[y][x]
            # wall
            if tile == '*':
                continue
            # doc
            elif tile == '$':
                # print('money at : '+str(x) + ', ' + str(y))
                data[y][x] = '.'
                cnt += 1
            # key
            elif 97 <= ord(tile) and ord(tile) <= 122:
                # print('key ' + tile + ' from : ' + str(x) + ', ' + str(y))
                current_keys = addKey(tile, current_keys)
                data[y][x] = '.'
                for pos in starting_points:
                    queue.append([pos[0], pos[1], current_keys])
            # openable door
            elif 65 <= ord(tile) and ord(tile) <= 90:
                # print('door ' + tile + ' at : ' + str(x) + ', ' + str(y))
                if bool(int(current_keys[ord(tile)-ord('A')])):
                    # print('door is opened')
                    data[y][x] = '.'
                    queue.append([x, y, current_keys])
                else:
                    continue
            # path
            elif tile == '.':
                pass
            # push next pos
            visited[y][x][current_keys] = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                queue.append([nx, ny, current_keys])
                
    print(cnt)