def runFightTurn(bot, enemy_player):
    # Call selectMonster, using the bot as an argument, so AI can choose monster from bot's monster array
    # Store the chosen monster in selected_monster
    selected_monster = selectMonster(bot)
    # Call selectAction, using the selected_monster as an argument, to have bot decide which action it should use
    selected_action = selectAction(selected_monster)
    # Call selectTarget, giving the bot player as the player that it's fighting against
    selected_target = selectTarget(enemy_player)
    # Use the three objects to execute the attack, using monster's useAction method
    selected_monster.useAction(selected_target, selected_action)

def selectMonster(bot):
    ''' 
    Bot selects a monster to use 
    Arguments:
    bot (player object)
    Returns:
    (monster object)
    '''
    # select the first monster that has enough mana to use a spell
    for monster in bot.monsters:
        if monster.is_alive == True:
            this_monster = monster
            for spell in this_monster.spells:
                if(this_monster.current_mana >= spell.mana_cost):
                    return this_monster
    # if no monster has enough mana to cast a spell, use monster with highest attack damage
    highest_damage_monster = bot.monsters[0]
    for monster in bot.monsters:
        if monster.is_alive == True:
            this_monster = monster
            if this_monster.actions[0].damage > highest_damage_monster.actions[0].damage:
                highest_damage_monster = this_monster

    return highest_damage_monster

def selectAction(selected_monster):
    ''' 
    Bot selects action to use. Selects first spell that can be used, otherwise uses basic attack 
    Args:
    selected_monster (monster object)
    Returns:
    (action object)
    '''
    this_monster = selected_monster
    for spell in this_monster.spells:
        if(this_monster.current_mana >= spell.mana_cost):
            return spell
    # if no spell can be used, use basic attack
    return this_monster.actions[0]

def selectTarget(enemy_player):
    '''
    Selects a target for an attack. Chooses the monster of a player that has the lowest hp
    Args:
    enemy_player (player object)
    Returns:
    (monster object)
    '''
    enemy_alive_monsters = []
    for monster in enemy_player.monsters:
        if monster.is_alive==True:
            enemy_alive_monsters.append(monster)
    lowest_hp_monster = enemy_alive_monsters[0]
    for monster in enemy_alive_monsters:
        this_monster = monster
        if this_monster.current_life < lowest_hp_monster.current_life:
            lowest_hp_monster = this_monster
    return lowest_hp_monster