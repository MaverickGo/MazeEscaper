import time

maze_map = [
  [1,1,1,1,1,1,1,1,1,1], #0
  [1,0,1,0,0,0,0,1,0,1], #1
  [1,0,1,0,0,1,0,1,0,1], #2
  [1,0,1,1,1,1,0,0,0,1], #3
  [1,0,0,0,0,0,0,1,0,1], #4
  [1,0,1,1,0,1,1,0,0,1], #5
  [1,1,1,0,0,0,0,1,0,1], #6
  [1,2,1,0,1,1,0,1,0,1], #7
  [1,0,0,0,0,1,0,0,0,1], #8
  [1,1,1,1,1,1,1,1,1,1]  #9
  #0,1,2,3,4,5,6,7,8,9
]

player_position = [1, 1]


def get_block(map, y, x):
  block = map[y][x]
  return block

def action(map, position, move):
  status = ''
  if move == 'W':
    position_change = [-1,0]
  elif move == 'S':
    position_change = [+1,0]
  elif move == 'D':
    position_change = [0,+1]
  elif move == 'A':
    position_change = [0,-1]
  next_block = get_block(map, position[0]+position_change[0], position[1]+position_change[1])
  if next_block == 0:
    position[0] += position_change[0]
    position[1] += position_change[1]
    status = 'pass'
  elif next_block == 1:
    status = 'wall'
  elif next_block == 2:
    status = 'victory'
    position[0] += position_change[0]
    position[1] += position_change[1]
  return(status, position)


print('Вы находитесь в лабиринте')
print('Доступные ходы - вверх(W), вниз(S), вправо(D), влево(A)')
while True:
  player_move = str(input('Куда бы вы хотели пойти?\n')).upper()
  if player_move != None:
    status, player_position = action(maze_map, player_position, player_move)
    #print(status, player_position)
    if status == 'pass':
      print('Вы успешно перешли на следующую клетку')
    elif status == 'wall':
      print('Перед вами стена. Вы остались на той же клетке')
    elif status == 'victory':
      print('Вы победили')
      time.sleep(5)
      break
  else:
    print('Введите корректное действие')