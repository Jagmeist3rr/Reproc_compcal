#!/usr/bin/env python3
import Ore_program
import compiler_calculator


def main_loop_continue():
    while True:
        value = input('Select Program?: Y/N')
        if value == 'Y' or value == 'y' or value == 'N' or value == 'n':
            break
        else:
            print('Please enter Y/N')
    return value


def main():
    while True:
        print("Select Program:")
        print("1: Ore Processing Program\n2: Compiler Calculator")
        program_select = int(input("Select a program: "))
        match program_select:
            case 1:
                Ore_program.ore_processing_program()
            case 2:
                compiler_calculator.compiler_main()
        let_loop_continue = main_loop_continue()
        if let_loop_continue.lower() == 'n':
            print('Goodbye!')
            break
        else:
            print('OK')


main()
