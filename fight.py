import player
import sys
from random import randint
import time

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class fight:
    def __init__(self, player1, player2, locx, locy):
        self.player1 = player1
        self.player2 = player2
        self.player2_defeated = False
        self.player1.id = 1
        self.player2.id = -1
        self.locx = locx            # NOT USED YET: coordinates for where the fight takes place
        self.locy = locy
        self.current_turn = 1       # current_turn = 1 means player1's turn, -1 is player2 turn
        self.current_turn_player = self.player1
        self.fight_state = 1        # fight_state = 1 means fight is active
        self.mainFight()

    def mainFight(self):
        ''' Main fight loop. 
        Checks if any player has zero monsters left
        If so, calls endFight()
        Else, calls nextTurn() 
        NOTE: fight_state is not used? '''
        while self.fight_state == 1:
            self.player1_num_alive_monsters = 0
            self.player2_num_alive_monsters = 0
            for monster in self.player1.monsters:
                if monster.is_alive == True:
                    self.player1_num_alive_monsters+=1
            for monster in self.player2.monsters:
                if monster.is_alive == True:
                    self.player2_num_alive_monsters+=1
            if(self.player1_num_alive_monsters == 0):
                self.endFight(winner=self.player2)
                break
            elif(self.player2_num_alive_monsters == 0):
                self.endFight(winner=self.player1)
                break
            else:
                self.nextTurn()


    # COLOR FUNCTIONS
    # These functions add console color codes to the .name props and returns them

    def printPlayerName(self, player):
        return bcolors.BLUE+player.name+bcolors.ENDC

    def printMonsterName(self, monster):
        return bcolors.YELLOW+monster.name+bcolors.ENDC

    def printActionName(self, action):
        return bcolors.RED+action.name+bcolors.ENDC

    def printAttackResults(self, attack_results):
        ''' takes an attack_results dict, which is obtained from monsterAttack()
        prints the results of an attack'''
        monster_attack = attack_results
        # create colored strings of some attack results properties
        attack_source_str = self.printMonsterName(monster_attack['source'])
        attack_target_str = self.printMonsterName(monster_attack['target'])
        action_str = self.printActionName(monster_attack['action'])
        # print action
        print(attack_source_str + " uses " + action_str + " on " + attack_target_str)
        # print damage done
        print(attack_target_str + " is " + "critically " * monster_attack['is_crit'] + "hit for " + str(monster_attack['total_damage']))
        # print if a monster was killed
        if monster_attack['target'].is_alive == False:
            print(attack_target_str + " was killed.")

    def nextTurn(self):
        ''' Starts a turn, called from the mainFight loop.'''
        # print whose turn it is
        print("It's "+self.printPlayerName(self.current_turn_player)+"'s turn.")
        print("\n")
        time.sleep(1)
        # call runTurn()
        self.runTurn(self.current_turn_player)
        # after Turn is run, switch whose turn it is
        self.current_turn*=-1
        if self.current_turn == 1:
            self.current_turn_player = self.player1
        else:
            self.current_turn_player = self.player2

    def endFight(self, winner):
        self.fight_state = 0
        print(winner.name + " wins the match")

    def runTurn(self, player):
        ''' takes player object as an argument, to know which player's turn it is'''
        # call drawBattle function to show the current status with players and monsters
        self.drawBattle()
        # Call selectMonster, using the current_player as an argument, to prompt user for input
        # Store the chosen monster in selected_monster
        selected_monster = self.selectMonster(player)
        # Call selectAction, using the selected_monster as an argument, to prompt user for input
        # Store the chosen action in selected_action
        selected_action = self.selectAction(selected_monster)
        # Call selectTarget, using the selected_action as an argument, to prompt user for input
        # Store the chosen target in selected_target
        selected_target = self.selectTarget(selected_action)
        # Use the three objects to execute the attack, using monsterAttack() function
        # Store the attack results dict in monster_attack
        monster_attack = self.monsterAttack(selected_monster, selected_target, selected_action)
        # Print the attack results using printAttackResults function
        self.printAttackResults(monster_attack)
        time.sleep(1)

    def drawBattle(self):
        ''' Draws the current state of the battle
        showing the two players, and the monsters with their lives using
        the new string_display property of the monster class '''
        print("Player 1: "+self.player1.name)
        print("Monsters:")
        for monster in self.player1.monsters:
            print(monster.string_display)
        print("\n")
        print("Player 2: "+self.player2.name)
        print("Monsters:")
        for monster in self.player2.monsters:
            print(monster.string_display)
        print("\n")
        time.sleep(1)

    def selectMonster(self, player):
        ''' Asks a player for input to select the monster to use in this turn
        Returns the chosen monster as a monster object
        '''
        print("Which monster do you want to use?")
        # List available monsters and print them
        selector_counter = 1
        for monster in player.monsters:
            print(str(selector_counter) + ": "+monster.string_display)
            selector_counter+=1

        while True:
            # Ask user for input
            selection = input("Choose Monster: ")
            # User input is string, so has to be converted to int
            # TODO: Catch error if int conversion fails! (handle incorrect input)
            # if selection-1 <= len(player.monsters):
            selection = int(selection)
            # If that monster is alive, return the monster (breaks while loop)
            # selection-1 because arrays start at zero
            if player.monsters[selection-1].is_alive:
                return player.monsters[selection-1]
            #If monster is dead, print error and start at beginning of while loop
            else:
                print("That monster is dead")

    def selectAction(self, selected_monster):
        ''' prompts user for input to select what action to take
        Argument: selected_monster (obj Monster) -> which monster's actions to list
        returns: Action selected'''
        print(selected_monster.name)
        print("\n")
        print("Actions: ")
        # List this monster's available actions using Spell.string_display property
        selector_counter = 1
        for action in selected_monster.actions:
            print(str(selector_counter) + ": "+action.string_display)
            selector_counter+=1
        print("\n")
        # Ask user for input
        # TO DO: Handle incorrect input, same as selectMonster!
        # TO DO: Currently only works with MANA, not rage!
        while True:
            selection = input("Choose Action: ")
            selection = int(selection)
            # If mana cost lower or equal to monster's current mana, return action
            if selected_monster.actions[selection-1].mana_cost <= selected_monster.current_mana:
                return selected_monster.actions[selection-1]
            # else print warning and back to start of while loop
            else: 
                print("Not enough mana")


    def selectTarget(self, action):
        if self.current_turn == 1:
            target_player = self.player2
        elif self.current_turn == -1:
            target_player = self.player1
        print("Which monster do you want to attack?")
        selector_counter = 1
        for monster in target_player.monsters:
            print(str(selector_counter) + ": "+monster.string_display)
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

        #if target dead do whatever

        result_dict = {'action': action, 'source': source, 'target': target, 'is_crit': is_crit, 'crit_damage': crit_damage, 'total_damage': total_damage}
        return result_dict

def startFight(player1, player2, locy, locx):
    this_fight = fight(player1, player2, locy, locx)