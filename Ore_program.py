#!/usr/bin/env python3
import csv

import Ore_processing_skill
import Ore_classes


def main():
    '''Main function for whole program, Includes loop to continue program unless user selects 'n' at the end'''
    continue_program = 'y'
    while continue_program == 'y':
        player_ore_stats = 0
        player_ore_stats = Ore_processing_skill.Ore_Processing.ore_stats()
        ore_dict = Ore_classes.ore_mineral_info()
        ore_amount = Ore_classes.ore_amount()

        mineral_header = ["mineral", "amount"]
        mineral_key_list = []
        mineral_value_list = []
        mineral_total = []


        for key, value in ore_dict.items():
            ore_dict[key] = (value * player_ore_stats) * ore_amount

        print(ore_dict)
        try:
            continue_program = input("Would you like to try again(y/n): ")
            if continue_program.lower() == 'n' or continue_program.lower() == 'y':
                continue
        except:
            print("Please enter y/n: ")
        if continue_program == 'n':
            break
    print("Goodbye!")


main()