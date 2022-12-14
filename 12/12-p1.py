import os
import sys
d = os.path.dirname(__file__)
input = open(os.path.join(d, 'input.txt'), 'r')
Lines = input.read().splitlines()

sys.setrecursionlimit(99999)

Terrain = []
Start = [0, 0]
Destiny = [0,0]
AvailableSteps = {}
OpenPositions = {}
VisitedPositions = {}

def generateTerrain():
  global Terrain
  global Start
  global Destiny
  for x, line in enumerate(Lines):
    latitude = []
    for y, high in enumerate(line):
      if (high == 'S'):
        Start = [x, y]
        high = 'a'
      if (high == 'E'):
        Destiny = [x, y]
        high = 'z'
      latitude.append(high)
    Terrain.append(latitude)

def MoveNorth(position):
  return [position[0] - 1, position[1]]
def MoveSouth(position):
  return [position[0] + 1, position[1]]
def MoveWest(position):
  return [position[0], position[1] - 1]
def MoveEast(position):
  return [position[0], position[1] + 1]

def getHeight(position):
  return Terrain[position[0]][position[1]]

def isWalkable(position, prevPosition):
  if(position[0] < 0 or position[0] >= len(Terrain) or position[1] < 0 or position[1] >= len(Terrain[0])):
    return False

  currentVal = ord(getHeight(position))
  nextVal = ord(getHeight(prevPosition))

  return abs(nextVal - currentVal) <= 1

def getDistance(a, b):
  [xA, yA] = a
  [xB, yB] = b

  return (abs(xA - xB) + abs(yA - yB))

def updatePosition(position, prevPosition):
  global OpenPositions
  positionInfo = OpenPositions[str(position)]

  if positionInfo['dS'] > prevPosition['dS'] + 1:
    positionInfo['dS'] = prevPosition['dS'] + 1
    positionInfo['parent'] = prevPosition['position']
    OpenPositions[str(position)] = positionInfo

def calculatePosition(position, prevPosition):
  global OpenPositions

  if str(position) in OpenPositions:
    return updatePosition(position, prevPosition)
  if str(position) in VisitedPositions or not isWalkable(position, prevPosition['position']):
    return

  value = {}
  value['position'] = position
  value['from'] = prevPosition['position']
  value['dS'] = prevPosition['dS'] + 1
  value['dD'] = getDistance(position, Destiny)
  value['value'] = value['dS'] + value['dD']
  
  OpenPositions[str(position)] = value

def calculateSurroundings(positionInfo):
  position = positionInfo['position']
  calculatePosition(MoveNorth(position), positionInfo)
  calculatePosition(MoveSouth(position), positionInfo)
  calculatePosition(MoveWest(position), positionInfo)
  calculatePosition(MoveEast(position), positionInfo)

def getNextStep():
  global OpenPositions
  next = { 'value': 99999999 }
  for k in OpenPositions:
    if(OpenPositions[k]['value'] < next['value'] or (OpenPositions[k]['value'] < next['value'] and OpenPositions[k]['dD'] < next['value'])):
      next = OpenPositions[k]
  
  return next

def PrintTerrain(current):
  print()
  print(str(current))
  for x, l in enumerate(Terrain):
    line = ''
    for y, high in enumerate(Terrain[x]):
      if(current[0] == x and current[1] == y):
        line += '.'
      elif(str([x, y]) in OpenPositions):
        line += 'O'
      elif str([x, y]) in VisitedPositions:
        line += 'X'
      else:
        line += Terrain[x][y]
    print(line)
  print()

def Walk(position):
  global OpenPositions
  # PrintTerrain(position)
  VisitedPositions[str(position)] = OpenPositions[str(position)]
  del OpenPositions[str(position)]

  if(position[0] == Destiny[0] and position[1] == Destiny[1]):
    return 0

  calculateSurroundings(VisitedPositions[str(position)])
  next = getNextStep()

  return Walk(next['position']) + 1

def FindPath(position):
  global VisitedPositions
  current = VisitedPositions[str(position)]
  position = current['position']

  if(position[0] == Start[0] and position[1] == Start[1]):
    return 0
  
  return FindPath(current['from']) + 1


generateTerrain()
OpenPositions[str(Start)] = {
  'dS': 0,
  'position': Start
}
print(Walk(Start))
print(FindPath(Destiny))
