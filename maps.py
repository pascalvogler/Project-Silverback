import map_tiles
import object_tiles

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



class map_tile:
  def __init__(self, name=None, walkable=False, style="", tile_str=" "):
    self.name = name
    self.walkable = walkable
    self.tile_str = tile_str
    self._style = style
    self.obj_on_top = None

  @property
  def style_str(self):
    if self.obj_on_top == None:
      style_str = getattr(bcolors, self._style) + self.tile_str + bcolors.ENDC
    else:
      style_str = getattr(bcolors, self._style) + self.obj_on_top.map_display.style_str + bcolors.ENDC
    return style_str

  def placeObject(self, placed_object):
    ''' has to be type player or type item'''
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
  ''' creates map array from txt file
  Arguments: 
  arg_map: txt file
  Returns:
  list of lists with tiles'''

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
      print(map_list[i][y])
      # 
      tile_args = getattr(map_tiles,map_list[i][y])
      _map[i].append(map_tile(**tile_args))
  return _map
