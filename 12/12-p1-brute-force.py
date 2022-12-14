import copy
import os
d = os.path.dirname(__file__)
input = open(os.path.join(d, 'input.txt'), 'r')
Lines = input.read().splitlines()

Terrain = []
Start = [0, 0]
Destiny = [0,0]
Visited = []

Paths = 0

North = 'N'
West = 'W'
South = 'S'
East = 'E'

for x, line in enumerate(Lines):
  latitude = []
  lV = []
  for y, high in enumerate(line):
    if (high == 'S'):
      Start = [x, y]
      high = 'a'
    if (high == 'E'):
      Destiny = [x, y]
      high = 'z'
    latitude.append(high)
    lV.append(False)
  Terrain.append(latitude)
  Visited.append(lV)

def allFalse(arr):
  res = True
  for p in arr:
    if p != False:
      res = False
  return res

def getHeight(position):
  return Terrain[position[0]][position[1]]

def MoveNorth(position):
  return [position[0] - 1, position[1]]
def MoveSouth(position):
  return [position[0] + 1, position[1]]
def MoveWest(position):
  return [position[0], position[1] - 1]
def MoveEast(position):
  return [position[0], position[1] + 1]

def Walkable(current, next, v):
  # print(v)
  # print(next)
  if(v[next[0]][next[1]]):
    return False

  currentVal = ord(getHeight(current))
  nextVal = ord(getHeight(next))

  return abs(nextVal - currentVal) <= 1

Steps = 0
def Walk(position, direction, v):
  global Paths
  global Steps
  # print(Paths)
  Steps += 1
  v[position[0]][position[1]] = True
  if(position[0] == Destiny[0] and position[1] == Destiny[1]):
    # print('Encontrado')
    return 1
  
  results = []
  if (direction != North and position[0] != 0 and Walkable(position, MoveNorth(position), v)):
    # print('al North' + str(position[0])+ ' '+ str(position[1]))
    Paths += 1
    results.append(Walk(MoveNorth(position), South, copy.deepcopy(v)))
  if (direction != West and position[1] != 0 and Walkable(position, MoveWest(position), v)):
    # print('al West' + str(position[0])+ ' '+ str(position[1]))
    Paths += 1
    results.append(Walk(MoveWest(position), East, copy.deepcopy(v)))
  if (direction != South and position[0] != len(Terrain) - 1 and Walkable(position, MoveSouth(position), v)):
    # print('al South' + str(position[0])+ ' '+ str(position[1]))
    Paths += 1
    results.append(Walk(MoveSouth(position), North, copy.deepcopy(v)))

  # print(position[1], '>>>>>>>>>>>>>')
  if (direction != East and position[1] != len(Terrain[0]) - 1 and Walkable(position, MoveEast(position), v)):
    # print('al East' + str(position[0])+ ' '+ str(position[1]))
    Paths += 1
    results.append(Walk(MoveEast(position), West, copy.deepcopy(v)))
  
  # print(results)
  minPath = 9999999999
  for res in results:
    Paths -= 1
    if(res != False and minPath > res):
      minPath = res

  if len(results) == 0 or (allFalse(results) and results[0] == False):
    return False
  
  return minPath + 1

print(Walk(Start, 'Start', copy.deepcopy(Visited)) - 1)
print(Steps)