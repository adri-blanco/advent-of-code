
def generateTrees():
  input = open('input.txt', 'r')
  Lines = input.read().splitlines()
  Trees = []
  for line in Lines:
    row = []
    for tree in line:
      row.append(tree)
    Trees.append(row)

  return Trees

Trees = generateTrees()

def getScenicValueNorth(tree, x, y):
  if (x == 0 and tree > Trees[x][y]):
    return 0

  if(tree > Trees[x - 1][y]):
    return 1 + getScenicValueNorth(tree, x - 1, y)
  else:
    return 1

def getScenicValueSouth(tree, x, y, sizeX):
  if (x == sizeX - 1 and tree > Trees[x][y]):
    return 0

  if(tree > Trees[x + 1][y]):
    return 1 + getScenicValueSouth(tree, x + 1, y, sizeX)
  else:
    return 1

def getScenicValueWest(tree, x, y):
  if (y == 0 and tree > Trees[x][y]):
    return 0

  if(tree > Trees[x][y - 1]):
    return 1 + getScenicValueWest(tree, x, y - 1)
  else:
    return 1

def getScenicValueEast(tree, x, y, sizeY):
  if (y == sizeY - 1 and tree > Trees[x][y]):
    return 0

  if(tree > Trees[x][y + 1]):
    return 1 + getScenicValueEast(tree, x, y + 1, sizeY)
  else:
    return 1

def getScenicValue(tree, x, y, sizeX, sizeY):
  if(x == 0 or y == 0 or x == sizeX - 1 or y == sizeY - 1):
    return 0
  return getScenicValueNorth(tree, x, y) * getScenicValueSouth(tree, x, y, sizeX) * getScenicValueEast(tree, x, y, sizeY) * getScenicValueWest(tree, x, y)


highestScenicValue = 0
for x, row in enumerate(Trees):
  for y, tree in enumerate(row):
    v = getScenicValue(tree, x, y, len(Trees), len(row))
    if(v > highestScenicValue):
      highestScenicValue = v

print(highestScenicValue)