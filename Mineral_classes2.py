#!/usr/bin/env python 3
# Mineral class and processing amounts
import Mineral_classes


class Ores():
    ore_dict = {}
    ore_name = ""
    mineral_list = {}
    mineral_name = ""
    def retrieve_mineral_info(ore_name, ore_dict):
        for dict_list in Mineral_classes.all_ores_dict_list:
            for key, value in dict_list.items():
                if ore_name.lower() == key.lower():
                    #print(ore_name, value, dict_list)
                    if ore_name in dict_list:
                        mineral_name = list(dict_list)[-1]
                        ore_dict[mineral_name] = value
        return ore_dict


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


class Spoudmain(Ores):
    ore_name = "Spoudmain"
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


total_ore_dict = [Veldspar.retrieve_mineral_info(Veldspar.ore_name, Veldspar.ore_dict), Scordite.retrieve_mineral_info(Scordite.ore_name, Scordite.ore_dict),
                  Pyroxeres.retrieve_mineral_info(Pyroxeres.ore_name, Pyroxeres.ore_dict), Plagioclase.retrieve_mineral_info(Plagioclase.ore_name, Plagioclase.ore_dict),
                  Omber.retrieve_mineral_info(Omber.ore_name, Omber.ore_dict), Kernite.retrieve_mineral_info(Kernite.ore_name, Kernite.ore_dict),
                  Jaspet.retrieve_mineral_info(Jaspet.ore_name, Jaspet.ore_dict), Hemorphite.retrieve_mineral_info(Hemorphite.ore_name, Hemorphite.ore_dict),
                  Hedbergite.retrieve_mineral_info(Hedbergite.ore_name, Hedbergite.ore_dict), Spoudmain.retrieve_mineral_info(Spoudmain.ore_name, Spoudmain.ore_dict),
                  Dark_Ochre.retrieve_mineral_info(Dark_Ochre.ore_name, Dark_Ochre.ore_dict), Gneiss.retrieve_mineral_info(Gneiss.ore_name, Gneiss.ore_dict),
                  Crokite.retrieve_mineral_info(Crokite.ore_name, Crokite.ore_dict), Bistot.retrieve_mineral_info(Bistot.ore_name, Bistot.ore_dict),
                  Arkonor.retrieve_mineral_info(Arkonor.ore_name, Arkonor.ore_dict), Mercoxit.retrieve_mineral_info(Mercoxit.ore_name, Mercoxit.ore_dict)]


print(total_ore_dict)