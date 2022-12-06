def day1():
  calories = []
  tempCal = 0
  f = open('input.txt', 'r')
  lines = f.readlines()

  for line in lines:
    if line.strip() == '':
      calories.append(tempCal)
      tempCal = 0
    else:
      tempCal += int(line.strip())
    # print(f'temp {tempCal}')
  calories = sorted(calories, reverse=True)
  
  return f'Top elf: {calories[0]}\n Top three elves added: {calories[0]+calories[1]+calories[2]}'
          
          
if __name__ == "__main__":
  print(day1())
