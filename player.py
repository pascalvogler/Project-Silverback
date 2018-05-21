class player:
  def __init__(self, name, level=1, locx=1, locy=1, fight_state=0, player_type='Bot'):
    self.name = name
    self.level = level
    self.monsters = []
    self.items = []
    self.locx = locx
    self.locy = locy
    self.fight_state = fight_state
    self.player_type = player_type

  def __str__(self):
    return "Player name: {}".format(self.name)


  def addMonster(self, monster):
    self.monsters.append(monster)
    result_string = self.name + " gets a new "+monster.name
    return result_string
  