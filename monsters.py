import spell

# Console colors used for __str__
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[90m'
    ENDC = '\033[0m'

class Basic_Form:
    life_multiplier = 15

    def xp_to_next_level(self, current_level):
        _xp_to_next_lvl = int(500*current_level**1.2)
        return _xp_to_next_lvl

    @property
    def xp_reward(self):
        return self.level*100

    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, level = 1, spells = []):
        self.name = name
        self.type = monster_type
        self.terrain = terrain
        self.lore = lore
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stamina = stamina
        self.spells = spells
        self.current_life = self.stamina * self.life_multiplier
        self.level = level
        self.xp =  0
    
    @property
    def max_life(self):
        new_life = self.stamina * self.life_multiplier
        return new_life  
    
    def changeLife(self, life_delta):
        self.current_life = self.current_life + life_delta
        if self.current_life < 0:
            self.current_life = 0
        return self.current_life

    def learnSpell(self, spell):
        self.spells.append(spell)

    def gainXp(self, exp):
        ''' adds xp to monster and triggers levelups
        Argument: 
        exp: Experience to add (int)
        Returns: None
        '''
        self.xp += exp
        print(self.name + " has gained "+ str(exp) + " Experience.")
        xp_to_next_lvl = self.xp_to_next_level(self.level)
        if(self.xp >= xp_to_next_lvl):
            _xp_remainder = self.xp - xp_to_next_lvl
            self.levelUp()
            self.gainXp(_xp_remainder)
        return True

    def levelUp(self):
        # TO DO
        self.level+=1
        self.xp = 0
        print(self.name+" has leveled up to level "+str(self.level))


    @property
    def is_alive(self):
        _is_alive = self.current_life>0
        return _is_alive

    @property
    def string_display(self):
        ''' displays monster name and life
        changes font to grey if monster is dead'''
        _string = self.name + " Life: " + str(self.current_life) + "/" + str(self.max_life)
        if(self.is_alive == False):
            _string = bcolors.GREY + _string + bcolors.ENDC
        return _string

    @property
    def string_display_name(self):
        _string = self.name
        if(self.is_alive == False):
            _string = bcolors.GREY + _string + bcolors.ENDC
        return _string
    

    
    
    
    
class Physical_Animal(Basic_Form):
    
    attack_power_multiplier = 2
    
    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, max_rage, wrath, level, spells = []):
        super().__init__(name, monster_type, terrain, lore, strength, agility, intelligence, stamina, level, spells = [])
        self.max_rage = max_rage
        self.wrath = wrath
        self.current_rage = 0

    def changeRage(self, rage_delta):
        self.current_rage = self.current_rage + rage_delta
        return self.current_rage
    
    @property
    def attack_power(self):
        ap = self.attack_power_multiplier * self.strength + self.attack_power_multiplier * self.agility
        return ap

    # actions property copies object's spells and adds the basic attack based on attack power.
    @property
    def actions(self):
        attack_damage = self.attack_power
        basic_attack = spell.Spell(name='Basic Attack', damage=attack_damage, mana_cost=0)
        all_actions = self.spells.copy()
        all_actions.insert(0, basic_attack)
        return all_actions
    


class Spell_Animal(Basic_Form):
    
    spell_power_multiplier = 2
    mana_multiplier = 10
    
    def __init__(self, name, monster_type, terrain, lore, strength, agility, intelligence, stamina, level, spells = []):
        super().__init__(name, monster_type, terrain, lore, strength, agility, intelligence, stamina, level, spells = [])
        self.current_mana = self.max_mana

    @property
    def max_mana(self):
        _max_mana = self.intelligence * self.mana_multiplier
        return _max_mana    

    def changeMana(self, mana_delta):
        self.current_mana = self.current_mana + mana_delta
        return self.current_mana
        
    @property
    def attack_power(self):
        ap = self.spell_power_multiplier * self.intelligence
        return ap

    # actions property copies object's spells and adds the basic attack based on attack power.
    @property
    def actions(self):
        attack_damage = self.attack_power
        basic_attack = spell.Spell(name='Basic Attack', damage=attack_damage, mana_cost=0)
        all_actions = self.spells.copy()
        all_actions.insert(0, basic_attack)
        return all_actions

    @property
    def string_display(self):
        ''' same as super class, but added mana display '''
        _string = self.name + " Life: " + str(self.current_life) + "/" + str(self.max_life) + " Mana: " + str(self.current_mana) + "/" + str(self.max_mana)
        if(self.is_alive == False):
            _string = bcolors.GREY + _string + bcolors.ENDC
        return _string
