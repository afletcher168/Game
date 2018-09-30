'''
Created on Jul 4, 2018

@author: Andrew Fletcher

This project/game is meant to serve as a 
personal project in order to test/use/learn skills
in python. 

The current idea is to make a game that simulates 
turn-based combat drawing from World of Warcraft
combat concepts.
'''
import sys

from time import sleep
from pip._vendor.distlib.compat import raw_input

from Character import Player, Enemy
from Abilities import Abilities
from Battle import Battle

TINY_PAUSE_IN_SECONDS = 1
SMALL_PAUSE_IN_SECONDS =  3


"""The intro to the game. First interaction with user."""
game_name = "TBD"

print("Welcome! You are now playing %s. Are you ready to go on an adventure??!?!?!" % game_name)
while True:
    user_action = raw_input("Type 'y' or 'yes' to continue, type 'n', 'no', or 'quit' to quit: ")
    if user_action.lower() == "n" or user_action.lower() == "no" or user_action.lower() == "quit":
        print("Well, screw you then. Bye-bye")
        sys.exit()
    elif user_action.lower() == "y" or user_action.lower() == "yes":
        print ("Coolio. Let's get started then.")
        break
    else:
        print("That's not one of the options, Mr.(or Ms. IDK) smartypants")
user_name = raw_input("What will your name in this game be? ")
print("Excellent choice! Although to be honest, there wasn't a bad choice.")
print("Please note that if you wish to quit at any time, just type: 'quit' or 'q' any time you are prompted, and hit enter.")
wait = raw_input("Press enter to continue.")
sleep(TINY_PAUSE_IN_SECONDS)
"""The start of the game!"""

"""Commenting out for now because story is mostly print statements.  I want to get into the main purpose of the game.

print("------------------------------------------------------------------------------------------------------------------------------")
print("You wake up. You feel a a slight, but chilling breeze on your face.")
print("You feel the warmth of a warm bed and heavy blankets surrounding your body. You don't want to move, but feel that you should.")
counter = 0
while True:
    print("You start to get out of bed, but feel really tired.")
    if counter == 0:
        choice = raw_input("Type: 'wake up' to wake up, otherwise you will fall back asleep: ")
    if counter > 0:
        choice = raw_input(":")
    if choice.lower() == "wake up":
        print("You try your best to shake the drowsiness off, run your blurry eyes, then take in the rest of your surroundings.")
        break
    elif choice.lower() == "quit":
        print("That's unfortunate.")
        sys.exit()
    elif choice.lower() != "wake up" and counter == 3:
        print("There's a loud bang as someone bursts into the room. Alarmed, you face the origin of the sound.")
        sleep(3)
        print("oh, it's your dad.")
        print("'Get up, it's almost sunrise,' he said, gruffly.")
        print("Feeling chastised, you get up. This is not how you wanted to start your day.")
        break
    else:
        print("You succumb to your desires and fall back asleep...")
        counter += 1
        sleep(5)
    
print("You are sitting in your bedroom. You realize you left the window open. No wonder it's freezing.")
print("You go to close the window.")
raw_input("(Press Enter):")
print("As you walk up to the window, you look outside.")
print("You see a few people out and about, but most of the village still sleeps.")
raw_input("(Press Enter):")
print("You go to the common room to get breakfast.")
print("You help yourself to the food in the closet.")
print("You try to eat as much as you can. You have a feeling this is going to a long day.")
raw_input("(Press Enter):")
print("Your dad reappears in the doorway.")
print("  'Hurry up. You don't have all day.'")
raw_input("(Press Enter):")
print("Outside, you see Andrew, your best friend, waiting for you.")
print("  'Wassuuup, my duuude!?'")
print("You remember how annoying he is.")
print("  'Are you ready for a fun-filled day of endless walking?'")
print("You gaze across the field, at the endless mass of trees and shrubbery.")
raw_input("  You: ")
print("  'I know. I can't wait...'")
print("Together, you head to forest.")
raw_input("(Press Enter):")
print("                           ---")
print("  'When I die, I want you to plant a tree on my grave, and burn it.'")
sleep(1)
print("Andrew didn't really appreciate the forest. He always liked to compare the tree trunks to the bars of a prison.")
print("The village, built in a valley, is wedged between mountains on one side, and a wide, dense forest on the other.")
print("As a result, the village was effectively cut off from the rest of civilization.")
print("  'Let's take a break, my feet are killing me.'")
raw_input("(Press Enter):")
print("You guys had just spent at least half a day stumbling through the forest, emptying traps and resetting them.")
print("  'We already filled up one pack, and now we're outta food for us to eat. I'm gonna head back, drop this off, and grab some more food. Stay here and take a break.'")
print("You decide to take a nap while you wait...'")
raw_input("(Press Enter):")
"""

"""Player Construction"""
player = Player(1)
abilities = Abilities()
print(player)
executes = {'1':abilities.melee, '-1':abilities.roundhouse_strike, '-2':abilities.final_smash}
dot_executes = {}
battle = Battle()

game_turn = 0

"""Testing"""


"""Encounter 1"""
print("You encounter your first enemy.")
enemy1 = Enemy(1, 'melee', False, "", "")
enemies = {'1':enemy1}
print("Enemies: %s" % (enemies))
encounter_turn = 0
print("To perform actions during a fight, type out an option from the menu or one of the universal commands.")
print("The universal commands are 'q' or 'quit' for quit, 's' for stats, 'd' for description, and 'k' to see this key again.")

"""Encounter 1 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("type '1' to melee (and press enter): ")
        if user_action.lower() == "quit" or user_action.lower() == 'q':
            sys.exit()
        elif user_action.lower() == 's':
            print(player)
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
                print("Please input a valid input.")
        elif user_action.lower() == 'k':
            print("Type 'q' or 'quit' to quit.")
            print("Type 's' to see stats.")
            print("Type 'd' to see ability descriptions.")
            print("Type 'k' to see this menu again.")
        elif user_action not in abilities.description:
            print("Please enter a valid input.")
    
    """Encounter 1 Target Choosing"""        
    print("Note: you are about to be asked to select a target enemy. Each enemy is given a number, starting from one, and has a certain level, health, and strength.")
    print("each enemy will be denoted in the format: 'enemy Number-(level/current Health/strength)'")
    target = ""
    while target != '1' and target.lower() != 'c':
        target = raw_input("Choose a target: 1-(%s/%.2f/%s) Note: type 1 to select target number 1: " % (enemy1.level, enemy1.health, enemy1.strength))
        if target.lower() == "quit" or target.lower() == 'q':
            sys.exit()
        elif target.lower() == 's':
            print(player)
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
        elif target.lower() == 'k':
            print("Type 'q' or 'quit' to quit.")
            print("Type 's' to see stats.")
            print("Type 'd' to see ability descriptions.")
            print("Type 'k' to see this menu again.")
            print("Type 'c' to cancel and re-pick ability.")
        elif target != '1' and target.lower() != 'c':
            print("Please enter a valid input.")
    if target.lower() == 'c':
        encounter_turn -= 1
        game_turn -= 1
        continue
    enemies[target].take_damage(abilities.melee(player.level, player.strength), abilities.parry_resist)
    print("You deal %.2f damage to target %s." % (abilities.damage, target))
    if enemy1.health <= 0:
        break
    else:
        player.take_damage(abilities.melee(enemy1.level, enemy1.strength), abilities.parry_resist)
        print("You take %.2f damage from Enemy1." % abilities.damage)
    
    if player.health <= 0:
        print("You died. rip.")
        sys.exit()

print("Congrats!! you beat the first enemy.")

wait = raw_input("Press enter to continue.")

"""Encounter 2"""
print("You are ambushed by two enemies this time.")
enemy1 = Enemy(1, 'melee', False, "", "")
enemy2 = Enemy(1, 'melee', False, "", "")
enemies = {'1':enemy1, '2':enemy2}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0
print("The universal commands are 'q' or 'quit' for quit, 's' for stats, 'd' for description, and 'k' to see this key again.")

"""Encounter 2 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("type '1' to melee (and press enter): ")
        if user_action.lower() == "quit" or user_action.lower() == 'q':
            sys.exit()
        elif user_action.lower() == 's':
            print(player)
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
            print("Type 'd' to see ability descriptions.")
            print("Type 'k' to see this menu again.")
        elif user_action not in abilities.description:
            print("Please enter a valid input.")
            
    """Encounter 2 Target Choosing"""
    print("Note: you are about to be asked to select a target enemy. Each enemy is given a number, starting from one, and has a certain level, health, and strength.")
    print("each enemy will be denoted in the format: 'enemy Number-(level/current Health/strength)'")
    target = ""
    while target not in enemies and target.lower() != 'c':
        target = raw_input("Choose a target: %s Note: type 1 to select enemy 1 or type 2 to select enemy 2: " % (enemies_left))
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
    enemies[target].take_damage(abilities.melee(player.level, player.strength), abilities.parry_resist)
    print("You deal %.2f damage to target %s." % (abilities.damage, target))

    for enemy in enemies:
        if enemy in enemies_left and enemies[enemy].health <= 0:
            print("Enemy%s dies." % enemy)
            del enemies_left[enemy]
        
    if enemy1.health <= 0 and enemy2.health <= 0:
        break
    else:
        for enemy in enemies_left:
            player.take_damage(abilities.melee(enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
            print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
    
    if player.health <= 0:
        print("You died. rip.")
        sys.exit()
       
print("Congrats!! You beat the heck out of both of them.")
sleep(TINY_PAUSE_IN_SECONDS)

"""Level 2"""
print("Nice! You just leveled up!")
player.level_up()
print(player)
print("Normally, at the end of each fight, you will heal 25% of your max health...")
print("When you level up however, you will be fully healed.")
sleep(SMALL_PAUSE_IN_SECONDS)
print("Also, you just gained a new ability!")
abilities.names['2'] = "Heavy Strike"
abilities.description['2'] = "Heavy Strike: A heavy strike that deals significant damage, but has a cooldown. (3 turns)"
executes['2'] = abilities.heavy_strike
print(abilities.description['2'])

wait = raw_input("Press enter to continue.")

"""Encounter 3"""
print("You are somehow ambushed by another two enemies this time.")
enemy1 = Enemy(1, 'melee', False, "", "")
enemy2 = Enemy(2, 'melee', False, "", "")
enemies = {'1':enemy1, '2':enemy2}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0
print("You though, now have a stronger move in your arsenal.")
print("Also, when choosing an ability, you may now type 'e' to show enemy information.")

"""Encounter 3 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 3 Target Choosing"""
    
    print("PLease note that the enemies are getting stronger too. Here, Enemy 2 is stronger.")
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
    
    
    enemies[target].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
    print("You deal %.2f damage to target %s." % (abilities.damage, target))
    abilities.last_used[user_action] = encounter_turn

    for enemy in enemies:
        if enemy in enemies_left and enemies[enemy].health <= 0:
            print("Enemy%s dies." % enemy)
            del enemies_left[enemy]
        
    if len(enemies_left) == 0:
        break
    else:
        for enemy in enemies_left:
            player.take_damage(abilities.melee(enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
            print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
    
    if player.health <= 0:
        print("You died. rip.")
        sys.exit()
       
print("Congrats!! You have exposed your enemies for the wimps that they are.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)

sleep(TINY_PAUSE_IN_SECONDS)
"""Level 3"""
print("Nice! You level up again!")
player.level_up()
print(player)
sleep(TINY_PAUSE_IN_SECONDS)
print("You gain a new ability!")
abilities.names['3'] = "Sweeping Strike"
abilities.description['3'] = "Sweeping Strike: A wide, sweeping attack that deals weaker damage to all enemies, but deals 20% more damage to the primary target. (1 turn)"
executes['3'] = abilities.sweeping_strike
print(abilities.description['3'])

print("...")
wait = raw_input("Press enter to continue.")

"""Encounter 4"""
print("Wow. You're not very good at this. You are, again, somehow ambushed. This time by 3 enemies.")
enemy1 = Enemy(2, 'melee', False, "", "")
enemy2 = Enemy(2, 'melee', False, "", "")
enemy3 = Enemy(1, 'melee', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0
print("You should make use of your newfound ability.")

"""Encounter 4 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 4 Target Choosing"""
    
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
                    enemies[i].take_damage(executes[user_action](player.level, player.strength) * 1.20, abilities.parry_resist)
                    print("You deal %.2f damage to target %s." % (abilities.primary_damage, i))
                else:
                    enemies[i].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
                    print("You deal %.2f damage to target %s." % (abilities.damage, i))
        abilities.last_used[user_action] = encounter_turn
    else:
        enemies[target].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
        print("You deal %.2f damage to target %s." % (abilities.damage, target))
        abilities.last_used[user_action] = encounter_turn

    for enemy in enemies:
        if enemy in enemies_left and enemies[enemy].health <= 0:
            print("Enemy%s dies." % enemy)
            del enemies_left[enemy]
        
    if len(enemies_left) == 0:
        break
    else:
        for enemy in enemies_left:
            player.take_damage(abilities.melee(enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
            print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
    
    if player.health <= 0:
        print("You died. rip.")
        sys.exit()
       
print("Congrats!! You have rid their pitiful existence of...well, existence.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)


print("...")
wait = raw_input("Press enter to continue.")

"""Encounter 5"""
print("I don't even understand how it's possible. You are, again, somehow ambushed.")
print("This time, they brought a ranged archer.")
print("When targeting a melee enemy with an AOE ability, it will hit all melee enemies, but miss ranged enemies.")
print("Conversely, when targeting a ranged enemy with an AOE ability, it will hit all ranged enemies, but miss melee enemies.")
print("Additionally, ranged units have a chance that they will miss any given shot. However, they deal more damage with each shot, and their accuracy increases with level.")
enemy1 = Enemy(2, 'melee', False, "", "")
enemy2 = Enemy(1, 'melee', False, "", "")
enemy3 = Enemy(1, 'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0

"""Encounter 5 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 5 Target Choosing"""
    
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
                    enemies[i].take_damage(executes[user_action](player.level, player.strength) * 1.20, abilities.parry_resist)
                    print("You deal %.2f damage to target %s." % (abilities.primary_damage, i))
                else:
                    enemies[i].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
                    print("You deal %.2f damage to target %s." % (abilities.damage, i))
        abilities.last_used[user_action] = encounter_turn
    else:
        enemies[target].take_damage(executes[user_action](player.level, player.strength), abilities.parry_resist)
        print("You deal %.2f damage to target %s." % (abilities.damage, target))
        abilities.last_used[user_action] = encounter_turn

    for enemy in enemies:
        if enemy in enemies_left and enemies[enemy].health <= 0:
            print("Enemy%s dies." % enemy)
            del enemies_left[enemy]
        
    if len(enemies_left) == 0:
        break
    else:
        for enemy in enemies_left:
            if enemies_left[enemy].distance == "melee":
                player.take_damage(abilities.melee(enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
                print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
            elif enemies_left[enemy].distance == "ranged":
                player.take_damage(abilities.shoot(enemies_left[enemy].level, enemies_left[enemy].strength, enemies_left[enemy].accuracy), abilities.parry_resist)
                if abilities.damage == 0:
                    print("Enemy%s misses." % (enemy))
                else:
                    print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
    
    if player.health <= 0:
        print("You died. rip.")
        sys.exit()
       
print("Congrats!! You really showed them.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.

sleep(TINY_PAUSE_IN_SECONDS)
"""Level 4"""
print("Nice! You level up! You are now level 4.")
player.level_up()
print(player)

print("...")
wait = raw_input("Press enter to continue.")


"""Encounter 6"""
print("A big boi blocks the road.")
sleep(TINY_PAUSE_IN_SECONDS)
enemy1 = Enemy(5, 'melee', True, "", "")
enemy1.strength -= 4          ## Lowering his strength to make him more tank-like
enemy1.max_health += 20        ## Raising his health to make him more tank-like
enemy1.health += 20
enemy1.parry_chance += 0.15     ## To encourage him to parry at least like once.
enemies = {'1':enemy1}
enemies_left = dict(enemies)
encounter_turn = 0
player.take_damage(abilities.melee(enemies_left['1'].level, enemies_left['1'].strength), abilities.parry_resist)
print("You take %.2f damage from Enemy%s." % (abilities.damage, '1'))
sleep(TINY_PAUSE_IN_SECONDS)
print("You realize that he isn't friendly.")
sleep(TINY_PAUSE_IN_SECONDS)
print("Enemies: %s" % (enemies_left))
print("You also notice that he has a shield.")

"""Encounter 6 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 6 Target Choosing"""
    
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
        else:
            print("You deal %.2f damage to target %s." % (enemies_left[target].damage_taken, target))
        abilities.last_used[user_action] = encounter_turn

    for enemy in enemies:
        if enemy in enemies_left and enemies[enemy].health <= 0:
            print("Enemy%s dies." % enemy)
            del enemies_left[enemy]
        
    if len(enemies_left) == 0:
        break
    else:
        for enemy in enemies_left:
            if enemies_left[enemy].distance == "melee":
                player.take_damage(abilities.melee(enemies_left[enemy].level, enemies_left[enemy].strength), abilities.parry_resist)
                if player.parry:
                    print("You parry Enemy%s's attack." % (enemy))
                else:
                    print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
            elif enemies_left[enemy].distance == "ranged":
                player.take_damage(abilities.shoot(enemies_left[enemy].level, enemies_left[enemy].strength, enemies_left[enemy].accuracy), abilities.parry_resist)
                if abilities.damage == 0:
                    print("Enemy%s misses." % (enemy))
                else:
                    print("You take %.2f damage from Enemy%s." % (abilities.damage, enemy))
    
    if player.health <= 0:
        print("You died. rip.")
        sys.exit()
       
print("Congrats!! He dead.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)

sleep(TINY_PAUSE_IN_SECONDS)
"""Level 5"""
print("Nice! You level up to level 5!")
player.level_up()
print(player)
sleep(TINY_PAUSE_IN_SECONDS)
print("You pick up his shield, and decide to keep it...")
sleep(TINY_PAUSE_IN_SECONDS)
player.has_shield = True
print("You gain 2 new abilities!")
abilities.names['4'] = "Shield Bash"
abilities.description['4'] = "Shield Bash: A blunt attack that deals moderate damage to a single enemy, and causes you to take reduced damage for 1 turn. (5 turn)"
executes['4'] = abilities.shield_bash
print(abilities.description['4'])
abilities.names['5'] = "Block"
abilities.description['5'] = "Block: Rest behind your shield, taking reduced damage and lowering your other cooldowns by 1 turn. (no cooldown)"
executes['5'] = abilities.block
print(abilities.description['5'])
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
print("")
print("Note: For shield block, even though it would seem unnecessary to choose a target, you will still be prompted to do so to give you a chance to change your mind.")

print("...")
wait = raw_input("Press enter to continue.")



"""Encounter 7"""
print("aaaaaaand, you get ambushed.")
sleep(TINY_PAUSE_IN_SECONDS)
enemy1 = Enemy(3, 'melee', True, "", "")
enemy2 = Enemy(3, 'melee', True, "", "")
enemy3 = Enemy(3, 'melee', True, "", "")
enemy4 = Enemy(3, 'melee', True, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3, '4':enemy4}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 7 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 7 Target Choosing"""
    
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
    if user_action in abilities.cd_reduction_abilities:
        for i in abilities.cd_reduce_which[user_action]:
            abilities.last_used[i] -= abilities.cd_reduction_abilities[user_action]
    
    for enemy in enemies:
        if enemy in enemies_left and enemies[enemy].health <= 0:
            print("Enemy%s dies." % enemy)
            del enemies_left[enemy]
        
    if len(enemies_left) == 0:
        break
    else:
        for enemy in enemies_left:
            if enemies_left[enemy].distance == "melee":
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
        
    player.incoming_damage_multiplier = 1
       
print("Congrats!! Those suckers had it coming.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)

"""Level 6"""
print("Nice! Level 6!")
player.level_up()
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
abilities.names['6'] = "Maim"
abilities.description['6'] = "Maim: Quickly maim the target, causing them to bleed over 5 turns. (no cooldown)"
print(abilities.description['6'])
executes['6'] = abilities.maim
dot_executes['6'] = abilities.maim_bleed


"""Encounter 8"""
print("What starts with am and ends with bushed? That's right, you were ambushed.")
sleep(TINY_PAUSE_IN_SECONDS)
enemy1 = Enemy(6, 'melee', True, "", "")
enemy2 = Enemy(5, 'melee', False, "", "")
enemies = {'1':enemy1, '2':enemy2}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 8 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 8 Target Choosing"""
    
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
    if user_action in abilities.cd_reduction_abilities:
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
            if enemies_left[enemy].distance == "melee":
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
    player.incoming_damage_multiplier = 1
    
    if len(enemies_left) == 0:
        break
       
print("Eh, that was ok.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)


print("...")
wait = raw_input("Press enter to continue.")

"""Encounter 9"""
print("A giant, wooden horse blocks your path.")
sleep(TINY_PAUSE_IN_SECONDS)
print("You decide that it's probably safe...")
sleep(TINY_PAUSE_IN_SECONDS)
print("Holy Hades, it's an ambush.")
enemy1 = Enemy(3, 'melee', True, "", "")
enemy2 = Enemy(3, 'melee', False, "", "")
enemy3 = Enemy(3, 'ranged', False, "", "")
enemy4 = Enemy(3, 'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3, '4':enemy4}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 9 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 9 Target Choosing"""
    
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
    if user_action in abilities.cd_reduction_abilities:
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
            if enemies_left[enemy].distance == "melee":
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
    player.incoming_damage_multiplier = 1
    
    if len(enemies_left) == 0:
        break
       
print("Congrats!! You totally desTROYed them.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)


"""Level 7"""
print("Nice! Level 7!")
player.level_up()
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
abilities.names['7'] = "Backhand Strike"
abilities.description['7'] = "Backhand Strike: Swing at the target in a backhand motion doing moderate damage and reducing the cooldown on Shield Bash by 1 turn. (2 turns)"
print(abilities.description['7'])
executes['7'] = abilities.backhand_strike


"""Encounter 10"""
print("Something blocks your way. It looks suspiciously like a mini-boss to end the tutorial...")
enemy1 = Enemy(7, 'melee', True, "mini-boss", "")
enemies = {'1':enemy1}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 10 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 10 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You essentially finished the tutorial.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.

"""Level 8-10"""
print("Nice! Level 8!")
print("You can now also level up a stat called agility.")
print("Agility reduces all your cooldowns permanently by 1 turn for every 5 points. (1 point per increase)")
player.level_up()
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
print("Nice! Level 9!")
print("As a reminder, strength increases damage, shield block damage mitigation, parry chace, and resistance to parry. (+1)")
print("Max_health increases maximum health. (+20)")
print("Health regen increases health regeneration about each battle. (+5%)")
player.level_up()
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
print("Nice! Level 10!")
player.level_up()
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)



"""THE REAL FITGHT BEGINS"""

print("Now, you will level up much less often, so try to use your health as efficiently as possible.")

"""LEVEL 1"""
"""Encounter 1-1"""
print("Encounter 1-1")
enemy1 = Enemy(8, 'melee', True, "", "")
enemy2 = Enemy(8, 'melee', True, "", "")
enemies = {'1':enemy1, '2':enemy2}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 1-1 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 1-1 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("you did it.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)


"""Encounter 1-2"""
print("Encounter 1-2")
enemy1 = Enemy(7, 'melee', True, "", "")
enemy1.strength -= 5
enemy2 = Enemy(6, 'melee', False, "", "")
enemy3 = Enemy(7,'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 1-2 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 1-2 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You beat the second encounter.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)

"""Encounter 1-3"""
print("Encounter 1-3 BOSS")
enemy1 = Enemy(12, 'melee', True, "boss", "")
enemies = {'1':enemy1}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 1-3 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 1-3 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You beat the first level.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.

print("Nice! Level 11!")
player.level_up()
if player.increased_stat.lower() == 'a' and player.agility % 5 == 0:     ##For every 5 points...
    for i in abilities.cooldown:
        abilities.cooldown[i] -= 1     ##reduce all cooldowns by 1 turn.
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
    

"""LEVEL 2"""
"""Encounter 2-1"""
print("Encounter 2-1")
enemy1 = Enemy(6, 'melee', False, "", "")
enemy2 = Enemy(6, 'melee', False, "", "")
enemy3 = Enemy(6, 'melee', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 2-1 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 2-1 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You essentially finished the tutorial.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)


"""Encounter 2-2"""
print("Encounter 2-2")
enemy1 = Enemy(6, 'ranged', False, "", "")
enemy1.strength -= 5
enemy2 = Enemy(6, 'ranged', False, "", "")
enemy2.strength -= 5
enemy3 = Enemy(6, 'ranged', False, "", "")
enemy3.strength -= 5
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 2-2 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 2-2 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You essentially finished the tutorial.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)

"""Encounter 2-3"""
print("Encounter 2-3 BOSS")
enemy1 = Enemy(4, 'melee', True, "mini-boss", "")
enemy2 = Enemy(4, 'melee', True, "", "")
enemy2.strength -= 3
enemy3 = Enemy(4, 'melee', True, "", "")
enemy3.strength -= 3
enemy4 = Enemy(4, 'melee', False, "", "")
enemy5 = Enemy(4, 'melee', False, "", "")
enemy6 = Enemy(4, 'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3, '4':enemy4, '5':enemy5, '6':enemy6}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 2-3 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 2-3 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You beat the second level.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.

print("Nice! Level 12!")
player.level_up()
if player.increased_stat.lower() == 'a' and player.agility % 5 == 0:     ##For every 5 points...
    for i in abilities.cooldown:
        abilities.cooldown[i] -= 1     ##reduce all cooldowns by 1 turn.
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)



"""LEVEL 3"""
"""Encounter 3-1"""
print("Encounter 3-1")
enemy1 = Enemy(13, 'melee', True, "mini-boss", "")
enemies = {'1':enemy1}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 3-1 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 3-1 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You essentially finished the tutorial.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)


"""Encounter 3-2"""
print("Encounter 3-2")
enemy1 = Enemy(7, 'melee', True, "", "")
enemy2 = Enemy(7, 'melee', False, "", "")
enemy3 = Enemy(7, 'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 3-2 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 3-2 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You essentially finished the tutorial.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.
player.heal(player.max_health * player.heal_after_battle_percent)

"""Encounter 3-3"""
print("Encounter 3-3 BOSS")
enemy1 = Enemy(10, 'melee', True, "boss", "")
enemy1.strength -= 5
enemy1.max_health += 40
enemy1.health += 40
enemy2 = Enemy(4, 'melee', False, "", "")
enemy3 = Enemy(4, 'ranged', False, "", "")
enemy3.health -= 20
enemy3.max_health -= 20
enemy4 = Enemy(6, 'ranged', False, "", "")
enemy4.health -= 20
enemy4.max_health -= 20

enemies = {'1':enemy1, '2':enemy2, '3':enemy3, '4':enemy4}
print("Enemies: %s" % (enemies))
enemies_left = dict(enemies)
encounter_turn = 0


"""Encounter 3-3 Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    user_action = ""
    while user_action not in abilities.description:
        user_action = raw_input("Choose an ability: %s: " % (abilities.names))
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
            
    """Encounter 3-3 Target Choosing"""
    
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
            if enemies_left[enemy].distance == "melee":
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
       
print("grats. You beat the third level.")

"""Reset after battle"""
for key in abilities.last_used:
    abilities.last_used[key] = -99             ##-99 is to make sure abilities do not start on cooldown.

print("Nice! Level 13!")
player.level_up()
if player.increased_stat.lower() == 'a' and player.agility % 5 == 0:     ##For every 5 points...
    for i in abilities.cooldown:
        abilities.cooldown[i] -= 1     ##reduce all cooldowns by 1 turn.
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)




"""LEVEL 4"""

print("You find a wandering adventurer.")
print("He decides to join you.")
print("He says he can heal you while you are in combat by bringing out your own regeneration in the heat of battle.")
friend_name = raw_input("What would you like to call him/her? ")

"""Encounter 4-1"""
print("Encounter 4-1")
enemy1 = Enemy(16, 'melee', True, "mini-boss", "-1")
enemies = {'1':enemy1}

battle.battle(game_turn, abilities, executes, dot_executes, player, enemies, friend_name)

"""Encounter 4-2"""
print("Encounter 4-2")
enemy1 = Enemy(10, 'melee', False, "", "")
enemy2 = Enemy(8, 'melee', False, "", "")
enemy3 = Enemy(8, 'melee', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}

battle.battle(game_turn, abilities, executes, dot_executes, player, enemies, friend_name)

"""Encounter 4-3"""
print("Encounter 4-3")
enemy1 = Enemy(7, 'melee', True, "", "")
enemy2 = Enemy(5, 'melee', False, "", "")
enemy3 = Enemy(5, 'melee', False, "", "")
enemy4 = Enemy(5, 'melee', False, "", "")
enemy5 = Enemy(5, 'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3, '4':enemy4, '5':enemy5}

battle.battle(game_turn, abilities, executes, dot_executes, player, enemies, friend_name)

"""Encounter 4-4"""
print("Encounter 4-4")
enemy1 = Enemy(13, 'melee', True, "boss", "-1")
enemy2 = Enemy(5, 'melee', False, "", "")
enemy3 = Enemy(5, 'ranged', False, "", "")
enemies = {'1':enemy1, '2':enemy2, '3':enemy3}

battle.battle(game_turn, abilities, executes, dot_executes, player, enemies, friend_name)


print("Nice! Level 14!")
player.level_up()
if player.increased_stat.lower() == 'a' and player.agility % 5 == 0:     ##For every 5 points...
    for i in abilities.cooldown:
        abilities.cooldown[i] -= 1     ##reduce all cooldowns by 1 turn.
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)


print("Nice! Level 15!")
player.level_up()
if player.increased_stat.lower() == 'a' and player.agility % 5 == 0:     ##For every 5 points...
    for i in abilities.cooldown:
        abilities.cooldown[i] -= 1     ##reduce all cooldowns by 1 turn.
print(player)
for i in abilities.self_effect_value:
    abilities.self_effect_value[i] = (1 - player.shield_cover_perc)
    
"""Encounter 5-0"""
print("Encounter 5-0")
print("FINAL BOSS")
enemy1 = Enemy(20, 'melee', True, "boss", "-2")
enemy2 = Enemy(5, 'ranged', False, "", "-1")
enemy3 = Enemy(8, 'ranged', False, "", "-1")
enemy4 = Enemy(12, 'ranged', False, "", "-1")
enemy5 = Enemy(20, 'ranged', False, "mini-boss", "-1")

enemies = {'1':enemy1}
enemies_left = dict(enemies)

encounter_turn = 0
names_with_cd = dict(abilities.names)
print("Enemies: %s" % (enemies_left))

"""Ability Choosing"""
while True:
    game_turn += 1
    encounter_turn += 1
    print("Turn: %s" % encounter_turn)
    
    if encounter_turn == 3:
        enemies['2'] = enemy2
        enemies_left['2'] = enemy2
        print("A minion joins the fight.")
        print("Enemies: %s" % (enemies_left))
    if encounter_turn == 13:
        enemies['3'] = enemy3
        enemies_left['3'] = enemy3
        print("Another minion joins the fight.")
        print("Enemies: %s" % (enemies_left))
    if encounter_turn == 23:
        enemies['4'] = enemy4
        enemies_left['4'] = enemy4
        print("Another minion joins the fight. They keep getting stronger.")
        print("Enemies: %s" % (enemies_left))
    if encounter_turn == 33:
        print("You feel a sense of urgency to finish the fight.")
    if encounter_turn == 35:
        enemies['5'] = enemy5
        enemies_left['5'] = enemy5
        print("Another mini-boss joins the fight.")
        print("Enemies: %s" % (enemies_left))

    if encounter_turn % 3 == 0:
        player.heal(player.max_health*player.heal_after_battle_percent)
        print("%s heals you for %.2f." % (friend_name, (player.heal_after_battle_percent*player.max_health*0.75)))
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
        
    if len(enemies_left) == 0 or enemies['1'].health <= 0:
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
    
    if len(enemies_left) == 0 or enemies['1'].health <= 0:
        break
       
print("Congratulation. You won.")
print("You beat the game in %s turns." % (game_turn))
print("Thank you for playing. You're the best! :)")
