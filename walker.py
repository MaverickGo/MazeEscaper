world = [
  [1,1,1,1], #0
  [1,0,0,1], #1
  [1,0,0,1], #2
  [1,1,1,1]  #3
  #0,1,2,3
]
playerPosition = [2, 1] # [y, x]
movements = {
  'Вверх': 'w',
  'Вниз': 's',
  'Вправо': 'd',
  'Влево': 'a',
}
def action(move, currentPosition, world):
  status = ''
  if move=='w':
    print(world[playerPosition[0]-1][playerPosition[1]])
    if world[playerPosition[0]-1][playerPosition[1]] == 0:
      currentPosition[0] -= 1
      status = 'success'
    elif world[playerPosition[0]-1][playerPosition[1]] == 1:
      status = 'fail'
  elif move=='s':
    #block = world[playerPosition[0]+1][playerPosition[1]]
    if world[playerPosition[0]+1][playerPosition[1]] == 0:
      currentPosition[0] += 1
      status = 'success'
    elif world[playerPosition[0]+1][playerPosition[1]] == 1:
      status = 'fail'
  elif move=='d':
    #block = world[playerPosition[0]][playerPosition[1]+1]
    if world[playerPosition[0]][playerPosition[1]+1] == 0:
      currentPosition[1] += 1
      status = 'success'
    elif world[playerPosition[0]][playerPosition[1]+1] == 1:
      status = 'fail'
  elif move=='a':
    #block = world[playerPosition[0]][playerPosition[1]-1]
    if world[playerPosition[0]][playerPosition[1]-1] == 0:
      currentPosition[1] -= 1
      status = 'success'
    elif world[playerPosition[0]][playerPosition[1]-1] == 1:
      status = 'fail'
  return(status, playerPosition)

print('Вы находитесь в лабиринте')
while True:
  my_input = input('Куда бы вы хотели пойти?\n')
  #try:
  move = movements.get(my_input)
    #print(move)
  #action(move, playerPosition, world))
  status, playerPosition = action(move, playerPosition, world)
  print(status, playerPosition)
  #except:
  #  print('Введите корректное действие')