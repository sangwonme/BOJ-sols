from collections import deque

# input
n = int(input())

# each data is composed of [time, # of parents, children, done time]
buildings = [[0, 0, [], 0] for _ in range(n)]
queue = deque()
for i in range(n):
    data = list(map(int, input().split()))
    buildings[i][0] = data[0]
    parents_num = len(data) - 2
    buildings[i][1] = parents_num
    # connect parent & child
    for j in range(parents_num):
        buildings[data[j+1]-1][2].append(i)
    # enqueue if parents_num == 0 -> [node idx, current time = 0]
    if parents_num == 0:
        queue.append(i)

# compute time in topological order
while queue:
    # update done_time
    idx = queue.popleft()
    done_time = buildings[idx][3] + buildings[idx][0]
    buildings[idx][3] = done_time
    # check children nodes : if all condition is satisfied enqueue the node
    children = buildings[idx][2]
    for i in range(len(children)):
        buildings[children[i]][1] -= 1
        buildings[children[i]][3] = max(buildings[children[i]][3], done_time)
        if buildings[children[i]][1] == 0:
            queue.append(children[i])

# print answer
for i in range(n):
    print(buildings[i][3])