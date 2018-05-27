import maps
import player
import fight

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
  movement_matrix = {
    'n': [-1,0],
    'e': [0,1],
    's': [1,0],
    'w': [0,-1]
  }
  # move player
  player_desired_pos = [player_current_pos[i]+movement_matrix[direction][i] for i in range(len(player_current_pos))]
  desired_tile = player_map[player_desired_pos[0]][player_desired_pos[1]]
  if(desired_tile.walkable == False):
    print("Can't go there")
    return 0
  else:
    if(type(desired_tile.obj_on_top) == player.player):
      fight_winner = fight.startFight(arg_player, desired_tile.obj_on_top, player_desired_pos[0], player_desired_pos[1])
      # remove loser from game, put winner where he belongs
    else:
      player_map[arg_player.posx][arg_player.posy].removeObject()
      arg_player.posx = player_desired_pos[0]
      arg_player.posy = player_desired_pos[1]
      player_map[arg_player.posx][arg_player.posy].placeObject(arg_player)
      return 1

def spawnPlayer(player, posx, posy, spawn_map):
  player.posx = posx
  player.posy = posy
  players_arr.append(player)
  player_map = spawn_map
  player.current_map = spawn_map
  player_map[posx][posy].placeObject(player)

def drawMap(themap):
  ''' draws the map in the console.
  Arguments: 
  themap: list of lists with tile objects
  '''
  # clear screen
  print("\033[2J")
  # move cursor top left
  print("\033[H")
  for line in themap:
    linestr = ""
    #debugstr = ""
    for tile in line:
      linestr += tile.style_str
      #debugstr = tile.obj_on_top
      #print(debugstr)
    print(linestr)

