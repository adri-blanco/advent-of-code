input = open('input.txt', 'r')
Lines = input.read().splitlines()

pointer = '/'
fileSystem = {'/': 0}
lineIndex = 0
UsedSpace = 0

def cd(arg):
  if(arg == '/'):
    return '/'
  
  if(arg == '..'):
    newPointer = pointer.split('/')
    newPointer.pop()
    return '/'.join(newPointer)
  
  if(pointer == '/'):
    return '/' + arg

  return pointer + '/' + arg

def ls():
  global lineIndex
  global UsedSpace
  while(lineIndex < len(Lines)):
    if(Lines[lineIndex].find('$') != -1):
      break
    output = Lines[lineIndex]
    info = output.split()

    if(info[0] == 'dir'):
      if(pointer == '/'):
        fileSystem['/' + info[1]] = 0
      else:
        fileSystem[pointer + '/' + info[1]] = 0
        

    if(info[0] != 'dir'):
      UsedSpace += int(info[0])
      fileSystem[pointer] += int(info[0])

    lineIndex += 1

def runCommand(input):
  global pointer
  global lineIndex
  cmd = input.split()
  if(cmd[1] == 'cd'):
    pointer = cd(cmd[2])
    lineIndex += 1

  if(cmd[1] == 'ls'):
    lineIndex += 1
    ls()

while(lineIndex < len(Lines)):
  runCommand(Lines[lineIndex])

sizes = {}
for dir in fileSystem:
  for innerDir in fileSystem:
    if(innerDir.startswith(dir)):
      if(not dir in sizes):
        sizes[dir] = fileSystem[innerDir]
      else:
        sizes[dir] += fileSystem[innerDir]

TotalSpace = 70000000
NeededSpace = 30000000
AvailableSpace = TotalSpace - UsedSpace
sizes = list(sizes.values())
sizes.sort()

value = 0
for size in sizes:
  if(AvailableSpace + size > NeededSpace):
    value = size
    break
print(value)
