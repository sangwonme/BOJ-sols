document = input()
inputData = input()

# count at document by iterator
count = 0
idx = 0
while idx <= (len(document) - len(inputData)):
  if inputData == document[idx : idx + len(inputData)]:
    count += 1
    idx += (len(inputData))
  else:
    idx += 1

# print answer
print(count)