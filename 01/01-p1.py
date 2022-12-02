input = open('input.txt', 'r')
Lines = input.readlines()
  
maxCalories = 0
currentCalories = 0
for line in Lines:
  if(line == '\n'):
    if(currentCalories > maxCalories):
      maxCalories = currentCalories
    currentCalories = 0
    continue

  currentCalories += int(line)

print(maxCalories)