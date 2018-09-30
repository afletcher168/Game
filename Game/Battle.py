'''
Created on Aug 12, 2018

@author: aflet
'''
from pip._vendor.distlib.compat import raw_input
import sys


class Battle(object):
    '''
    The class for the battle sequence.
    '''

    FRIEND_HEAL_PERCENT = 0.75
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def battle(self, game_turn, abilities, executes, dot_executes, player, enemies, friend_name):
        encounter_turn = 0
        enemies_left = dict(enemies)
        names_with_cd = dict(abilities.names)
        print("Enemies: %s" % (enemies_left))

        """Ability Choosing"""
        while True:
            game_turn += 1
            encounter_turn += 1
            print("Turn: %s" % encounter_turn)
            if encounter_turn % 5 == 0:
                player.heal(player.max_health*player.heal_after_battle_percent*self.FRIEND_HEAL_PERCENT)
                print("%s heals you for %.2f." % (friend_name, (player.heal_after_battle_percent*player.max_health*self.FRIEND_HEAL_PERCENT)))
            for i in names_with_cd:
                since_used = encounter_turn - (abilities.last_used[i] + 1)     ## +1 is to make the cooldown start the turn after ability is used.
                if since_used < abilities.cooldown[i]:
                    names_with_cd[i] = ("%s (%s)" % (abilities.names[i], abilities.cooldown[i] - since_used))
                else:
                    names_with_cd[i] = abilities.names[i]
            user_action = ""
            while user_action not in abilities.description:
                user_action = raw_input("Choose an ability: %s: " % (names_with_cd))
                if user_action.lower() == "quit" or user_action.lower() == 'q':
                    sys.exit()
                elif user_action.lower() == 's':
                    print(player)
                elif user_action.lower() == 'e':
                    print("Enemies: %s" % (enemies_left))
                elif user_action.lower() == 'd':
                    user_action = raw_input("Which ability? (1,2,.. or all): ")
                    if user_action.lower() == "quit" or user_action.lower() == 'q':
                        sys.exit()
                    elif user_action.lower() == 'all':
                        for element in range(1, len(abilities.description)+1):
                            print("%s: %s" % (element, abilities.description[str(element)]))
                    elif user_action.isnumeric() and int(user_action) > 0 and int(user_action) <= len(abilities.description):
                        print("%s: %s" % (user_action, abilities.description[user_action]))
                        user_action = ""
                    else:
                        print("Please input a valid number.")
                        user_action = ""
                elif user_action.lower() == 'k':
                    print("Type 'q' or 'quit' to quit.")
                    print("Type 's' to see stats.")
                    print("Type 'e' to see enemy information. (When choosing ability)")
                    print("Type 'd' to see ability descriptions.")
                    print("Type 'k' to see this menu again.")
                elif user_action not in abilities.description:
                    print("Please enter a valid input.")
            if abilities.is_on_cd(abilities.cooldown[user_action], abilities.last_used[user_action], encounter_turn):
                encounter_turn -= 1
                game_turn -= 1
                continue
            
            """Target Choosing"""
    
            target = ""
            while target not in enemies and target.lower() != 'c':
                target = raw_input("Choose a target: %s : " % (enemies_left))
                if target.lower() == "quit" or target.lower() == 'q':
                    sys.exit()
                elif target.lower() == 's':
                    print(player)
                elif target.lower() == 'k':
                    print("Type 'q' or 'quit' to quit.")
                    print("Type 's' to see stats.")
                    print("Type 'd' to see ability descriptions.")
                    print("Type 'k' to see this menu again.")
                    print("Type 'c' to cancel and re-pick ability. (When choosing target)")
                elif target.lower() == 'd':
                    target = raw_input("Which ability? (1,2,.. or all): ")
                    if target.lower() == "quit" or target.lower() == 'q':
                        sys.exit()
                    elif target.lower() == 'all':
                        for element in range(1, len(abilities.description)+1):
                            print("%s: %s" % (element, abilities.description[str(element)]))
                    elif target.isnumeric() and int(target) > 0 and int(target) <= len(abilities.description):
                        print("%s: %s" % (target, abilities.description[target]))
                        target = ""
                    else:
                        print("Please input a valid number.")
                        target = ""
                elif target not in enemies and target.lower() != 'c':
                    print("Please enter a valid input.")
            if target.lower() != 'c' and enemies[target].health <= 0:
                print("The target is dead. Choose another one.")
                encounter_turn -= 1
                game_turn -= 1
                continue
            if target.lower() == 'c':
                encounter_turn -= 1
                game_turn -= 1
                continue
    
            if user_action in abilities.is_aoe:
                for i in enemies_left:
                    if enemies_left[i].distance == enemies_left[target].distance:
                        if i == target:
                            enemies_left[i].take_damage(executes[user_action](player.level, player.strength) * 1.20, abilities.parry_resist)
                            if enemies_left[i].parry:
                                print("Enemy%s is parries your attack." % (i))
                            else:
                                print("You deal %.2f damage to target %s." % (enemies_left[i].damage_taken, i))
                        else:
                            enemies[i].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
                            if enemies_left[i].parry:
                                print("Enemy%s parries your attack." % (i))
                            else:
                                print("You deal %.2f damage to target %s." % (enemies_left[i].damage_taken, i))
                abilities.last_used[user_action] = encounter_turn
            else:
                enemies_left[target].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
                if enemies_left[target].parry:
                    print("Enemy%s parries your attack." % (target))
                elif abilities.damage != 0:
                    print("You deal %.2f damage to target %s." % (enemies_left[target].damage_taken, target))
                abilities.last_used[user_action] = encounter_turn
            for i in abilities.self_effect_duration:
                if abilities.is_active(abilities.self_effect_duration[i], abilities.last_used[i], encounter_turn):
                    player.incoming_damage_multiplier *= abilities.self_effect_value[i]
            if user_action in abilities.cd_reduction_abilities and enemies_left[target].parry != True:
                for i in abilities.cd_reduce_which[user_action]:
                    abilities.last_used[i] -= abilities.cd_reduction_abilities[user_action]
            if user_action in abilities.is_dot:
                enemies_left[target].active_dots[user_action] = abilities.dot_duration[user_action]
    
            for enemy in enemies:
                if enemy in enemies_left and enemies[enemy].health <= 0:
                    print("Enemy%s dies." % enemy)
                    del enemies_left[enemy]
        
            if len(enemies_left) == 0:
                break
            else:
                for enemy in enemies_left:
                    if enemies_left[enemy].ability != "" and not abilities.enemy_is_on_cd(abilities.cooldown[enemies_left[enemy].ability], abilities.last_used[enemies_left[enemy].ability], encounter_turn):
                        if enemies_left[enemy].is_casting == -1:     ##To start cast
                            print("Enemy%s is preparing to attack." % (enemy))
                            enemies_left[enemy].is_casting = abilities.cast_time[enemies_left[enemy].ability]
                            enemies_left[enemy].is_casting -= 1
                        elif enemies_left[enemy].is_casting > 0:     ##During cast
                            print("Enemy%s is preparing to attack." % (enemy))
                            enemies_left[enemy].is_casting -= 1
                        else:     ##Finish cast
                            player.take_damage(executes[enemies_left[enemy].ability](enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
                            print("You take %.2f damage from Enemy%s." % (player.damage_taken, enemy))
                            enemies_left[enemy].is_casting = -1     ##Reset
                            abilities.last_used[enemies_left[enemy].ability] = encounter_turn
                    elif enemies_left[enemy].distance == "melee":
                        player.take_damage(abilities.melee(enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
                        if player.parry:
                            print("You parry Enemy%s's attack." % (enemy))
                        elif abilities.damage != 0:
                            print("You take %.2f damage from Enemy%s." % (player.damage_taken, enemy))
                    elif enemies_left[enemy].distance == "ranged":
                        player.take_damage(abilities.shoot(enemies_left[enemy].level, enemies_left[enemy].strength, enemies_left[enemy].accuracy), abilities.parry_resist)
                        if abilities.damage == 0:
                            print("Enemy%s misses." % (enemy))
                        elif abilities.damage != 0:
                            print("You take %.2f damage from Enemy%s." % (player.damage_taken, enemy))
    
            if player.health <= 0:
                print("You died. rip.")
                sys.exit()
            else:
                print("Your current health is: %.2f." % (player.health))
        
            player.incoming_damage_multiplier = 1
    
            for enemy in enemies:
                if enemy in enemies_left:
                    for i in enemies[enemy].active_dots:
                        enemies_left[enemy].take_damage(dot_executes[i](player.level, player.strength), abilities.parry_resist)
                        print("Enemy%s takes %.2f damage from %s dot." % (enemy, enemies_left[enemy].damage_taken, abilities.names[i]))
                        enemies_left[enemy].active_dots[i] -= 1
                    if enemies[enemy].health <= 0:
                        print("Enemy%s dies." % enemy)
                        del enemies_left[enemy]
        
            for enemy in enemies_left:    
                for i in abilities.is_dot:
                    if i in enemies_left[enemy].active_dots and enemies_left[enemy].active_dots[i] == 0:
                        del enemies_left[enemy].active_dots[i]
    
            if len(enemies_left) == 0:
                break
       
        print("grats. You beat the level.")
        """Reset after battle"""
        player.heal(player.max_health*player.heal_after_battle_percent)
        for key in abilities.last_used:
            abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.