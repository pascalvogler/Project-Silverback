import monsters
import spell
import player

# TESTS 

# Create two animals
physical_animal_1 = monsters.Physical_Animal("Silverback", "Mammal", "Forest", "Aber so was vomene krasse Schlaeger", 80, 40, 30, 80, 100, 20, "1")
spell_animal_1 = monsters.Spell_Animal("Silverback Wizard", "Mammal", "Forest", "Aber so was vomene krasse Schlaeger", 80, 40, 30, 80, 500, 20, "1")


# Summon four spells
sp_heavy_bolt_fire = spell.summonSpell(spell='bolt', element='fire', modifier='heavy')
sp_cunning_bolt_ice = spell.summonSpell(spell='bolt', element='ice', modifier='cunning')
sp_weak_blast_ice = spell.summonSpell(spell='blast', element='ice', modifier='weak')
sp_bolt = spell.summonSpell(spell='bolt')

# Teach each animal two of the spells
spell_animal_1.learnSpell(sp_heavy_bolt_fire)
spell_animal_1.learnSpell(sp_cunning_bolt_ice)
physical_animal_1.learnSpell(sp_weak_blast_ice)
physical_animal_1.learnSpell(sp_bolt)

# Print animals with spells using spell.Spell.__str__
print("Listing monsters...")
print("\n")
print(physical_animal_1.name)
print(physical_animal_1.name+ " has the following spells:")
for spell in physical_animal_1.spells:
    print(spell)
print("\n")
print(spell_animal_1.name)
print(spell_animal_1.name+ " has the following spells:")
for spell in spell_animal_1.spells:
    print(spell)
print("\n")

# Create two players
player1 = player.player(name="Player 1", player_type='player')
player2 = player.player(name="Player 2", player_type='player')

# Give each player a monster and print the return string from player.addMonster method
print(player1.addMonster(physical_animal_1))
print(player2.addMonster(spell_animal_1))



