import map_tiles
import object_tiles
import objects

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG_GREY = '\033[48;5;7m'
    BG_BLUE = '\033[48;5;20m'
    BG_DARKGREY = '\033[48;5;8m'
    BG_WHITE = '\033[48;5;15m'
    ENDC = '\033[0m'

class game_map:
  def __init__(self, map_data, name="noname"):
    self.name = name
    self.width = len(map_data)
    self.height = len(map_data[0])
    self.map_data = map_data

  def placeObject(self, posx, posy, placed_object):
    self.map_data[posy][posx].placeObject(placed_object)

  def removeObject(self, posx, posy):
    self.map_data[posy][posx].removeObject()





class map_tile:
  def __init__(self, name=None, walkable=False, style="", tile_str=" "):
    self.name = name
    self.walkable = walkable
    self.tile_str = tile_str
    self._style = style
    self.obj_on_top = None

  @property
  def style_str(self):
    ''' 
    Returns this tile's style string
    Background color is the tile's own (according to map_tiles.py)
    If an object is on top of the tile, prints that object's tile string (character and color according to object_tiles.py) instead of the usual " " for empty tiles
    ''' 
    if self.obj_on_top == None:
      style_str = getattr(bcolors, self._style) + self.tile_str + bcolors.ENDC
    else:
      style_str = getattr(bcolors, self._style) + self.obj_on_top.map_display.style_str + bcolors.ENDC
    return style_str

  def placeObject(self, placed_object):
    ''' 
    Places an object on top of the tile.
    Args:
    placed_object (player or type object)
    '''
    self.obj_on_top = placed_object

  def removeObject(self):
    self.obj_on_top = None

class object_tile:
  def __init__(self, name, walkable=True, style="", object_str=" "):
    self.name = name
    self.walkable = walkable
    self.object_str = object_str
    self._style = style

  @property
  def style_str(self):
    style_str = getattr(bcolors, self._style) + self.object_str
    return style_str


def createMap(arg_map):
  ''' creates map from txt file
  Arguments: 
  arg_map (path to .txt file): Text file of characters (see object_tiles.py)
  Returns:
  (game_map object)
  '''

  # open file at path, read line by line into map_list
  with open(arg_map) as f:
    map_list = f.readlines()
  # remove breaks
  map_list = [x.strip() for x in map_list]
  # create new list to populate with map_tile objects
  _map = []
  # for each line
  for i in range(len(map_list)):
    # add a new empty list to _map
    _map.append([])
    # for each character of this line
    for y in range(len(map_list[i])):
      tile_args = getattr(map_tiles,map_list[i][y])
      _map[i].append(map_tile(**tile_args))
  result_map = game_map(map_data=_map)
  return result_map

def createMapFromList(arg_map):
  ''' create map from list of lists
  Args:
  arg_map (list of lists): LoL of characters (see object_tiles.py)
  Returns:
  List of Lists of map_tile objects
  '''
  map_list = arg_map
  _map = []
  # for each line
  for i in range(len(map_list)):
    # add a new empty list to _map
    _map.append([])
    # for each character of this line
    for y in range(len(map_list[i])):
      tile_args = getattr(map_tiles,map_list[i][y])
      _map[i].append(map_tile(**tile_args))
  result_map = game_map(map_data=_map)
  placeDoor(result_map)
  return result_map

def placeDoor(map_obj):
  ''' Scans a map for door tiles and places a door object on top if found.
  Args:
  map_obj (map object)
  Returns:
  True if door is placed
  NOTE: Currently only places a single door (first 'Door' tile found)
  False if no door is placed
  '''
  for line in map_obj.map_data:
    for tile in line:
      if tile.name == "Door":
        _door = objects.door()
        tile.placeObject(_door)
        return True
  return False
