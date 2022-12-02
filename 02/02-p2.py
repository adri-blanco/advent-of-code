# By the definition of the problem
# A = Rock
# B = Paper
# C = Scissors
#
# X = Loss
# Y = Draw
# Z = Win

def getMyMove(move, result):
  dictionary = {
    "A": {
      "X": "C",
      "Y": "A",
      "Z": "B"
    },
    "B": {
      "X": "A",
      "Y": "B",
      "Z": "C"
    },
    "C": {
      "X": "B",
      "Y": "C",
      "Z": "A"
    },
  }
  return dictionary[move][result];

def getScoreByMove(myMove):
  scoreByMove = {
    "A": 1,
    "B": 2,
    "C": 3,
  }
  return scoreByMove[myMove];

def getScoreByMatch(myMove, rivalMove):
  if(myMove == rivalMove):
    return 3

  if((myMove == 'A' and rivalMove == 'C') or (myMove == 'B' and rivalMove == 'A') or (myMove == 'C' and rivalMove == 'B')):
    return 6
  
  return 0

def getScore(myMove, rivalMove):
  return getScoreByMove(myMove) + getScoreByMatch(myMove, rivalMove)

input = open('input.txt', 'r')
Lines = input.readlines()

score = 0
for line in Lines:
  [rivalMove, result] = line.replace('\n', '').split(' ')
  myMove = getMyMove(rivalMove, result)
  score += getScore(myMove, rivalMove)

print(score)

  