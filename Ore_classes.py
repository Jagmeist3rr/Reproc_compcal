#!/usr/bin/env python3
# Mineral class and processing amounts
import Mineral_classes


class Ores():
    '''Base class that makes empty dictionaries and functions that retrieve and create ore dictionaries'''
    ore_dict = {}
    ore_name = ""
    mineral_list = {}
    mineral_name = ""

    def retrieve_mineral_info_normal(ore_name, ore_dict):
        '''Takes the ore dictionary from Mineral_Classes and makes an ore dictionary which contains the list of minerals and amount of each mineral'''
        # For normal ore mineral list
        for dict_list in Mineral_classes.all_ores_dict_list:
            for key, value in dict_list.items():
                if ore_name.lower() == key.lower():
                    if ore_name in dict_list:
                        mineral_name = list(dict_list)[-1]
                        ore_dict[mineral_name] = value/30
        return ore_dict

    def mineral_info_rich(ore_name, ore_dict):
        '''Takes the normal ore dictionary and mulitplies the values by 10 for any rich ore types that are used'''
        rich_dict = Ores.retrieve_mineral_info_normal(ore_name, ore_dict)
        for key, value in rich_dict.items():
            rich_dict[key] = round(value * 10, 2)
        return rich_dict

    def mineral_info_compressed(ore_name, ore_dict):
        '''Takes the normal ore dictionary and mulitplies the values by 100 for any compressed ore types that are used'''
        compressed_dict = Ores.retrieve_mineral_info_normal(ore_name, ore_dict)
        for key, value in ore_dict.items():
            compressed_dict[key] = round(value * 100, 2)
        return compressed_dict

# The classes below and based on the different Ores and contains their name and an empty ore dictionary
class Veldspar(Ores):
    ore_name = "Veldspar"
    ore_dict = {}


class Scordite(Ores):
    ore_name = "Scordite"
    ore_dict = {}


class Pyroxeres(Ores):
    ore_name = "Pyroxeres"
    ore_dict = {}


class Plagioclase(Ores):
    ore_name = "Plagioclase"
    ore_dict = {}


class Omber(Ores):
    ore_name = "Omber"
    ore_dict = {}


class Kernite(Ores):
    ore_name = "Kernite"
    ore_dict = {}


class Jaspet(Ores):
    ore_name = "Jaspet"
    ore_dict = {}


class Hemorphite(Ores):
    ore_name = "Hemorphite"
    ore_dict = {}


class Hedbergite(Ores):
    ore_name = "Hedbergite"
    ore_dict = {}


class Spodumain(Ores):
    ore_name = "Spodumain"
    ore_dict = {}


class Dark_Ochre(Ores):
    ore_name = "Dark Ochre"
    ore_dict = {}


class Gneiss(Ores):
    ore_name = "Gneiss"
    ore_dict = {}


class Crokite(Ores):
    ore_name = "Crokite"
    ore_dict = {}


class Bistot(Ores):
    ore_name = "Bistot"
    ore_dict = {}


class Arkonor(Ores):
    ore_name = "Arkonor"
    ore_dict = {}


class Mercoxit(Ores):
    ore_name = "Mercoxit"
    ore_dict = {}


def select_ore_type():
    '''Retrieves input from user and askes for what type of ore the user will be processing, i.e Normal ore, Rich Ore, Compressed Ore'''
    while True:
        ore_type = input("What ore type are you processing(Normal, Rich, Compressed): ")
        if ore_type.lower() == "normal" or ore_type.lower() == "rich" or ore_type.lower() == "compressed":
            break
        print("Please enter normal, rich, compressed: ")
    return ore_type


def select_ore_name():
    '''Retrieves inout from user and askes for which ore they will be processing'''
    ore_list = ["veldspar", "scordite", "pyroxeres", "plagioclase", "omber", "jaspet", "hedbergite", "dark ochre",
                "crokite", "arkonor", "kernite", "hemorphite", "spodumain", "gneiss", "bistot", "mercoxit"]
    while True:
        ore_name = input("What ore are you processing: ")
        if ore_name in ore_list:
            break
        print("Please enter a proper ore name: ")
    return ore_name


def ore_mineral_info():
    '''Calls on the functions to retrieve ore name and ore type and then returns the appropriate dictionary for each type of ore'''
    ore_name = select_ore_name()
    ore_type = select_ore_type()
    if ore_name == "veldspar":
        if ore_type == "normal":
            return Veldspar.retrieve_mineral_info_normal(Veldspar.ore_name, Veldspar.ore_dict)
        elif ore_type == "rich":
            return Veldspar.mineral_info_rich(Veldspar.ore_name, Veldspar.ore_dict)
        elif ore_type == "compressed":
            return Veldspar.mineral_info_compressed(Veldspar.ore_name, Veldspar.ore_dict)
    elif ore_name == "scordite":
        if ore_type == "normal":
            return Scordite.retrieve_mineral_info_normal(Scordite.ore_name, Scordite.ore_dict)
        elif ore_type == "rich":
            return Scordite.mineral_info_rich(Scordite.ore_name, Scordite.ore_dict)
        elif ore_type == "compressed":
            return Scordite.mineral_info_compressed(Scordite.ore_name, Scordite.ore_dict)
    elif ore_name == "pyroxeres":
        if ore_type == "normal":
            return Pyroxeres.retrieve_mineral_info_normal(Pyroxeres.ore_name, Pyroxeres.ore_dict)
        elif ore_type == "rich":
            return Pyroxeres.mineral_info_rich(Pyroxeres.ore_name, Pyroxeres.ore_dict)
        elif ore_type == "compressed":
            return Pyroxeres.mineral_info_compressed(Pyroxeres.ore_name, Pyroxeres.ore_dict)
    elif ore_name == "plagioclase":
        if ore_type == "normal":
            return Plagioclase.retrieve_mineral_info_normal(Plagioclase.ore_name, Plagioclase.ore_dict)
        elif ore_type == "rich":
            return Plagioclase.mineral_info_rich(Plagioclase.ore_name, Plagioclase.ore_dict)
        elif ore_type == "compressed":
            return Plagioclase.mineral_info_compressed(Plagioclase.ore_name, Plagioclase.ore_dict)
    elif ore_name == "omber":
        if ore_type == "normal":
            return Omber.retrieve_mineral_info_normal(Omber.ore_name, Omber.ore_dict)
        elif ore_type == "rich":
            return Omber.mineral_info_rich(Omber.ore_name, Omber.ore_dict)
        elif ore_type == "compressed":
            return Omber.mineral_info_compressed(Omber.ore_name, Omber.ore_dict)
    elif ore_name == "jaspet":
        if ore_type == "normal":
            return Jaspet.retrieve_mineral_info_normal(Jaspet.ore_name, Jaspet.ore_dict)
        elif ore_type == "rich":
            return Jaspet.mineral_info_rich(Jaspet.ore_name, Jaspet.ore_dict)
        elif ore_type == "compressed":
            return Jaspet.mineral_info_compressed(Jaspet.ore_name, Jaspet.ore_dict)
    elif ore_name == "hedbergite":
        if ore_type == "normal":
            return Hedbergite.retrieve_mineral_info_normal(Hedbergite.ore_name, Hedbergite.ore_dict)
        elif ore_type == "rich":
            return Hedbergite.mineral_info_rich(Hedbergite.ore_name, Hedbergite.ore_dict)
        elif ore_type == "compressed":
            return Hedbergite.mineral_info_compressed(Hedbergite.ore_name, Hedbergite.ore_dict)
    elif ore_name == "dark ochre":
        if ore_type == "normal":
            return Dark_Ochre.retrieve_mineral_info_normal(Dark_Ochre.ore_name, Dark_Ochre.ore_dict)
        elif ore_type == "rich":
            return Dark_Ochre.mineral_info_rich(Dark_Ochre.ore_name, Dark_Ochre.ore_dict)
        elif ore_type == "compressed":
            return Dark_Ochre.mineral_info_compressed(Dark_Ochre.ore_name, Dark_Ochre.ore_dict)
    elif ore_name == "crokite":
        if ore_type == "normal":
            return Crokite.retrieve_mineral_info_normal(Crokite.ore_name, Crokite.ore_dict)
        elif ore_type == "rich":
            return Crokite.mineral_info_rich(Crokite.ore_name, Crokite.ore_dict)
        elif ore_type == "compressed":
            return Crokite.mineral_info_compressed(Crokite.ore_name, Crokite.ore_dict)
    elif ore_name == "mercoxit":
        if ore_type == "normal":
            return Mercoxit.retrieve_mineral_info_normal(Mercoxit.ore_name, Mercoxit.ore_dict)
        elif ore_type == "rich":
            return Mercoxit.mineral_info_rich(Mercoxit.ore_name, Mercoxit.ore_dict)
        elif ore_type == "compressed":
            return Mercoxit.mineral_info_compressed(Mercoxit.ore_name, Mercoxit.ore_dict)
    elif ore_name == "bistot":
        if ore_type == "normal":
            return Bistot.retrieve_mineral_info_normal(Bistot.ore_name, Bistot.ore_dict)
        elif ore_type == "rich":
            return Bistot.mineral_info_rich(Bistot.ore_name, Bistot.ore_dict)
        elif ore_type == "compressed":
            return Bistot.mineral_info_compressed(Bistot.ore_name, Bistot.ore_dict)
    elif ore_name == "gneiss":
        if ore_type == "normal":
            return Gneiss.retrieve_mineral_info_normal(Gneiss.ore_name, Gneiss.ore_dict)
        elif ore_type == "rich":
            return Gneiss.mineral_info_rich(Gneiss.ore_name, Gneiss.ore_dict)
        elif ore_type == "compressed":
            return Gneiss.mineral_info_compressed(Gneiss.ore_name, Gneiss.ore_dict)
    elif ore_name == "spodumain":
        if ore_type == "normal":
            return Spodumain.retrieve_mineral_info_normal(Spodumain.ore_name, Spodumain.ore_dict)
        elif ore_type == "rich":
            return Spodumain.mineral_info_rich(Spodumain.ore_name, Spodumain.ore_dict)
        elif ore_type == "compressed":
            return Spodumain.mineral_info_compressed(Spodumain.ore_name, Spodumain.ore_dict)
    elif ore_name == "hemorphite":
        if ore_type == "normal":
            return Hemorphite.retrieve_mineral_info_normal(Hemorphite.ore_name, Hemorphite.ore_dict)
        elif ore_type == "rich":
            return Hemorphite.mineral_info_rich(Hemorphite.ore_name, Hemorphite.ore_dict)
        elif ore_type == "compressed":
            return Hemorphite.mineral_info_compressed(Hemorphite.ore_name, Hemorphite.ore_dict)
    elif ore_name == "kernite":
        if ore_type == "normal":
            return Kernite.retrieve_mineral_info_normal(Kernite.ore_name, Kernite.ore_dict)
        elif ore_type == "rich":
            return Kernite.mineral_info_rich(Kernite.ore_name, Kernite.ore_dict)
        elif ore_type == "compressed":
            return Kernite.mineral_info_compressed(Kernite.ore_name, Kernite.ore_dict)
    elif ore_name == "arkonor":
        if ore_type == "normal":
            return Arkonor.retrieve_mineral_info_normal(Arkonor.ore_name, Arkonor.ore_dict)
        elif ore_type == "rich":
            return Arkonor.mineral_info_rich(Arkonor.ore_name, Arkonor.ore_dict)
        elif ore_type == "compressed":
            return Arkonor.mineral_info_compressed(Arkonor.ore_name, Arkonor.ore_dict)
