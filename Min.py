#!/usr/bin/env python 3
#Skill level page
import Min_test

class Skill_Level():
    player_skill_level = 0
    basic_levels = {}
    advanced_levels = {}
    expert_levels = {}
    def Get_Player_Skill_Level():
        Skill_Level.player_skill_level = int(input("What is your total Ore Processing Skill level: "))
        return Skill_Level.player_skill_level


class Ore_Processing(Skill_Level):
    Skill_Level.Get_Player_Skill_Level()
    base_ore_proficiency = 30.0
    percent_ore_proficiency = 30.0
    basic_levels = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    advanced_levels = {6: 10, 7: 15, 8: 20, 9: 25, 10: 30}
    expert_levels = {11: 5, 12: 10, 13: 15, 14: 20, 15: 25}
    all_ore_processing_levels = [basic_levels, advanced_levels, expert_levels]

    def calculate_level_percentages():
        updated_ore_processing_levels = {}
        for dict_list in Ore_Processing.all_ore_processing_levels:
            for key, value in dict_list.items():
                dict_list[key] = (value * Ore_Processing.percent_ore_proficiency)/100
                updated_ore_processing_levels = dict_list
        return updated_ore_processing_levels


    def obtain_player_ore_processing_level():
        for dict_list in Ore_Processing.all_ore_processing_levels:
            for key in dict_list:
                if Skill_Level.player_skill_level == key:
                    print("Finally")

Ore_Processing.calculate_level_percentages()
Ore_Processing.obtain_player_ore_processing_level()
#main()




