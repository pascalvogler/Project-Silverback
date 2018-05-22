import player
import sys
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class fight:
    def __init__(self, player1, player2, locx, locy):
        self.player1 = player1
        self.player2 = player2
        self.player1.id = 1
        self.player2.id = -1
        self.locx = locx
        self.locy = locy
        self.current_turn = -1       # current_turn = 1 means player1's turn, -1 is player2 turn
        self.fight_state = 1        # fight_state = 1 means fight is active
        self.nextTurn()


    def nextTurn(self):
        self.current_turn*=-1
        if self.current_turn == 1:
            print("It's "+self.player1.name+"'s turn.") 
            self.runTurn(self.player1)
        else:
            print("It's "+self.player2.name+"'s turn.")
            self.runTurn(self.player2)

    def endFight(self):
        self.fight_state = 0

    def runTurn(self, player):
        self.drawBattle()
        selected_monster = self.selectMonster(player)
        selected_action = self.selectAction(selected_monster)
        selected_target = self.selectTarget(selected_action)
        monster_attack = self.monsterAttack(selected_monster, selected_target, selected_action)
        print(monster_attack['source'] + " uses " + monster_attack['action'] + " on " + monster_attack['target'])
        print(monster_attack['target'] + " is " + "critically " * monster_attack['is_crit'] + "hit for " + str(monster_attack['total_damage']))


    def drawBattle(self):
        print("Player 1: "+self.player1.name)
        print("\n")
        print("Monsters:")
        for monster in self.player1.monsters:
            print(monster.name + " Life: "+str(monster.current_life))
        print("\n")
        print("\n")
        print("Player 2: "+self.player2.name)
        print("\n")
        print("Monsters:")
        for monster in self.player2.monsters:
            print(monster.name + " Life: "+str(monster.current_life))
        print("\n")

    def selectMonster(self, player):
        print("Which monster do you want to use?")
        selector_counter = 1
        for monster in player.monsters:
            print(str(selector_counter) + ": "+monster.name)
            selector_counter+=1
        print("\n")
        selection = input("Choose Monster: ")
        selection = int(selection)
        if selection-1 <= len(player.monsters):
            return player.monsters[selection-1]

    def selectAction(self, selected_monster):
        print(selected_monster.name)
        print("\n")
        print("Actions: ")
        selector_counter = 1
        for action in selected_monster.actions:
            print(str(selector_counter) + ": "+action.name)
            selector_counter+=1
        print("\n")
        selection = input("Choose Action: ")
        selection = int(selection)
        if selection <= len(selected_monster.actions):
            return selected_monster.actions[selection-1]

    def selectTarget(self, action):
        if self.current_turn == 1:
            target_player = self.player2
        elif self.current_turn == -1:
            target_player = self.player1
        print("Which monster do you want to attack?")
        selector_counter = 1
        for monster in target_player.monsters:
            print(str(selector_counter) + ": "+monster.name)
            selector_counter+=1
        print("\n")
        selection = input("Select target: ")
        selection = int(selection)
        if selection-1 <= len(target_player.monsters):
            return target_player.monsters[selection-1]

    def monsterAttack(self, source, target, action):
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

        source.changeMana(-action.mana_cost)
        target.changeLife(-total_damage)

        result_dict = {'action': action.name, 'source': source.name, 'target': target.name, 'is_crit': is_crit, 'crit_damage': crit_damage, 'total_damage': total_damage}
        return result_dict

def startFight(player1, player2, locy, locx):
    this_fight = fight(player1, player2, locy, locx)
    this_fight.nextTurn()