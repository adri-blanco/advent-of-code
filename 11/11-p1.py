input = open('input.txt', 'r')
Lines = input.read().splitlines()

def getItems(line):
  sp = line.split('Starting items: ')
  return list(map(int, sp[1].split(', ')))
  
def getOperand(operand):
  if(operand == 'old'):
    return operand
  return int(operand)

def getOperation(line):
  sp = line.split(' = old ')
  [op, operand] = sp[1].split(' ')

  if(operand == 'old'):
    match(op):
      case '+': return lambda old: old + old
      case '*': return lambda old: old * old

  match(op):
    case '+': return lambda old: old + int(operand)
    case '*': return lambda old: old * int(operand)

def getTest(line):
  return int(line.split()[-1])

def parseMonkeys():
  index = 0
  Monkeys = []
  while(index < len(Lines)):
    Monkey = {}
    Monkey["inspections"] = 0
    Monkey["items"] = getItems(Lines[index + 1])
    Monkey["operation"] = getOperation(Lines[index + 2])
    Monkey["test"] = getTest(Lines[index + 3])
    Monkey["true"] = getTest(Lines[index + 4])
    Monkey["false"] = getTest(Lines[index + 5])

    index += 7
    Monkeys.append(Monkey)

  return Monkeys

Monkeys = parseMonkeys()

def throwItem(nextMonkey, level):
  global Monkeys
  Monkeys[nextMonkey]["items"].append(level)

for round in range(0, 20): 
  for monkey in Monkeys:
    for worryItemLevel in monkey["items"]:
      newLevel = monkey["operation"](worryItemLevel)
      newLevel //= 3
      monkey["inspections"] += 1

      if(newLevel % monkey["test"] == 0):
        throwItem(monkey["true"], newLevel)
      else:
        throwItem(monkey["false"], newLevel)
    monkey["items"] = []

Inspections = []
for m in Monkeys:
  Inspections.append(m["inspections"])

Inspections.sort(reverse=True)
MonkeyBusiness = Inspections[0] * Inspections[1]

print(MonkeyBusiness)