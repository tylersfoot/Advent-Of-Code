def day2p1():
  score = 0
  f = open('input.txt', 'r')
  lines = f.readlines()

  for line in lines:
    move1, move2 = line.strip()[0:2]
    
    # checks for tie
    if ((move1=='A' and move2=='X') or (move1=='B' and move2=='Y') or (move1=='C' and move2=='Z')):
      score+=3
    if move2 == 'X': #rock
      score+=1
      if move1 == 'C':
        score+=6
    elif move2 == 'Y': #paper
      score+=2
      if move1 == 'A':
        score+=6
    elif move2 == 'Z': #scissors
      score+=3
      if move1 == 'B':
        score+=6
    print(f'score {score} move1 {move1} move2 {move2}')
  return score

def day2p2():
  score = 0
  f = open('input.txt', 'r')
  lines = f.readlines()

  for line in lines:
    move1 = line.strip()[0]
    move2 = line.strip()[2]

    if move2 == 'X':
      move2 = 'A'
    if move2 == 'Y':
      move2 = 'B'
    if move2 == 'Z':
      move2 = 'C'

    if move2 == 'B':
      move2 = move1
    elif move2 == 'C':
      if move1 == 'A':
        move2 = 'B'
      elif move1 == 'B':
        move2 = 'C'
      else:
        move2 = 'A'
    elif move2 == 'A':
      if move1 == 'A':
        move2 = 'C'
      elif move1 == 'B':
        move2 = 'A'
      else:
        move2 = 'B'

    
    # checks for tie
    if move1 == move2:
      score+=3
    if move2 == 'A': #rock
      score+=1
      if move1 == 'C':
        score+=6
    elif move2 == 'B': #paper
      score+=2
      if move1 == 'A':
        score+=6
    elif move2 == 'C': #scissors
      score+=3
      if move1 == 'B':
        score+=6
    print(f'score {score} move1 {move1} move2 {move2}')
  return score
    
          
if __name__ == "__main__":
  print(day2p2())
