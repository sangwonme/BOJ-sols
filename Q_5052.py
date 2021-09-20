t = int(input())

for test_case in range(t):
  # input
  n = int(input())
  data = list(input() for _ in range(n))
  
  # sort
  data.sort()
  
  # case when data returns YES/NO
  result = 'YES'
  for i in range(n-1):
    cur, nxt = data[i], data[i+1]
    if len(cur) <= len(nxt) and nxt.find(cur) == 0:
      result = 'NO'
      continue    
  
  # print answer
  print(result)