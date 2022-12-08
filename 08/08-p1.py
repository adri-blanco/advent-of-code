
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

def isVisibleNorth(tree, x, y):
  if (x == 0 and tree > Trees[x][y]):
    return True

  if(tree > Trees[x - 1][y]):
    return isVisibleNorth(tree, x - 1, y)
  else:
    return False

def isVisibleSouth(tree, x, y, sizeX):
  if (x == sizeX - 1 and tree > Trees[x][y]):
    return True

  if(tree > Trees[x + 1][y]):
    return isVisibleSouth(tree, x + 1, y, sizeX)
  else:
    return False

def isVisibleWest(tree, x, y):
  if (y == 0 and tree > Trees[x][y]):
    return True

  if(tree > Trees[x][y - 1]):
    return isVisibleWest(tree, x, y - 1)
  else:
    return False

def isVisibleEast(tree, x, y, sizeY):
  if (y == sizeY - 1 and tree > Trees[x][y]):
    return True

  if(tree > Trees[x][y + 1]):
    return isVisibleEast(tree, x, y + 1, sizeY)
  else:
    return False

def isVisible(tree, x, y, sizeX, sizeY):
  if(x == 0 or y == 0 or x == sizeX - 1 or y == sizeY - 1):
    return True
  return isVisibleNorth(tree, x, y) or isVisibleSouth(tree, x, y, sizeX) or isVisibleEast(tree, x, y, sizeY) or isVisibleWest(tree, x, y)


visibleTrees = 0
for x, row in enumerate(Trees):
  for y, tree in enumerate(row):
    if(isVisible(tree, x, y, len(Trees), len(row))):
      visibleTrees += 1

print(visibleTrees)