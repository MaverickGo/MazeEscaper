import time
import keyboard


maze_map = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,1,3,1,0,0,0,0,1,0,1,0,0,0,1],
  [1,0,1,0,1,1,1,1,0,1,0,1,3,1,0,1],
  [1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1],
  [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1],
  [1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1],
  [1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1],
  [1,0,0,1,3,0,1,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
  [1,3,1,0,0,0,0,1,2,0,0,0,0,1,3,1],
  [1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1],
  [1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1],
  [1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1],
  [1,0,0,0,1,3,0,0,0,1,1,1,1,0,1,1],
  [1,0,1,0,1,0,0,1,0,0,0,3,1,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

player_position = [1, 1]

player_balance = 0

def get_block(map, y, x):
  block = map[y][x]
  return block

def action(map, position, move, balance):
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
  elif next_block == 3:
    status = 'pass&coin'
    position[0] += position_change[0]
    position[1] += position_change[1]
    balance += 1
    map[position[0]][position[1]] = 0
  return(status, position, map, balance)

def print_gradually(text, delay):
  for letter in text:
    print(letter, end='')
    time.sleep(delay)
  print('\n')


print('Вы находитесь в лабиринте')
print('Доступные действия -\nХодьба: вверх(W), вниз(S), вправо(D), влево(A)')
while True:
  player_move = key = keyboard.read_key().upper()
  keyboard.press('backspace')
  if ['W', 'S', 'A', 'D'].__contains__(player_move):
    status, player_position, maze_map, player_balance = action(maze_map, player_position, player_move, player_balance)
    if status == 'pass':
      print_gradually('Вы успешно перешли на следующую клетку', 0.05)
    elif status == 'wall':
      print_gradually('Перед вами стена. Вы остались на той же клетке', 0.05)
    elif status == 'victory':
      print_gradually('Вы победили', 0.05)
      print_gradually('За игру вы смогли собрать ' + str(player_balance) + ' монеток из 7', 0.05)
      time.sleep
      break
    elif status == 'pass&coin':
      print_gradually('Вы успешно перешли на следующую клетку и нашли монетку, ваш баланс полнен на 1', 0.05)
      print_gradually('Ваш балан сейчас - ' + str(player_balance), 0.05)
    time.sleep(0.2)