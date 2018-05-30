import maps
import player as p
import fight
from random import randint

players_arr = []

def movePlayer(arg_player, direction):
  ''' 
  Arguments:
  player: Player object that is to be moved
  direction: string, has to be 'n' 'e' 's' 'w' for north east south west

  If move is possible, changes player coordinates posx and posy

  Returns: 
  1 if move worked, 0 if it didn't
  '''
  player_current_pos = [arg_player.posx, arg_player.posy]
  player_map = arg_player.current_map
  map_data = player_map.map_data
  movement_matrix = {
    'n': [0,-1],
    'e': [1,0],
    's': [0,1],
    'w': [-1,0]
  }
  # move player
  player_desired_pos = [player_current_pos[i]+movement_matrix[direction][i] for i in range(len(player_current_pos))]
  desired_tile = map_data[player_desired_pos[1]][player_desired_pos[0]]
  if(desired_tile.walkable == False):
    print("Can't go there")
    return 0
  elif desired_tile.obj_on_top != None:
    # If there's an obj_on_top of the tile, trigger that object's collisionAction
    desired_tile.obj_on_top.collisionAction(arg_player)
  else:
    # If tile is walkable and no object on top, remove player from current tile and place on next tile
    player_map.removeObject(arg_player.posx, arg_player.posy)
    arg_player.posx = player_desired_pos[0]
    arg_player.posy = player_desired_pos[1]
    player_map.placeObject(arg_player.posx, arg_player.posy, arg_player)
    return 1

def spawnObject(obj, posx, posy, spawn_map):
  ''' Assigns player to map_tile, sets player location properties '''

  players_arr.append(obj) # TO DO: MOVE TO GAME_MAP OBJECT

  if type(obj)==p.player:
    obj.current_map = spawn_map
    obj.posx = posx
    obj.posy = posy
  spawn_map.placeObject(posx, posy, obj)

def randomSpawn(obj, spawn_map):
  '''
  Spawns an object at a random walkable position on the map
  Args:
  obj (Object or Player object): object to be placed
  spawn_map (game_map object): map on which object is to be spawned
  '''
  map_data = spawn_map.map_data
  map_height = len(map_data)
  map_width = len(map_data[0])
  pos_x = randint(1, map_width-1)
  pos_y = randint(1, map_height-1)
  if(map_data[pos_y][pos_x].walkable == False):
    randomSpawn(obj, spawn_map)
  else:
    spawnObject(obj, pos_x, pos_y, spawn_map)


def despawnPlayer(player):
  ''' 
  Removes player from map_tile, sets player location properties to None 
  Args:
  player (Player object): player to despawn
  '''
  player_current_pos = [player.posx, player.posy]
  # Remove object that is on top of player tile (which is itself)
  player.current_map.removeObject(player.posx, player.posy)
  player.current_map = None
  player.posx = None
  player.posy = None

def drawMap(player, themap):
  ''' draws the map in the console.
  Arguments: 
  player: the player, for whom the map is drawn
  themap: list of lists with tile objects
  '''
  #viewport has to be even int!
  VIEWPORT_H = 32
  VIEWPORT_V = 12
  # get player position and deduct 1/2 viewport towards left and top
  display_center_v = player.posy
  display_center_h = player.posx
  display_top_left = [display_center_v-int(VIEWPORT_V/2), display_center_h-int(VIEWPORT_H/2)]
  map_data = themap.map_data
  viewport_map = []
  for i in range(len(map_data)):
    if display_top_left[0] <= i <= display_top_left[0]+VIEWPORT_V:
      # for all lines within viewport add new empty list
      viewport_map.append([])
      cur_vp_map_line = len(viewport_map)-1
      for j in range(len(map_data[i])):
        if display_top_left[1] <= j <= display_top_left[1]+VIEWPORT_H:
          # for all tiles within viewport, add tile
          viewport_map[cur_vp_map_line].append(map_data[i][j])



  # new array with just the tiles to be drawn
  # clear screen
  print("\033[2J")
  # move cursor top left
  print("\033[H")
  for line in viewport_map:
    linestr = ""
    #debugstr = ""
    for tile in line:
      linestr += tile.style_str
      #debugstr = tile.obj_on_top
      #print(debugstr)
    print(linestr)

