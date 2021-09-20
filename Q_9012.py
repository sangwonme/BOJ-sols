# input
t = int(input())

# test_case
for test_case in range(t):
  result = 'NO'
  string = input()
  # check the length is even
  if len(string) % 2 == 0:
    tmp = 0
    # check open and close is well done
    for i in range(len(string)):
      tmp += 1 if string[i] == '(' else -1
      if tmp < 0:
        break 
    if tmp == 0:
      result = 'YES'
  print(result)