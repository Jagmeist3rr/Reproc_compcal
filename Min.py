#!/usr/bin/env python 3
#Skill level page
import Mineral_classes

class Skill_Level():
    player_skill_level = 0
    basic_levels = {}
    advanced_levels = {}
    expert_levels = {}

    def Get_Player_Skill_Level():
        while True:
            Skill_Level.player_skill_level = int(input("What is your total Ore Processing Skill level: "))
            if 0 < Skill_Level.player_skill_level < 16:
                break
            print("Please enter a number from 1-15: ")
        return Skill_Level.player_skill_level

class Ore_Processing(Skill_Level):
    Skill_Level.Get_Player_Skill_Level()
    player_ore_proficiency = 0
    percent_ore_proficiency = 30.0
    basic_levels = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    advanced_levels = {6: 10, 7: 15, 8: 20, 9: 25, 10: 30}
    expert_levels = {11: 5, 12: 10, 13: 15, 14: 20, 15: 25}
    all_ore_processing_levels = [basic_levels, advanced_levels, expert_levels]
    updated_ore_processing_levels = {}

    def calculate_level_percentages():
        for dict_list in Ore_Processing.all_ore_processing_levels:
            for key, value in dict_list.items():
                Ore_Processing.updated_ore_processing_levels[key] = (value * Ore_Processing.percent_ore_proficiency)/100
        return Ore_Processing.updated_ore_processing_levels

    def ore_stats():
        Ore_Processing.calculate_level_percentages()
        if Skill_Level.player_skill_level < 6:
            Ore_Processing.player_ore_proficiency = Ore_Processing.percent_ore_proficiency + Ore_Processing.updated_ore_processing_levels[Skill_Level.player_skill_level]
            return Ore_Processing.player_ore_proficiency
        elif 5 < Skill_Level.player_skill_level < 11:
            Ore_Processing.player_ore_proficiency = Ore_Processing.percent_ore_proficiency + Ore_Processing.updated_ore_processing_levels[5] + Ore_Processing.updated_ore_processing_levels[Skill_Level.player_skill_level]
            return Ore_Processing.player_ore_proficiency
        elif Skill_Level.player_skill_level > 10:
            Ore_Processing.player_ore_proficiency = Ore_Processing.percent_ore_proficiency + Ore_Processing.updated_ore_processing_levels[5] + Ore_Processing.updated_ore_processing_levels[10] + Ore_Processing.updated_ore_processing_levels[Skill_Level.player_skill_level]
            return Ore_Processing.player_ore_proficiency
        else:
            print("Error")

reproc3 = Ore_Processing.ore_stats()
print(reproc3)




