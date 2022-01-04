from collections import deque

# test case
t = int(input())
for _ in range(t):
    # input
    operations = list(input())
    n = int(input())
    arr = input()[1:-1].split(',')
    queue = deque(arr) if arr[0]!='' else deque()
    
    # do operations
    is_reversed = False
    for i in range(len(operations)):
        if operations[i] == 'R':
            is_reversed = not is_reversed
        elif operations[i] == 'D':
            if not queue:
                print('error')
                break
            elif not is_reversed:
                queue.popleft()
            elif is_reversed:
                queue.pop()
        # print result
        if i == len(operations)-1:
            print('[', end='')
            for j in range(len(queue)):
                idx = j
                if is_reversed:
                    idx = len(queue) - 1 -j
                print(queue[idx], end=',' if j!=len(queue)-1 else '')
            print(']')