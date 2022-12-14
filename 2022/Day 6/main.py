def day6p1():
  with open('input.txt') as f:
    code = f.read()
  print(code)
  buffer = ''
  bad = False
  for i in range(len(code)):
    bad = False
    # all I did was change these to 14 for part 2
    if len(buffer) < 4:
      buffer += code[i]
    if len(buffer) == 4:
      for x in range(len(buffer)):
        for y in range(len(buffer)):
          if (buffer[x] == buffer[y]) and (x != y):
            bad = True
            break
        if bad:
          break
      if bad == False:
        print(f'{str(i+1)} {buffer}')
        return i
      else:
        buffer = buffer[1:] + code[i]
  return('help')
      
def day6p2():
  with open('input.txt') as f:
    code = f.read()
  print(code)
  buffer = ''
  bad = False
  for i in range(len(code)):
    bad = False
    if len(buffer) < 14:
      buffer += code[i]
    if len(buffer) == 14:
      for x in range(len(buffer)):
        for y in range(len(buffer)):
          if (buffer[x] == buffer[y]) and (x != y):
            bad = True
            break
        if bad:
          break
      if bad == False:
        print(f'{str(i+1)} {buffer}')
        return i
      else:
        buffer = buffer[1:] + code[i]
  return('help')

if __name__ == "__main__":
  print(day6p2())
  '''
  part 1: 1760
  part 2: 2974
  '''
