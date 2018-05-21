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
        self.life_delta = life_delta
        self.current_life = self.current_life + self.life_delta
        return self.current_life
    
    
class Physical_Animal(Basic_Form):
    
    attack_power_multiplicator = 10
    
    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, max_rage, wrath, spell = []):
        super().__init__(name, monster_type, terrain, lore, strength, agility, intelligence, stamina, spell = [])
        self.max_rage = max_rage
        self.wrath = wrath
        self.current_rage = self.max_rage

    def current_rage(self, rage_delta):
        self.rage_delta = rage_delta
        self.current_rage = self.current_rage + self.rage_delta
        return self.current_rage
    
    def attack_power_physical(self):
        self.attack_power = self.attack_power_multiplicator * self.strength + self.attack_power_multiplicator * self.dexterity
        return self.attack_power


class Spell_Animal(Basic_Form):
    
    spell_power_multiplicator = 20
    
    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, max_mana, mana_regen, spell = []):
        super().__init__(name, monster_type, terrain, lore, strength, agility, intelligence, stamina, spell = [])
        self.max_mana = max_mana
        self.mana_regen = mana_regen
        self.current_mana = self.max_mana
        
        def current_mana(self, mana_delta):
            self.mana_delta = mana_delta
            self.current_mana = self.current_mana + self.mana_delta
            return self.current_mana
        
        def attack_power_spell(self):
            self.attack_power = self.spell_power_multiplicator * self.intelligence
            return self.attack_power


physical_1 = Physical_Animal("Silverback", "Mammal", "Forest", "Aber so was vomene krasse Schlaeger", 80, 40, 30, 80, 100, 20, "1")

print(physical_1.current_life)
print(physical_1.max_life)

physical_1.stamina += 1

print(physical_1.max_life)
print(physical_1.current_life)
