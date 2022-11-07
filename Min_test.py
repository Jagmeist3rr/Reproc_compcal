#!/usr/bin/env python 3
#Mineral class and processing amounts

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
                       "Dark Orchre": 2.88, "Spodumain": 59.1, "Hemorphite": 16.5, "Crokite": 116.4, "Arkonor": 26.4}


class Pyerite(Mineral):
    ore_dict= {"Scordite": .34, "Plagioclase": .2, "Omber": .23, "Pyroxeres": 1.68, "Gneiss": 2.64,
                       "Spodumain": 11.22, "Hemorphite": 8.19, "Bistot": 18.36}


class Mexallon(Mineral):
    ore_dict= {"Plagioclase": .29, "Kernite": 1.44, "Pyroxeres": 0.75, "Gneiss": 2.76,
                       "Spodumain": 1.08, "Jaspet": 7.38, "Arkonor": 3.0}


class Isogen(Mineral):
    ore_dict= {"Omber": 0.17, "Kernite": .14, "Dark Orchre": 0.17, "Gneiss": 0.55,
                       "Spodumain": .18, "Hemorphite": 0.48, "Hedbergite": 1.38}


class Nocxium(Mineral):
    ore_dict= {"Pyroxeres": 0.09, "Dark Orchre": 0.13,  "Hemorphite": 0.04,
                       "Hedbergite": 0.03,"Jaspet": 0.14, "Crokite": 0.28}


class Zydrine(Mineral):
    ore_dict= {"Hemorphite": 0.15, "Hedbergite": 0.04,"Jaspet": 0.17, "Crokite": 0.29, "Bistot": 0.11}


class Megacyte(Mineral):
    ore_dict= {"Bistot": 0.24, "Arkonor": 0.31}


class Morphote(Mineral):
    ore_dict= {"Mercoxit": 0.18}

reproc = Tritanium.ore_dict_print(Tritanium.ore_dict)
reproc_v2 = Tritanium.rich_dict_print(Tritanium.ore_dict)
reproc_v3 = Tritanium.compressed_dict_print(Tritanium.ore_dict)

reproc_s = Pyerite.ore_dict_print(Pyerite.ore_dict)
reproc_s2 = Pyerite.rich_dict_print(Pyerite.ore_dict)
reproc_s3 = Pyerite.compressed_dict_print(Pyerite.ore_dict)

print(reproc)
print(reproc_v2)
print(reproc_v3)
print(reproc_s)
print(reproc_s2)
print(reproc_s3)