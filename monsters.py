

class Basic_Form:
    life_multiplicator = 15

    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, spell = []):
        self.name = name
        self.type = monster_type
        self.terrain = terrain
        self.lore = lore
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stamina = stamina
        self.spell = spell
        #self.max_life = self.stamina * self.life_multiplicator
        self.current_life = self.stamina * self.life_multiplicator

    @property
    def max_life(self):
        new_life = self.stamina * self.life_multiplicator
        return new_life
    
    def changeLife(self, life_delta):
        self.current_life = self.current_life + life_delta
        return self.current_life
    
    
class Physical_Animal(Basic_Form):
    
    attack_power_multiplicator = 10
    
    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, max_rage, wrath, spell = []):
        super().__init__(name, monster_type, terrain, lore, strength, agility, intelligence, stamina, spell = [])
        self.max_rage = max_rage
        self.wrath = wrath
        self.current_rage = 0

    def changeRage(self, rage_delta):
        self.current_rage = self.current_rage + rage_delta
        return self.current_rage
    
    @property
    def attack_power(self):
        ap = self.attack_power_multiplicator * self.strength + self.attack_power_multiplicator * self.agility
        return ap


class Spell_Animal(Basic_Form):
    
    spell_power_multiplicator = 20
    
    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, max_mana, mana_regen, spell = []):
        super().__init__(name, monster_type, terrain, lore, strength, agility, intelligence, stamina, spell = [])
        self.max_mana = max_mana
        self.mana_regen = mana_regen
        self.current_mana = self.max_mana
        
    def changeMana(self, mana_delta):
        self.current_mana = self.current_mana + mana_delta
        return self.current_mana
        
    @property
    def attack_power(self):
        ap = self.spell_power_multiplicator * self.intelligence
        return ap


#TESTS 

physical_1 = Physical_Animal("Silverback", "Mammal", "Forest", "Aber so was vomene krasse Schlaeger", 80, 40, 30, 80, 100, 20, "1")
spell_1 = Spell_Animal("Silverback_Spell", "Mammal", "Forest", "Aber so was vomene krasse Schlaeger", 80, 40, 30, 80, 500, 20, "1")

print(spell_1.current_mana)
print(spell_1.changeMana(-100))