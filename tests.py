import monsters
import spell
import player
import fight
import overworld
import maps

# change directory to directory of this file, for importing maps
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# TESTS 

# Create animals
spell_animal_2 = monsters.Spell_Animal(
  "Harpy Sorceress",
  "Mammal", 
  "Forest", 
  "Uses the element of wind to smash her enemies into a thousand pieces", 
  strength=20, 
  agility=30, 
  intelligence=30, 
  stamina=20, 
  spells=[], 
  level=1
  )

spell_animal_1 = monsters.Spell_Animal(
  "Green Blob", 
  "Mammal", 
  "Forest", 
  "Uses the element of wind to smash her enemies into a thousand pieces", 
  strength=20, 
  agility=30, 
  intelligence=30, 
  stamina=20, 
  spells=[], 
  level=1
  )

spell_animal_3 = monsters.Spell_Animal(
  "Goblin King", 
  "Mammal", 
  "Forest", 
  "Uses the element of wind to smash her enemies into a thousand pieces", 
  strength=20, 
  agility=30, 
  intelligence=30, 
  stamina=20, 
  spells=[], 
  level=1
  )

spell_animal_4 = monsters.Spell_Animal(
  "Silverback Wizard", 
  "Mammal", 
  "Forest", 
  "Aber so was vomene krasse Schlaeger", 
  strength=1, 
  agility=1, 
  intelligence=1, 
  stamina=1, 
  spells=[], 
  level=20
  )


# Summon four spells
sp_heavy_bolt_fire = spell.summonSpell(spell='bolt', element='fire', modifier='heavy')
sp_cunning_bolt_ice = spell.summonSpell(spell='bolt', element='ice', modifier='cunning')
sp_weak_blast_ice = spell.summonSpell(spell='blast', element='ice', modifier='weak')
sp_weak_bolt = spell.summonSpell(spell='bolt', modifier='weak')
sp_heavy_blast = spell.summonSpell(spell='blast', modifier='heavy')
sp_cunning_blast = spell.summonSpell(spell='blast', modifier='cunning')

# crit 100% for testing
sp_cunning_blast.crit = 1

# Teach each animal two of the spells
spell_animal_1.learnSpell(sp_heavy_bolt_fire)
spell_animal_1.learnSpell(sp_cunning_bolt_ice)
spell_animal_2.learnSpell(sp_weak_blast_ice)
spell_animal_3.learnSpell(sp_heavy_blast)
spell_animal_3.learnSpell(sp_weak_bolt)
spell_animal_4.learnSpell(sp_cunning_blast)

# Print animals with spells using spell.Spell.__str__
print("Listing monsters...")
print("\n")
print(spell_animal_2.name)
print(spell_animal_2.name+ " has the following spells:")
for spell in spell_animal_2.spells:
    print(spell)
print("\n")
print(spell_animal_1.name)
print(spell_animal_1.name+ " has the following spells:")
for spell in spell_animal_1.spells:
    print(spell)
print("\n")

# Create two players
player1 = player.player(
  name="Johnny", 
  player_type='bot',
  object_display='p'
  )

player2 = player.player(
  name="Jenny", 
  player_type='bot',
  object_display='p'
  )

pack_of_tigers = player.player(
  name="Pack of Tigers",
  player_type = 'bot', 
  object_display='t'
  )

# give 3 tigers to pack_of_tigers
for i in range(3):
  monster_tiger = monsters.Spell_Animal(
    "Tiger",
    "Mammal", 
    "Forest", 
    "Is hungry", 
    strength=15, 
    agility=15, 
    intelligence=15, 
    stamina=10, 
    spells=[], 
    level=1
    )
  pack_of_tigers.addMonster(monster_tiger)

#give monsters to players
print(player1.addMonster(spell_animal_1))
print(player1.addMonster(spell_animal_2))
print(player2.addMonster(spell_animal_3))
print(player2.addMonster(spell_animal_4))

print("creating map...")
this_map = maps.createMap("maps/map1.txt")

print("spawning player 1")
overworld.spawnPlayer(
  player=player1, 
  posx=8, 
  posy=8,
  spawn_map = this_map
  )

print("spawning player 2")
overworld.spawnPlayer(
  player=player2,
  posx=15, 
  posy=14,
  spawn_map = this_map
  )

print("spawning pack of tigers")
overworld.spawnPlayer(
  player=pack_of_tigers, 
  posx=8, 
  posy=13,
  spawn_map = this_map
  )

overworld.drawMap(this_map)

while True: 
  command = input("Move (n, e, s, w): ")
  if command in ("n", "e", "s", "w"):
    print("moving Player 1: "+command)
    overworld.movePlayer(player1, command)
    # Tests for changing cursor position
    #print("\0337")
    #print("\033[2J")
    #print("\033[H")
    overworld.drawMap(this_map)
    #print("\0338")

  else:
    print("invalid input")

