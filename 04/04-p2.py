input = open('input.txt', 'r')
Lines = input.readlines()

def toInt(string):
  return int(string)

def getJobLimits(job):
  split = job.split('-')
  return list(map(toInt, split))

def isJobOverlap(job1, job2):
  [job1Start, job1End] = job1
  [job2Start, job2End] = job2
  return job1End < job2Start

counter = 0
for line in Lines:
  [elf1, elf2] = line.replace('\n', '').split(',')
  job1 = getJobLimits(elf1)
  job2 = getJobLimits(elf2)
  
  if(not isJobOverlap(job1, job2) and not isJobOverlap(job2, job1)):
    counter += 1

print(counter)