# input
n = int(input())

# chess board arr : queen can lay on True element
chess = [[True for i in range(n)] for j in range(n)]
def initChess():
  for i in range(n):
    for j in range(n):
      chess[i][j] = True

# cnt w/ recursive ftn
def findQueen(x, y):
  result = 0
  # if queen is on last row, then count result
  if x == n - 1:
    return 1
  # update chess board only for under rows
  updated_tiles = []
  for r in range(x + 1, n):
    if chess[r][y]:
      chess[r][y] = False
      updated_tiles.append((r, y))
    if y + (r - x) < n and chess[r][y + (r - x)]:
      chess[r][y + (r - x)] = False
      updated_tiles.append((r, y + r - x))
    if y - (r - x) >= 0 and chess[r][y - (r - x)]:
      chess[r][y - (r - x)] = False
      updated_tiles.append((r, y - r + x))
  # check the places where queen can be for next row -> push in stack
  for c in range(n):
    if chess[x + 1][c]:
      result += findQueen(x + 1, c)
  # backtrack
  for tile in updated_tiles:
    chess[tile[0]][tile[1]] = True

  return result

# seach for n tiles at 0th row
count = 0
for i in range(n):
  initChess()
  count += findQueen(0, i)
print(count)