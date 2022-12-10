input = open('input.txt', 'r')
Lines = input.read().splitlines()

Register = 1
Cycle = 0
Output = ''

def nextCycle():
  global Cycle
  global Output

  if(Cycle >= Register - 1 and Cycle <= Register + 1):
    Output += '#'
  else:
    Output += '.'

  Cycle += 1
  if(Cycle == 40):
    Output += '\n'
    Cycle = 0

for cmd in Lines:
  nextCycle()
  if(cmd == 'noop'):
    continue

  nextCycle()
  [op, val] = cmd.split(' ')
  Register += int(val)

print(Output)