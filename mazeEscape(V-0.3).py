import time
import keyboard


maze_map = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,3,1,1,0,0,0,1,1,1,0,0,0,0,3,1],
  [1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1],
  [1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1],
  [1,0,0,0,0,0,1,0,0,0,0,3,1,0,1,1],
  [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1],
  [1,0,0,0,1,0,0,0,1,0,1,0,1,0,3,1],
  [1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1],
  [1,3,0,0,1,0,0,0,0,0,1,1,1,1,1,1],
  [1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1],
  [1,0,1,1,1,1,1,0,1,0,3,1,2,1,0,1],
  [1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1],
  [1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1],
  [1,3,1,0,0,0,0,0,3,1,1,1,0,1,3,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

player_position = [6, 3]
player_balance = 0

def get_block(map, y, x):
  block = map[y][x]
  return block

def action(map, position, move, balance):
  status = ''
  if move == 'W':
    position_change = [-1,0]
    status += 'вверх'
  elif move == 'S':
    position_change = [+1,0]
    status += 'вниз'
  elif move == 'D':
    position_change = [0,+1]
    status += 'вправо'
  elif move == 'A':
    position_change = [0,-1]
    status += 'влево'
  next_block = get_block(map, position[0]+position_change[0], position[1]+position_change[1])
  if next_block == 0:
    position[0] += position_change[0]
    position[1] += position_change[1]
    status += '.pass'
  elif next_block == 1:
    status += '.wall'
  elif next_block == 2:
    status += '.victory'
    position[0] += position_change[0]
    position[1] += position_change[1]
  elif next_block == 3:
    status += '.pass&coin'
    position[0] += position_change[0]
    position[1] += position_change[1]
    balance += 1
    map[position[0]][position[1]] = 0
  return(status, position, map, balance)

def getModule(number):
  if number < 0:
    number *= -1
  return number

def getNeededEnding(number):
  if 11 <= number <= 14:
    ending = 'ок'
  else:
    number = int(str(number)[-1])
    if number == 1:
      ending = 'ку'
    elif 2 <= number <= 4:
      ending = 'ки'
    else:
      ending = 'ок'
  return(ending)


print('Вы находитесь в лабиринте')
print('Доступные действия -\nХодьба: вверх(W), вниз(S), вправо(D), влево(A)')
while True:
  player_move = key = keyboard.read_key().upper()
  keyboard.press('backspace')
  if ['W', 'S', 'A', 'D'].__contains__(player_move):
    status, player_position, maze_map, player_balance = action(maze_map, player_position, player_move, player_balance)
    if status.split('.')[1] == 'pass':
      print('Вы перешли на клетку ' + status.split('.')[0])
    elif status.split('.')[1] == 'wall':
      print('Вы уткнулись в стену. Прохода ' + status.split('.')[0] + ' нет')
    elif status.split('.')[1] == 'victory':
      print('Вы нашли выход и выбрались из лабиринта')
      print('За игру вы собрали ' + str(player_balance) + ' монет'+ getNeededEnding(player_balance) +' из 9')
      print('Для выхода нажмите на Esc')
      keyboard.wait('esc')
      break
    elif status.split('.')[1] == 'pass&coin':
      print('Вы успешно перешли на клетку '+ status.split('.')[0] +' и нашли монетку, ваш баланс полнен на 1')
      print('Ваш баланc сейчас - ' + str(player_balance))
  time.sleep(0.2)