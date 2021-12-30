from collections import deque

# input
s, t = map(int, input().split())

# grpah
queue = deque([(s, '')])
visited = {}
visited[s] = True

# bfs
res = '-1'
while queue:
    num, history = queue.popleft()
    # break condition
    if num == t:
        res = history if history != '' else '0'
        break
    # case 1 : *
    if num*num <= 10**9 and not num*num in visited:
        visited[num*num] = True
        queue.append([num*num, history+'*'])
    # case 2 : +
    if num+num <= 10**9 and not num+num in visited:
        visited[num+num] = True
        queue.append([num+num, history+'+'])
    # case 3 : -
    if t == 0 and not num-num in visited:
        visited[num-num] = True
        queue.append([num-num, history+'-'])
    # case 4 : /
    if num != 0 and not num/num in visited:
        visited[num/num] = True
        queue.append([num/num, history+'/'])
        
print(res)