import math
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

# Solution took from reddit. Tried to decompose the numbers in prime number compositions without much luck
# The idea base in that the divisible numbers repeat it's pattern each number of times, his less common multiple
# Good explanation here: https://www.reddit.com/r/adventofcode/comments/zizi43/comment/iztt8mx/?utm_source=reddit&utm_medium=web2x&context=3
t = []
for m in Monkeys:
  t.append(m["test"])
MaxNumber = math.prod(t);


for round in range(0, 10000):
  for monkey in Monkeys:
    for worryItemLevel in monkey["items"]:
      newLevel = monkey["operation"](worryItemLevel)
      newLevel = newLevel % MaxNumber
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