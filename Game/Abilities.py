'''
Created on Jul 15, 2018

@author: Andrew Fletcher
'''

import random
    
class Abilities(object):
    '''
    The class for the abilities
    '''
    description = {'1':"Melee: A basic, weak move that serves as a good filler move. (No cooldown)"}
    names = {'1':"Melee"}              ## Additional names and descriptions are added in main script as player progresses.
    cooldown = {'1':0, '2':3, '3':1, '4':7, '5':0, '6':0, '7':2, '-1':3, '-2':7}          ## number of turns an ability is on cooldown.
    last_used = {'1':-99,'2':-99,'3':-99, '4':-99, '5':-99, '6':-99, '7':-99, '-1':-99, '-2':-99}     ## -99 is to make sure the ability does not start the fight on cooldown.
    self_effect_value = {'4':0, '5':0}
    self_effect_duration = {'4':2, '5':1}
    dot_duration = {'6':6}
    cast_time = {'-1':1, '-2':2}
    cd_reduction_abilities = {'5':1, '7':1}     ## 1 for one turn reduced on the cooldown.
    cd_reduce_which = {'5':['1','2','3','4','6','7'], '7':['4']}
    is_aoe = ['3']
    is_dot = ['6']

    
    LOWER_BOUND = 0.8
    DAMAGE_VARIANCE = 0.4
    SMALL_LOWER_BOUND = 0.9
    SMALL_DAMAGE_VARIANCE = 0.2
    NORMAL_RESIST = 1
    UNAVOIDABLE = 999
    BLUNT_PARRY_RESIST = 5
    

    def __init__(self):
        '''
        Constructor
        '''
    
    def is_on_cd(self, cd, turn_used, current_turn):
        since_used = current_turn - (turn_used + 1)     ## +1 is to make the cooldown start the turn after ability is used.
        if since_used < cd:
            print("There are %s turns left on its cooldown." % (cd-since_used))
            return True
        else:
            return False

    def enemy_is_on_cd(self, cd, turn_used, current_turn):
        since_used = current_turn - (turn_used + 1)     ## +1 is to make the cooldown start the turn after ability is used.
        if since_used < cd:
            return True
        else:
            return False
    
    def is_active(self, duration, turn_used, current_turn):
        if (current_turn-turn_used) < duration:
            return True
        else:
            return False
    
    def melee(self, level, strength):
        """Ability '1'"""
        self.damage = strength*self.LOWER_BOUND + random.random()*strength*self.DAMAGE_VARIANCE
        self.parry_resist = self.NORMAL_RESIST * (level + strength)
        return self.damage
    
    def shoot(self, level, strength, accuracy):
        SHOOT_DAMAGE_WEIGHT = 1.3
        self.parry_resist = self.UNAVOIDABLE
        if random.random() <= accuracy:
            self.damage = SHOOT_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*SHOOT_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE
            return self.damage
        else:
            self.damage = 0
            return 0
    
    def heavy_strike(self, level, strength):
        """Ability '2'"""
        HEAVY_STRIKE_DAMAGE_WEIGHT = 1.5
        self.parry_resist = self.BLUNT_PARRY_RESIST * (level + strength)
        self.damage = HEAVY_STRIKE_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*HEAVY_STRIKE_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE
        return self.damage
    
    def sweeping_strike(self, level, strength):
        """Ability '3'"""
        SWEEPING_STRIKE_DAMAGE_WEIGHT = 0.5
        self.parry_resist = self.NORMAL_RESIST * (level + strength)
        self.damage = SWEEPING_STRIKE_DAMAGE_WEIGHT*strength*self.SMALL_LOWER_BOUND + random.random()*SWEEPING_STRIKE_DAMAGE_WEIGHT*strength*self.SMALL_DAMAGE_VARIANCE
        SWEEPING_STRIKE_PRIMARY_DAMAGE_WEIGHT = 1.20
        self.primary_damage = self.damage * SWEEPING_STRIKE_PRIMARY_DAMAGE_WEIGHT
        return self.damage
    
    def shield_bash(self, level, strength):
        """Ability '4'"""
        SHIELD_BASH_DAMAGE_WEIGHT = 1.4
        self.parry_resist = self.BLUNT_PARRY_RESIST * (level + strength)
        self.damage = SHIELD_BASH_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*SHIELD_BASH_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE
        return self.damage
    
    def block(self, level, strength):
        """Ability '5'"""
        self.damage = 0
        return self.damage
    
    def maim(self, level, strength):
        """Ability '6'"""
        MAIM_DAMAGE_WEIGHT = 0.1
        self.parry_resist = self.UNAVOIDABLE
        self.damage = MAIM_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*MAIM_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE
        return self.damage
    
    def maim_bleed(self, level, strength):
        """Ability '6' (dot)"""
        MAIM_BLEED_DAMAGE_WEIGHT = 2.0
        self.parry_resist = self.UNAVOIDABLE
        self.damage = (MAIM_BLEED_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*MAIM_BLEED_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE)/6     ##/6 because over 6 turns.
        return self.damage
    
    def backhand_strike(self, level, strength):
        """Ability '7'"""
        BACKHAND_STRIKE_DAMAGE_WEIGHT = 1.2
        self.parry_resist = self.NORMAL_RESIST * (level + strength)
        self.damage = BACKHAND_STRIKE_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*BACKHAND_STRIKE_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE
        return self.damage

    def roundhouse_strike(self, level, strength):
        """Ability '-1'"""
        ROUNDHOUSE_STRIKE_DAMAGE_WEIGHT = 3
        self.parry_resist = self.UNAVOIDABLE
        self.damage = ROUNDHOUSE_STRIKE_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*ROUNDHOUSE_STRIKE_DAMAGE_WEIGHT*strength*self.DAMAGE_VARIANCE
        return self.damage

    def final_smash(self, level, strength):
        """Ability -2"""
        FINAL_SMASH_DAMAGE_WEIGHT = 5
        self.parry_resist = self.UNAVOIDABLE
        self.damage = FINAL_SMASH_DAMAGE_WEIGHT*strength*self.LOWER_BOUND + random.random()*FINAL_SMASH_DAMAGE_WEIGHT*self.DAMAGE_VARIANCE
        return self.damage
