input = open('input.txt', 'r')
Lines = input.readlines()

def getColumnsLength():
  return len(Lines[0]) // 4

def initializeStacks():
  res = []
  for i in range(0, getColumnsLength()):
    res.append([])
  return res

def cleanItem(item):
  Dirt = ' []\n'
  clean = item
  for dirt in Dirt:
    clean = clean.replace(dirt, '')
  return clean

def buildStack():
  lineIndex = 0
  Stacks = initializeStacks()
  while(True):
    line = Lines[lineIndex]
    if(line.find('[') == -1):
      break
    lineIndex += 1

    i = 0
    while(i < len(line)):
      item = line[i : i + 4]
      if(item.find('[') != -1):
        Stacks[i//4].append(cleanItem(item))
      i += 4
  return Stacks

def buildOrders():
  Orders = []
  for line in Lines:
    if(line.find('move ') == -1):
      continue
    l = line.replace('\n', '').split(' ')
    Orders.append([int(l[1]), int(l[3]) -1 , int(l[5]) - 1])
  return Orders

def move(stack, order):
  [ammount, origin, destiny] = order
  for i in range(0, ammount):
    stack[destiny].insert(0, stack[origin].pop(0))
  return stack

Stack = buildStack()
Orders = buildOrders()
for order in Orders:
  Stack = move(Stack, order)

result = ''
for column in Stack:
  result += column[0]

print(result)