# input
gears = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())
query = [list(map(int, input().split())) for _ in range(k)]

# gear idx : each idx indicate element in 12o'clock direction
gear_idx = [0, 0, 0, 0]

# gear done : gear action is done (rotate or not), init for each step
gear_done = [False, False, False, False]
def init_gear_done():
    for i in range(4):
        gear_done[i] = False

# rotate
def rotate(gear, dir): 
    # done check
    if gear_done[gear]:
        return
    # rotate adjacent gear then rotate
    gear_done[gear] = True
    if 0 <= gear-1:
        left_idx = (gear_idx[gear] - 2) % 8
        right_idx = (gear_idx[gear-1] + 2) % 8
        if gears[gear][left_idx] != gears[gear-1][right_idx]:
            rotate(gear-1, -dir)
    if gear+1 < 4:
        left_idx = (gear_idx[gear+1] - 2) % 8
        right_idx = (gear_idx[gear] + 2) % 8
        if gears[gear+1][left_idx] != gears[gear][right_idx]:
            rotate(gear+1, -dir)         
    gear_idx[gear] = (gear_idx[gear] - dir) % 8
        
# simulate
for gear, dir in query:
    init_gear_done()
    rotate(gear-1, dir)
    
# print ans
res = 0
for i in range(4):
    res += gears[i][gear_idx[i]] * (2**i)
print(res)