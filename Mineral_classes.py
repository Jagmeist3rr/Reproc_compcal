#!/usr/bin/env python3
# Mineral classes that show which ore that contain the mineral and the amount of the mineral in each of those ores

class Mineral():
    '''Base class to return a basic dictionary of each mineral that shows which ore is in'''
    ore_dict = {}

    def ore_dict_print(ore_dict):
        return ore_dict


class Tritanium(Mineral):
    ore_dict = {"Veldspar": 1.25, "Scordite": .49, "Plagioclase": .15, "Omber": 1.8, "Kernite": .8, "Pyroxeres": 5.26,
                "Dark Orchre": 2.88, "Spodumain": 59.1, "Hemorphite": 16.5, "Crokite": 116.4, "Arkonor": 26.4,
                "Tritanium": 0}


class Pyerite(Mineral):
    ore_dict = {"Scordite": .34, "Plagioclase": .2, "Omber": .23, "Pyroxeres": 1.68, "Gneiss": 2.64,
                "Spodumain": 11.22, "Hemorphite": 8.19, "Bistot": 18.36, "Pyerite": 0}


class Mexallon(Mineral):
    ore_dict = {"Plagioclase": .29, "Kernite": 1.44, "Pyroxeres": 0.75, "Gneiss": 2.76,
                "Spodumain": 1.08, "Jaspet": 7.38, "Arkonor": 3.0, "Mexallon": 0}


class Isogen(Mineral):
    ore_dict = {"Omber": 0.17, "Kernite": .14, "Dark Orchre": 0.17, "Gneiss": 0.55,
                "Spodumain": .18, "Hemorphite": 0.48, "Hedbergite": 1.38, "Isogen": 0}


class Nocxium(Mineral):
    ore_dict = {"Pyroxeres": 0.09, "Dark Orchre": 0.13,  "Hemorphite": 0.04,
                "Hedbergite": 0.03, "Jaspet": 0.14, "Crokite": 0.28, "Nocxium": 0}


class Zydrine(Mineral):
    ore_dict = {"Hemorphite": 0.15, "Hedbergite": 0.04,"Jaspet": 0.17, "Crokite": 0.29, "Bistot": 0.11, "Zydrine": 0}


class Megacyte(Mineral):
    ore_dict = {"Bistot": 0.24, "Arkonor": 0.31, "Megacyte": 0}


class Morphite(Mineral):
    ore_dict = {"Mercoxit": 0.18, "Morphite": 0}


# Dictionary with all the mineral classes to be able to iterate later on
all_ores_dict_list = [Tritanium.ore_dict_print(Tritanium.ore_dict), Pyerite.ore_dict_print(Pyerite.ore_dict),
                      Mexallon.ore_dict_print(Mexallon.ore_dict), Isogen.ore_dict_print(Isogen.ore_dict),
                      Nocxium.ore_dict_print(Nocxium.ore_dict), Zydrine.ore_dict_print(Zydrine.ore_dict),
                      Megacyte.ore_dict_print(Megacyte.ore_dict), Morphite.ore_dict_print(Morphite.ore_dict)]
