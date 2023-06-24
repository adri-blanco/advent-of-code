import os
import time
route = os.path.dirname(__file__)
input = open(os.path.join(route, 'input.txt'), 'r')
Lines = input.read().splitlines()
Commands = Lines[0]

WIDE = 7
EMPTY_LINE = '.......'
BOARD = [EMPTY_LINE,  EMPTY_LINE, EMPTY_LINE]

H_BAR = ['@@@@']
PLUS = ['.@.', '@@@', '.@.']
L = ['@@@', '..@', '..@']
V_BAR = ['@', '@', '@', '@']
BLOCK = ['@@', '@@']

ORDER = [H_BAR, PLUS, L, V_BAR, BLOCK]

def printBoard():
  global BOARD
  back = "\033[" + str(len(BOARD) + 2) + "A"
  print(back)

  print('Rock number: ', BLOCKS_THROWN)
  for line in reversed(BOARD):
    print(line)

def removeSpace():
  blank = 0
  stillEmpty = True
  index = 0
  while(stillEmpty):
    if(BOARD[len(BOARD) - 1 - index] == EMPTY_LINE):
      index += 1
      blank += 1
    else:
      stillEmpty = False
    
  for x in range(3, blank):
    del BOARD[-1]

def fillBlank():
  neededLines = 0
  for i in range(0, 2):
    if(BOARD[len(BOARD) - 1 - i] != EMPTY_LINE):
      neededLines += 1

  for x in range(0, neededLines):
    BOARD.append(EMPTY_LINE)

NEXT_BLOCK = 0
BLOCK_INDEX = 0
throwBlock = True

def addBlock():
  global throwBlock
  global BLOCK_INDEX

  for i in range(0, len(ORDER[NEXT_BLOCK])):
    res = '..'
    res += ORDER[NEXT_BLOCK][i]
    while len(res) < 7:
      res += '.'
    BOARD.append(res)

  throwBlock = False


def canFall(index):
  if(index == 0):
    return False
  current = BOARD[index]
  below = BOARD[index - 1]
  for x, ele in enumerate(current):
    if(ele == '@' and below[x] != '.'):
      return False

  return True

def replaceIndex(str, new, index):
  return str[:index] + new + str[index+1:]

def isAllPlaced():
  global BOARD
  for i, line in enumerate(BOARD):
    if line.find('@') != -1:
      return False
  return True

def fall():
  global throwBlock
  global NEXT_BLOCK
  for i, line in enumerate(BOARD):
    if(line.find('@') != -1):
      if canFall(i):
        for x, ele in enumerate(BOARD[i]):
          if ele == '@':
            BOARD[i-1] = replaceIndex(BOARD[i - 1], '@', x)
            BOARD[i] = replaceIndex(BOARD[i], '.', x)
      else:
        BOARD[i] = line.replace('@', '#')
  
  if(isAllPlaced()):
    fillBlank()
    removeSpace()
    throwBlock = True
    NEXT_BLOCK = (NEXT_BLOCK + 1) % len(ORDER)

def reverse(str):
  return str[::-1]

def canGoLeft():
  for line in BOARD:
    if(line[0] == '@'):
      return False

    for i, ele in enumerate(line):
      if(i != 0 and line[i] == '@' and line[i - 1] == '#'):
        return False

  return True

def canGoRight():
  for line in BOARD:
    if(line[len(line) - 1] == '@'):
      return False
    
    for i, ele in enumerate(line):
      if(i != len(line) - 1 and line[i] == '@' and line[i + 1] == '#'):
        return False
  return True



def left(line):
  res = ''
  for i, ele in enumerate(line):
    if(i < len(line) - 1 and line[i + 1] == '@'):
      res += '@'
    elif(ele == '@'):
      res += '.'
    else:
      res += ele
  return res

def right(line):
  return reverse(left(reverse(line)))

def move(command):
  global BOARD
  OPERATION = None
  if(command == '<' and canGoLeft()):
    OPERATION = left
  if(command == '>' and canGoRight()):
    OPERATION = right

  if(OPERATION):
    for i, line in enumerate(BOARD):
      if(line.find('@') != -1):
        BOARD[i] = OPERATION(line)

BLOCKS_THROWN = 0

def towerHeight():
  res = 0
  for line in BOARD:
    if(line.find('#') != -1):
      res += 1
  return res

def loop(command):
  global throwBlock
  global BLOCKS_THROWN
  time.sleep(0.5)
  if(throwBlock):
    # print(BLOCKS_THROWN, towerHeight())
    BLOCKS_THROWN += 1
    addBlock()
  
  move(command)
  fall()

  printBoard()
  # print()

INDEX_COMMAND = 0
while(BLOCKS_THROWN < 30):
  loop(Lines[0][INDEX_COMMAND])
  INDEX_COMMAND = (INDEX_COMMAND + 1) % len(Lines[0])
