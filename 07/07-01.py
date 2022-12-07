input = open('input.txt', 'r')
Lines = input.read().splitlines()

pointer = '/'
fileSystem = {'/': 0}
lineIndex = 0

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

total = 0
for dir in sizes:
  if(sizes[dir] < 100000):
    total += sizes[dir]

print(total)