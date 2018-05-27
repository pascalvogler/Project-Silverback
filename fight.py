import sys
from random import randint
import time
import overworld
import bot

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
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player2_defeated = False
        self.player1.id = 0
        self.player2.id = 1
        self.current_turn = 1
        self.winner = None
        self.loser = None
        self.current_turn_player = self.player1
        self.fight_state = 1        # fight_state = 1 means fight is active
        self.mainFight()

    def mainFight(self):
        ''' Main fight loop. 
        Checks if any player has zero monsters left
        If so, calls endFight()
        Else, calls nextTurn() 
        NOTE: fight_state is not used? '''
        print(bcolors.RED+"Fight starts: "+self.player1.name+" vs "+self.player2.name+bcolors.ENDC)
        while self.fight_state == 1:
            # check if any player has no monsters left
            if self.player1.is_defeated == True:
              self.winner = self.player2
              self.loser = self.player1
              self.endFight(winner=self.winner, loser=self.loser)
              break
            elif self.player2.is_defeated == True:
              self.winner = self.player1
              self.loser = self.player2
              self.endFight()
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

    def colorString(self, string, color):
        ''' Args:
        string: str
        color: color from bcolors class
        Returns:
        string in selected color '''
        result = color+string+bcolors.ENDC
        return result

    def nextTurn(self):
        ''' Starts a turn, called from the mainFight loop.'''
        # print whose turn it is
        print("It's "+self.printPlayerName(self.current_turn_player)+"'s turn.")
        print("\n")
        time.sleep(1)
        self.drawBattle()
        # call runTurn()
        self.runTurn(self.current_turn_player)
        # after Turn is run, switch whose turn it is
        self.current_turn+=1
        if self.current_turn%2 == 1:
            self.current_turn_player = self.player1
        else:
            self.current_turn_player = self.player2

    def endFight(self):
        self.fight_state = 0
        overworld.despawnPlayer(self.loser)
        self.winner.regenerateMonsters()
        print(self.printPlayerName(self.winner) + " wins the match")

    def runTurn(self, player):
        ''' takes player object as an argument, to know which player's turn it is'''
        # call drawBattle function to show the current status with players and monsters
        if player.player_type == 'player':
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
            selected_monster.useAction(selected_target, selected_action)
        elif player.player_type == 'bot':
            if self.current_turn%2 == 1:
                target_player = self.player2
            elif self.current_turn%2 == 0:
                target_player = self.player1
            bot.runFightTurn(player, target_player)
            # basically do the same as with player, but select automatically


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
            print(str(selector_counter) + ": "+monster.string_display_name)
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
        print(self.printMonsterName(selected_monster))
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
        if self.current_turn%2 == 1:
            target_player = self.player2
        elif self.current_turn%2 == 0:
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

def startFight(player1, player2):
    this_fight = fight(player1, player2)
    return this_fight.winner