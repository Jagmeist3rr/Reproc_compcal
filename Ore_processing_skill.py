#!/usr/bin/env python3
# Skill level page


class Skill_Level():
    '''Sets player skill and makes 3 dictionaries for basic, advance, and expert skills'''
    player_skill_level = 0
    basic_levels = {}
    advanced_levels = {}
    expert_levels = {}

    def get_player_skill_level():
        '''Askes the user for their level, function ensures that number is within range of 0-15 and returns that number'''
        while True:
            while True:
                try:
                    Skill_Level.player_skill_level = int(input("What is your total Ore Processing Skill level: "))
                except ValueError:
                    print('Please enter a valid number')
                    continue
                break
            if -1 < Skill_Level.player_skill_level < 16:
                break
            print("Please enter a number from 0 -15: ")
        return Skill_Level.player_skill_level

class Ore_Processing(Skill_Level):
    '''Takes the user level and returns the player's ore processing skill percentage'''
    player_ore_proficiency = 0
    percent_ore_proficiency = 30.0
    basic_levels = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    advanced_levels = {6: 10, 7: 15, 8: 20, 9: 25, 10: 30}
    expert_levels = {11: 5, 12: 10, 13: 15, 14: 20, 15: 25}
    all_ore_processing_levels = [basic_levels, advanced_levels, expert_levels]
    updated_ore_processing_levels = {}

    def calculate_level_percentages():
        '''Takes the skill level dictionaries and converts it into a new dictionary with values as the correct percentage number'''
        for dict_list in Ore_Processing.all_ore_processing_levels:
            for key, value in dict_list.items():
                Ore_Processing.updated_ore_processing_levels[key] = (value * Ore_Processing.percent_ore_proficiency)/100
        return Ore_Processing.updated_ore_processing_levels

    def ore_stats():
        '''Takes the updated skill level dicitionary and player's skill level and returns the appropriate skill percentage for ore processing'''
        Skill_Level.get_player_skill_level()
        Ore_Processing.calculate_level_percentages()
        if 0 < Skill_Level.player_skill_level < 6:
            Ore_Processing.player_ore_proficiency = Ore_Processing.percent_ore_proficiency + Ore_Processing.updated_ore_processing_levels[Skill_Level.player_skill_level]
            return Ore_Processing.player_ore_proficiency
        elif 5 < Skill_Level.player_skill_level < 11:
            Ore_Processing.player_ore_proficiency = Ore_Processing.percent_ore_proficiency + Ore_Processing.updated_ore_processing_levels[5] + Ore_Processing.updated_ore_processing_levels[Skill_Level.player_skill_level]
            return Ore_Processing.player_ore_proficiency
        elif Skill_Level.player_skill_level > 10:
            Ore_Processing.player_ore_proficiency = Ore_Processing.percent_ore_proficiency + Ore_Processing.updated_ore_processing_levels[5] + Ore_Processing.updated_ore_processing_levels[10] + Ore_Processing.updated_ore_processing_levels[Skill_Level.player_skill_level]
            return Ore_Processing.player_ore_proficiency
        elif Skill_Level.player_skill_level == 0:
            print("work")
            Ore_Processing.player_ore_proficiency = 30
            return Ore_Processing.player_ore_proficiency
        else:
            print("Error")





