stacks = [['N', 'R', 'G', 'P'], ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'], ['M', 'S', 'V'], ['L ', 'S', 'R', 'C', 'Z', 'P'], ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'], ['C', 'T', 'N', 'W', 'D', 'M', 'S'], ['H', 'D', 'G', 'W', 'P'], ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'], ['R', 'P', 'F', 'L', 'W', 'G', 'Z']]

def day5p1():
  global stacks
  temp = 'HELP'
  with open('input.txt') as f:
    steps = f.read().splitlines()
    steps = steps
  for step in steps:
    amount = int(step.split(' ')[1])
    orig = int(step.split(' ')[3]) - 1
    goto = int(step.split(' ')[5]) - 1
    for i in range(amount):
      temp = stacks[orig][-1]
      del stacks[orig][-1]
      stacks[goto].append(temp)

  end = ''
  for i in stacks:
    end = end+str(i[-1])
  return end

def day5p2():
  global stacks
  temp = 'HELP'
  templ = []
  with open('input.txt') as f:
    steps = f.read().splitlines()
    steps = steps
  for step in steps:
    amount = int(step.split(' ')[1])
    orig = int(step.split(' ')[3]) - 1
    goto = int(step.split(' ')[5]) - 1
    for i in range(amount):
      temp = stacks[orig][-1]
      templ.append(temp)
      del stacks[orig][-1]
    for i in range(amount):
      temp = templ[-1]
      del templ[-1]
      stacks[goto].append(temp)

  end = ''
  for i in stacks:
    end = end+str(i[-1])
  return end


if __name__ == "__main__":
  print(day5p2())
  '''
  part 1: VPCDMSLWJ
  part 2: TPWCGNCCG
  '''
