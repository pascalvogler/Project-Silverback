import maps
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
    BG_DARKGREY = '\033[48;5;8m'
    BG_WHITE = '\033[48;5;15m'
    ENDC = '\033[0m'


class player:
  def __init__(self, name, level=1, fight_state=0, player_type='Bot'):
    self.name = name
    self.level = level
    self.monsters = []
    self.items = []
    self.posx = None
    self.posy = None
    self.current_map = None
    self.fight_state = fight_state
    self.player_type = player_type
    self.map_display = maps.object_tile(**getattr(object_tiles, "p"))

  def __str__(self):
    return "Player name: {}".format(self.name)


  def addMonster(self, monster):
    self.monsters.append(monster)
    result_string = self.name + " gets a new "+monster.name
    return result_string
  