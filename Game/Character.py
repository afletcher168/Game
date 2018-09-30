'''
Created on Jul 12, 2018

@author: Andrew Fletcher
'''

import random
import sys
from pip._vendor.distlib.compat import raw_input

class Character(object):
    '''
    The parent class for all characters.
    '''

    def __init__(self, level):
        '''
        Constructor
        '''
        self.level = level
        self.max_health = level * 10
        self.health = level * 10
        self.strength = level * 1
        
    def take_damage(self, amount, parry_resist):
        self.parry = False
        if self.has_shield:
            if parry_resist == 999:     ##Unavoidable
                calculated_parry_chance = 0
            else:
                calculated_parry_chance = (self.parry_chance*(self.level+self.strength)/parry_resist + self.parry_chance)/2
        
            if calculated_parry_chance > 0.80:
                calculated_parry_chance = 0.80
            if random.random() <= calculated_parry_chance:
                self.parry = True
                self.damage_taken = 0
            else:
                self.health -= (amount*self.incoming_damage_multiplier)
                self.damage_taken = (amount*self.incoming_damage_multiplier)
        else:
            self.health -= amount
            self.damage_taken = amount
    
    def heal(self, amount):
        if self.health + amount > self.max_health:
            self.health = self.max_health
        else:
            self.health += amount
        

class Player(Character):
    '''
    The class for the player of the game.
    '''
    
    def __init__(self, level):
        '''
        Constructor
        '''
        self.level = level
        self.max_health = level*15 + 50
        self.health = level*15 + 50
        self.strength = level*3 + 3
        self.agility = 0
        self.heal_after_battle_percent = 0.20
        self.has_shield = False
        self.incoming_damage_multiplier = 1
        self.parry_chance = 0.20 - (0.05/self.level) - (0.15/(self.strength**(1/3))) + (0.001*self.strength)
        self.active_dots = {}
        
    def __repr__(self):
        print(" You are level: %s." % (self.level))
        print(" Your strength is: %s." % (self.strength))
        print(" Your max health is: %s." % (self.max_health))
        print(" Your current health is: %.2f." % (self.health))
        print(" Your health regen is: %.0f%%." % (self.heal_after_battle_percent*100))     ##100 is to make it a percent.
        if self.has_shield:
            print(" Your parry chance is: %.2f." % (self.parry_chance))
            print(" Your shield block damage mitigation is: %.2f percent." % (self.shield_cover_perc))
        if self.level > 7:
            print(" Your agility is %s." % (self.agility))

        return ""

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.strength += 2
        self.parry_chance = 0.20 - (0.05/self.level) - (0.15/(self.strength**(1/3))) + (0.001*self.strength)
        self.shield_cover_perc = 0.35 + (0.002*self.strength)
        print(self)
        print("Which stat would you like to increase?")
        while True:
            if self.level > 7:
                self.increased_stat = raw_input("'a' for agility (+1), 's' for strength (+1), 'h' for max_health (+30), 'r' for health regen (+5%): ")
            else:
                self.increased_stat = raw_input("'s' for strength (+1), 'h' for max_health (+30), 'r' for health regen (+5%): ")
            
            if self.increased_stat.lower() == 's':
                self.strength += 1
                break
            elif self.increased_stat.lower() == 'h':
                self.max_health += 30
                self.health = self.max_health
                break
            elif self.increased_stat.lower() == 'r':
                self.heal_after_battle_percent += 0.05
                break
            elif self.increased_stat.lower() == 'a' and self.level > 7:
                self.agility += 1
                break
            elif self.increased_stat.lower() == 'q' or self.increased_stat.lower() == 'quit':
                quit_option = raw_input("Are you sure you would like to QUIT? (y or q to quit)")
                if quit_option.lower() == 'q' or quit_option.lower() == "quit" or quit_option.lower() == 'y' or quit_option.lower() == "yes":
                    print("Only losers quit. :(")
                    sys.exit()
                else:
                    print("Good.")
            else:
                print("Please input a valid answer.")

class Enemy(Character):
    '''
    The class for the enemies.
    '''
    def __init__(self, level, distance, has_shield, is_boss, ability):
        '''
        Constructor
        '''
        self.level = level
        self.max_health = level * 15
        self.health = level * 15
        self.strength = level * 2
        self.accuracy = 1 - (0.5/level)
        self.distance = distance
        if distance == "melee":
            self.incoming_damage_multiplier = 0.70
        self.has_shield = has_shield
        if has_shield:
            self.parry_chance = 0.22 - (0.03/self.level) - (0.10/(self.strength**(1/3)))
            self.max_health += 10
        else:
            self.strength += 2
        self.is_boss = is_boss
        if is_boss == "mini-boss":
            self.max_health *= 1.25      ##25% more health
            self.health *= 1.25
            self.strength *= 1.15        ##15% more strength
        elif is_boss == "boss":
            self.max_health *= 3         ##200% more health
            self.health *= 3
            self.strength *= 1.30         ##30% more strength
        self.ability = ability
        self.incoming_damage_multiplier = 1
        self.active_dots = {}
        self.is_casting = -1     ##Turns left on cast

    def __repr__(self):
        if self.has_shield:
            has_shield_msg = "Shield"
            if self.is_boss == "boss" or self.is_boss == "mini-boss":
                return ("(%s/%.2f/%.2f/%s/%s/%s)" % (self.level,self.health,self.strength,self.distance,has_shield_msg,self.is_boss.upper()))
            else:
                return ("(%s/%.2f/%s/%s/%s)" % (self.level,self.health,self.strength,self.distance,has_shield_msg))
        else:
            if self.is_boss == "boss" or self.is_boss == "mini-boss":
                return ("(%s/%.2f/%.2f/%s/%s)" % (self.level,self.health,self.strength,self.distance,self.is_boss.upper()))
            else:
                return ("(%s/%.2f/%s/%s)" % (self.level,self.health,self.strength,self.distance))

