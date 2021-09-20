n = int(input())
t = int(input())

network_connection = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

# connection input data
for connection in range(t):
  i, j = map(int, input().split())
  network_connection[i].append(j)
  network_connection[j].append(i)

# DFS Method
def countConnectedComputer():
  stack = []
  stack.append(1);
  count = 0
  visited[1] = True
  while stack:
    computer = stack.pop()
    for connected_computer in network_connection[computer]:
      if not visited[connected_computer]:
        stack.append(connected_computer)
        visited[connected_computer] = True
        count += 1
  return count

print(countConnectedComputer())
