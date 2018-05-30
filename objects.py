import object_tiles
import object_functions
import maps


class container:
  def __init__(self, name="Chest", object_display="c"):
    # sim
    self.name = name
    self.object_display = object_display
    self.map_display = maps.object_tile(**getattr(object_tiles, self.object_display))
    self.posx = 0
    self.posy = 0

  def collisionAction(self, triggering_player):
    ''' This is the function that's called when a player walks into the object. Normally called from overworld.py 
    Arguments:
    triggering_player (player object): The player that triggered (touched) the object
    '''

    # To do: Open container, show contents, let player pick up items and add to their inventory. 
    object_functions.openContainer(triggering_player)


class door:
  def __init__(self, name="Door", object_display="d"):
    self.name = name
    self.object_display = object_display
    self.map_display = maps.object_tile(**getattr(object_tiles, self.object_display))
    self.posx = 0
    self.posy = 0

  def collisionAction(self, triggering_player):
    object_functions.openDoor(triggering_player)
