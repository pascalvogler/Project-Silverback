import spell
import time
from random import randint

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
    def xp_to_next_level(self):
        _xp_to_next_lvl = int(500*self.level**1.2)
        return _xp_to_next_lvl

    @property
    def max_life(self):
        new_life = self.stamina * self.life_multiplier
        return new_life  

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

    def receiveDamage(self, damage, damage_source):
        ''' monster receives damage and gices xp to damage_source if it dies
        Arguments:
        damage (int): Amount of damage dealt
        damage_source (monster object): who's dealing the damage
        '''
        self.current_life-=damage
        if self.current_life < 0:
            self.current_life = 0
        if self.is_alive == False:
            print(printMonsterName(self) + " was killed.")
            time.sleep(1)
            damage_source.gainXp(self.xp_reward)

    def heal(self, amount):
        self.current_life += amount
        if self.current_life > self.max_life:
            self.current_life = self.max_life

    def learnSpell(self, spell):
        self.spells.append(spell)

    def gainXp(self, exp):
        ''' adds xp to monster and triggers levelups
        Argument: 
        exp: Experience to add (int)
        Returns: None
        '''
        def addXp(_xp):
            self.xp += _xp
            xp_to_next_lvl = self.xp_to_next_level
            if(self.xp >= xp_to_next_lvl):
                _xp_remainder = self.xp - xp_to_next_lvl
                self.levelUp()
                addXp(_xp_remainder)

        print(self.name + " has gained "+ str(exp) + " Experience.")
        time.sleep(1)
        addXp(exp)

    def levelUp(self):
        self.level += 1
        self.stamina = int(self.stamina*1.2)
        self.strength = int(self.strength*1.2)
        self.intelligence = int(self.intelligence*1.2)
        self.agility = int(self.agility*1.2)
        self.current_life = self.max_life
        self.current_mana = self.max_mana
        self.xp = 0
        print(self.name+" has leveled up to level "+str(self.level))
        time.sleep(1)
    
    def useAction(self, target, action):
        '''Takes: monster objects for source and target
        spell object for action
        Returns: dict of the attack results'''
        action_name = action.name
        action_damage = action.damage
        action_effect = action.effect
        action_mana_cost = action.mana_cost
        action_element = action.element
        action_crit = action.crit
        # is attack a crit? 
        is_crit = action.crit >= randint(0,100)/100
        # crit damage = currently 50% of normal damage
        crit_modifier = 0.5
        crit_damage = int(action.damage * crit_modifier)
        # if bool is_crit = False, is_crit * crit_damage = 0
        total_damage = action.damage + is_crit * crit_damage

        self.changeMana(-action.mana_cost)
        
        # create dict of attack results and print using printAttackResults()
        result_dict = {'action': action, 'source': self, 'target': target, 'is_crit': is_crit, 'crit_damage': crit_damage, 'total_damage': total_damage}
        printAttackResults(result_dict)
        target.receiveDamage(total_damage, self)
    
    
    
    
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

def printAttackResults(attack_results):
    ''' takes an attack_results dict, which is obtained from monsterAttack()
    prints the results of an attack'''
    monster_attack = attack_results
    # create colored strings of some attack results properties
    attack_source_str = printMonsterName(monster_attack['source'])
    attack_target_str = printMonsterName(monster_attack['target'])
    action_str = printActionName(monster_attack['action'])
    # print action
    print(attack_source_str + " uses " + action_str + " on " + attack_target_str)
    # print damage done
    print(attack_target_str + " is " + "critically " * monster_attack['is_crit'] + "hit for " + str(monster_attack['total_damage']))
    time.sleep(1)

def printMonsterName(monster):
    return bcolors.YELLOW+monster.name+bcolors.ENDC

def printActionName(action):
    return bcolors.RED+action.name+bcolors.ENDC
