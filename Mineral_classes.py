#!/usr/bin/env python 3
# Mineral class and processing amounts

class Mineral():
    ore_dict = {}

    def ore_dict_print(ore_dict):
        return ore_dict

    def rich_dict_print(ore_dict):
        rich_dict = {}
        for key, value in ore_dict.items():
            rich_dict[key] = round(value * 10, 2)
        return rich_dict

    def compressed_dict_print(ore_dict):
        compressed_dict = {}
        for key, value in ore_dict.items():
            compressed_dict[key] = round(value * 100, 2)
        return compressed_dict


class Tritanium(Mineral):
    ore_dict= {"Veldspar": 1.25, "Scordite": .49, "Plagioclase": .15, "Omber": 1.8, "Kernite": .8, "Pyroxeres": 5.26,
               "Dark Orchre": 2.88, "Spodumain": 59.1, "Hemorphite": 16.5, "Crokite": 116.4, "Arkonor": 26.4,
               "Tritanium": 0}


class Pyerite(Mineral):
    ore_dict= {"Scordite": .34, "Plagioclase": .2, "Omber": .23, "Pyroxeres": 1.68, "Gneiss": 2.64,
               "Spodumain": 11.22, "Hemorphite": 8.19, "Bistot": 18.36, "Pyerite": 0}


class Mexallon(Mineral):
    ore_dict= {"Plagioclase": .29, "Kernite": 1.44, "Pyroxeres": 0.75, "Gneiss": 2.76,
               "Spodumain": 1.08, "Jaspet": 7.38, "Arkonor": 3.0,"Mexallon": 0}


class Isogen(Mineral):
    ore_dict= {"Omber": 0.17, "Kernite": .14, "Dark Orchre": 0.17, "Gneiss": 0.55,
               "Spodumain": .18, "Hemorphite": 0.48, "Hedbergite": 1.38,"Isogen": 0}


class Nocxium(Mineral):
    ore_dict= {"Pyroxeres": 0.09, "Dark Orchre": 0.13,  "Hemorphite": 0.04,
               "Hedbergite": 0.03, "Jaspet": 0.14, "Crokite": 0.28, "Nocxium": 0}


class Zydrine(Mineral):
    ore_dict= {"Hemorphite": 0.15, "Hedbergite": 0.04,"Jaspet": 0.17, "Crokite": 0.29, "Bistot": 0.11, "Zydrine": 0}


class Megacyte(Mineral):
    ore_dict= {"Bistot": 0.24, "Arkonor": 0.31, "Megacyte": 0}


class Morphite(Mineral):
    ore_dict= {"Mercoxit": 0.18, "Morphite": 0}


Tritanium1 = Tritanium()
Pyerite1 = Pyerite()
Mexallon1 = Mexallon()
Isogen1 = Isogen()
Nocxium1 = Nocxium()
Zydrine1 = Zydrine()
Megacyte1= Megacyte()
Morphite1 = Morphite()

all_mineral_names = [Tritanium1.__class__.__name__, Pyerite1.__class__.__name__, Mexallon1.__class__.__name__, Isogen1.__class__.__name__,
                     Nocxium1.__class__.__name__, Zydrine1.__class__.__name__, Megacyte1.__class__.__name__, Morphite1.__class__.__name__]
all_ores_dict_list = [Tritanium.ore_dict_print(Tritanium.ore_dict), Pyerite.ore_dict_print(Pyerite.ore_dict),
                      Mexallon.ore_dict_print(Mexallon.ore_dict), Isogen.ore_dict_print(Isogen.ore_dict),
                      Nocxium.ore_dict_print(Nocxium.ore_dict), Zydrine.ore_dict_print(Zydrine.ore_dict),
                      Megacyte.ore_dict_print(Megacyte.ore_dict), Morphite.ore_dict_print(Morphite.ore_dict)]
all_rich_dict_list = [Tritanium.rich_dict_print(Tritanium.ore_dict), Pyerite.rich_dict_print(Pyerite.ore_dict),
                      Mexallon.rich_dict_print(Mexallon.ore_dict), Isogen.rich_dict_print(Isogen.ore_dict),
                      Nocxium.rich_dict_print(Nocxium.ore_dict), Zydrine.rich_dict_print(Zydrine.ore_dict),
                      Megacyte.rich_dict_print(Megacyte.ore_dict), Morphite.rich_dict_print(Morphite.ore_dict)]
all_compressed_dict_list = [Tritanium.compressed_dict_print(Tritanium.ore_dict), Pyerite.compressed_dict_print(Pyerite.ore_dict),
                            Mexallon.compressed_dict_print(Mexallon.ore_dict), Isogen.compressed_dict_print(Isogen.ore_dict),
                            Nocxium.compressed_dict_print(Nocxium.ore_dict), Zydrine.compressed_dict_print(Zydrine.ore_dict),
                            Megacyte.compressed_dict_print(Megacyte.ore_dict), Morphite.compressed_dict_print(Morphite.ore_dict)]

#print(mineral_name)
#print(all_mineral_names)
#print(all_ores_dict_list)
#print(all_rich_dict_list)
#print(all_compressed_dict_list)