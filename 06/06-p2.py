input = open('input.txt', 'r')
Lines = input.readlines()
data = Lines[0]

WordLength = 14
res = -1
for i in range(0, len(data)):
  if len(set(data[i : i + WordLength])) == WordLength:
    res = i + WordLength
    break

print(res)
  
