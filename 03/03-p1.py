input = open('input.txt', 'r')
Rucksacks = input.readlines()

def getCompartments(rucksack):
  size = len(rucksack)
  return [rucksack[0 : size//2], rucksack[size//2:size]]

def getDuplicated(c1, c2):
  for item in c1:
    index = c2.find(item)
    if(index != -1):
      return c2[index]

Priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def getPriority(item):
  return Priority.find(item) + 1

priority = 0
for rucksack in Rucksacks:
  [c1, c2] = getCompartments(rucksack.replace('\n',  ''))
  item = getDuplicated(c1, c2)
  priority += getPriority(item)

print(priority)