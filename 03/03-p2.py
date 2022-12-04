input = open('input.txt', 'r')
Rucksacks = input.readlines()

def getDuplicated(c1, c2, c3):
  for item in c1:
    indexC2 = c2.find(item)
    if(indexC2 != -1):
      indexC3 = c3.find(item)
      if(indexC3 != -1):
        return item

Priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def getPriority(item):
  return Priority.find(item) + 1

def cleanRucksack(rucksack):
  return rucksack.replace('\n', '')

priority = 0
# for rucksack in Rucksacks:
index = 0
while(index < len(Rucksacks)):
  r1 = cleanRucksack(Rucksacks[index])
  r2 = cleanRucksack(Rucksacks[index + 1])
  r3 = cleanRucksack(Rucksacks[index + 2])
  item = getDuplicated(r1, r2, r3)
  priority += getPriority(item)
  index += 3

print(priority)