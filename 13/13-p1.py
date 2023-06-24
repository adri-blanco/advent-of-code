import os
route = os.path.dirname(__file__)
input = open(os.path.join(route, 'input.txt'), 'r')
Lines = input.read().splitlines()

Comparitions = []
index = 0
while(index < len(Lines)):
  left = eval(Lines[index])
  right = eval(Lines[index + 1])

  Comparitions.append([ left, right])
  index += 3

def compare(l, r):
  if(len(l) == 0):
    return True
  if(len(r) == 0):
    return False

  left = l[0]
  right = r[0]
  print(left, 'vs' , right)

  if isinstance(left, list) or isinstance(right, list):
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    return compare(left, right)

  if(left == right):
    print(l)
    l.pop(0)
    r.pop(0)
    return compare(l, r)

  if(left < right):
    return True
  else:
    return False

sum = 0
for i, [left, right] in enumerate(Comparitions):
  print('========', i + 1, '========')
  res = compare(left, right)
  print(res)
  if res:
    sum += i + 1

print(sum)
