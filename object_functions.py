import maps
import random_map_test
import objects
import overworld

def openDoor(player):
  # create new random map
  random_map = random_map_test.randomMap()
  this_map = maps.createMapFromList(random_map)

  #change player's assigned map
  player.current_map = this_map

  #spawn player and an exit door on new map
  _door = objects.door()
  overworld.randomSpawn(_door, this_map)
  overworld.randomSpawn(player, this_map)

def openContainer(player):
  pass