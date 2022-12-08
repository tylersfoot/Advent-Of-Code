def day4p1():
  with open('input.txt') as f:
    pairs = f.read().splitlines()
  count = 0
  for pair in pairs:
    p1 = (pair.split(',')[0]).split('-')
    p2 = (pair.split(',')[1]).split('-')
    p1[0], p1[1], p2[0], p2[1] = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
    if ((p1[0]<=p2[0]) and (p1[1] >= p2[1])):
      count+=1
    elif ((p1[0] >= p2[0]) and (p1[1] <= p2[1])):
      count+=1
  return count

def day4p2():
  with open('input.txt') as f:
    pairs = f.read().splitlines()
  count = 0
  for pair in pairs:
    p1 = (pair.split(',')[0]).split('-')
    p2 = (pair.split(',')[1]).split('-')
    p1[0], p1[1], p2[0], p2[1] = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
    if ((p1[0] <= p2[0]) and (p1[1] >= p2[1])):
      count+=1
    elif ((p1[0] >= p2[0]) and (p1[1] <= p2[1])):
      count+=1
    elif ((p1[0] <= p2[0]) and (p1[1] >= p2[0])):
      count+=1
    elif ((p1[0] <= p2[1]) and (p1[1] >= p2[1])):
      count+=1
  return count

if __name__ == "__main__":
  print(day4p2())
  '''
  part 1: 448
  part 2: 794
  '''
