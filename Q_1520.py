# input
M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

# direction
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# dp
cache = [[-1 for _ in range(N)] for _ in range(M)]
cache[0][0] = 1
def search_path(y, x):
    # case 1 : already solved
    if cache[y][x] != -1:
        return cache[y][x]
    # case 2 : sum for 4 directions
    cache[y][x] = 0
    for i in range(4):
        nx, ny = dx[i], dy[i]
        if (0 <= x+nx < N and 0 <= y+ny < M) and arr[y+ny][x+nx] > arr[y][x]:
            cache[y][x] += search_path(y+ny, x+nx)
    return cache[y][x]

print(search_path(M-1, N-1))