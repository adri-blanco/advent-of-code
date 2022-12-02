input = open('input.txt', 'r')
Lines = input.readlines()

elfs = []
currentCalories = 0
for line in Lines:
  if(line == '\n'):
    elfs.append(currentCalories)
    currentCalories = 0
    continue

  currentCalories += int(line)

elfs.sort(reverse=True);
print(elfs[0]);
print(elfs[1]);
print(elfs[2]);
print(elfs[0] + elfs[1] + elfs[2]);
