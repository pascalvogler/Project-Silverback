from random import randint
from random import choice

def randomMap(size=choice(range(16,48,2))):

  def randomizeTile(current_tile, tile_before, num_steps_direction):
    random_1 = randint(1,100)/100
    if (map[tile_before[0]][ tile_before[1]] == 'h' or map[tile_before[0]][ tile_before[1]] == 'x'):
      if random_1 <= (0.3*num_steps_direction+1-current_step)/(0.3 * num_steps_direction) - numAdjacentCells(current_tile, 'm')*0.2:
        map[current_tile[0]][ current_tile[1]] = 'h'
      else:
        map[current_tile[0]][ current_tile[1]] = 'm'
    elif map[tile_before[0]][ tile_before[1]] == 'm':
      if random_1 <= (0.3*num_steps_direction+1-current_step)/ (0.3 * num_steps_direction) - numAdjacentCells(current_tile, 'o')*0.2:
        map[current_tile[0]][ current_tile[1]] = 'm'
      else:
        map[current_tile[0]][ current_tile[1]] = 'o'

    elif map[tile_before[0]][ tile_before[1]] == 'o':
      #if random_1 <= (0.3*num_steps_direction+1-current_step)/ (0.3 * num_steps_direction) - numAdjacentCells(current_tile, 'o')*0.2:
      #  map[current_tile[0]][ current_tile[1]] = 'm'
      #else:
        map[current_tile[0]][ current_tile[1]] = 'o'

  def numAdjacentCells(current_tile, value):
    ''' returns number of values around current tile that have provided value 
    Arguments: 
    current_tile (tuple [y,x]): tile to check for adj cells
    value (string): tile char to check for
    Returns:
    int
    '''
    adjacent_top = [current_tile[0]-1, current_tile[1]]
    adjacent_bot = [current_tile[0]+1, current_tile[1]]
    adjacent_left = [current_tile[0], current_tile[1]-1]
    adjacent_right = [current_tile[0], current_tile[1]+1]
    adj_list = [adjacent_top, adjacent_bot, adjacent_right, adjacent_left]
    num_adj_cells = 0
    for item in adj_list:
      if map[item[0]][item[1]] == value:
        num_adj_cells +=1
    return num_adj_cells



  map_height = size
  map_width = map_height+choice(range(0,8,2))

  map = []

  for i in range(map_height):
    map.append([])
    for y in range(map_width):
      map[i].append("x")

  num_steps_width = int(map_width/2)

  num_steps_height = int(map_height/2)

  num_steps = 0

  if num_steps_width < num_steps_height:
    num_steps = num_steps_width
  else:
    num_steps = num_steps_height

  current_step = 1

  while(current_step<num_steps):
    for i in range(map_height):
      for j in range(map_width):
        if i == current_step and (current_step<=j<=map_width-1-current_step):
         #TOP LINE
         tile_before = [i-1,j]
         current_tile = [i,j]
         randomizeTile(current_tile, tile_before, num_steps_width)
        elif map_height-1-current_step == i and (current_step<=j<=map_width-1-current_step):
         #BOTTOM LINE
         tile_before = [map_height-1-current_step+1,j]
         current_tile = [i,j]
         randomizeTile(current_tile, tile_before, num_steps_width)
        elif current_step <= i <= map_height-1-current_step and j == current_step:
         #LEFT LINE
         tile_before = [i,j-1]
         current_tile = [i,j]
         randomizeTile(current_tile, tile_before, num_steps_height)
        elif current_step <= i <= map_height-1-current_step and (map_width-1-current_step == j):
         # RIGHT LINE
         tile_before = [i,map_width-1-current_step+1]
         current_tile = [i,j]
         randomizeTile(current_tile, tile_before, num_steps_height)
    current_step+=1
  
  # Replace all unreachable 'o' tiles with 'm' tiles
  for i in range(map_height):
    for j in range(map_width):
      if map[i][j] == 'o' and numAdjacentCells([i,j],'m')+numAdjacentCells([i,j],'h')==4:
        map[i][j] = 'm'


  return map

def randomEmptyRoom(size=choice(range(6,16,2)), entrance='left'):
  map_height = size
  map_width = map_height+choice(range(-2,4,2))
  map = []
  for i in range(map_height):
    map.append([])
    for y in range(map_width):
      map[i].append("o")

  for i in range(map_height):
    map[i][0] = "x"
    map[i][map_width-1] = "x"
  for j in range(map_width):
    map[0][j] = "x"
    map[map_height-1][j] = "x"
    
  if entrance=='left':
    entrance_pos_vertical = randint(3, map_height-2)
    map[entrance_pos_vertical][0] = "d"
  elif entrance=='right':
    entrance_pos_vertical = randint(3, map_height-2)
    map[entrance_pos_vertical][map_width-1] = "d"
  elif entrance=='top':
    entrance_pos_horizontal = randint(3, map_width-2)
    map[0][entrance_pos_horizontal] = "d"
  elif entrance=='bottom':
    entrance_pos_horizontal = randint(3, map_width-2)
    map[map_height-1][entrance_pos_horizontal] = "d"

  return map






