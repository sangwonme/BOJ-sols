T = int(input())

for test_case in range(T):
  # input
  N = int(input())
  scores = []
  for i in range(N):
    scores.append(tuple(map(int, input().split())))
  scores.sort(key = lambda score: score[0])
  
  # find min, when min changes count ++
  min_score = 999999
  count = 0
  for score in scores:
    if score[1] < min_score:
      min_score = score[1]
      count += 1
  print(count)

