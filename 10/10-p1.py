input = open('input.txt', 'r')
Lines = input.read().splitlines()

Register = 1
Cycle = 0
SignalStrength = 0
Checks = [20, 60, 100, 140, 180, 220]

def nextCycle():
  global Cycle
  global SignalStrength
  Cycle += 1
  if (Cycle in Checks):
    SignalStrength += Register * Cycle

for cmd in Lines:
  nextCycle()
  if(cmd == 'noop'):
    continue

  nextCycle()
  [op, val] = cmd.split(' ')
  Register += int(val)

print('Cycle: ', Cycle)
print('Register: ', Register)
print('SignalStrength: ', SignalStrength)