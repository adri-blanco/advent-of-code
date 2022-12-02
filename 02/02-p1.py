# By the definition of the problem
# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

def translate(move):
  dictionary = {
    "X": "A",
    "Y": "B",
    "Z": "C"
  }
  return dictionary[move];

def getScoreByMove(myMove):
  scoreByMove = {
    "X": 1,
    "Y": 2,
    "Z": 3,
  }
  return scoreByMove[myMove];

def getScoreByMatch(myMove, rivalMove):
  if(myMove == rivalMove):
    return 3

  if((myMove == 'A' and rivalMove == 'C') or (myMove == 'B' and rivalMove == 'A') or (myMove == 'C' and rivalMove == 'B')):
    return 6
  
  return 0

def getScore(myMove, rivalMove):
  return getScoreByMove(myMove) + getScoreByMatch(translate(myMove), rivalMove)

input = open('input.txt', 'r')
Lines = input.readlines()

score = 0
for line in Lines:
  [rivalMove, myMove] = line.replace('\n', '').split(' ')
  score += getScore(myMove, rivalMove)

print(score)

  