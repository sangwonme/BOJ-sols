# input
string = input()

# linear search
count = 0
i = 0
while i < len(string):
  if i < len(string) - 2 and string[i:i+3] == 'dz=':
    count += 1
    i += 2
  elif string[i] in 'cdsz' and i < len(string) - 1 and string[i+1] in '-=':
    count += 1
    i += 1
  elif string[i] in 'ln' and i < len(string) - 1 and string[i+1] == 'j':
    count += 1
    i += 1
  else:
    count += 1
  i += 1

# answer
print(count)
