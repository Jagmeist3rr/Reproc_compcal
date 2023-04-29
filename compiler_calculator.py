import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def loop_continue():
    while True:
        value = input('Continue?: Y/N')
        if value == 'Y' or value == 'y' or value == 'N' or value == 'n':
            break
        else:
            print('Please enter Y/N')
    return value


class CompilerInfo:

    current_isk_to_corp = 100000000/50000
    basic_comp_exp = 500
    basic_corp_cost = 6000
    advance_comp_exp = 1000
    advance_corp_cost = 14000
    expert_comp_exp = 2000
    expert_corp_cost = 30000
    cp_purchase_conversion = 100000000

    @staticmethod
    def get_user_exp():
        while True:
            level_exp = int(input('How much to next level: '))
            current_exp = int(input('How much exp do you have: '))
            remain_exp = level_exp - current_exp
            if remain_exp > 0 and current_exp > 0 and current_exp > 0:
                break
            else:
                print('Please enter a number greater than 0')
        return remain_exp

    @staticmethod
    def get_user_level():
        while True:
            user_level = int(input('Whats your Implant level?: '))
            if 0 < user_level <= 45:
                break
            else:
                print('Please enter a number from 0 - 45')
        return user_level

    @staticmethod
    def get_user_info():
        remain_exp = CompilerInfo.get_user_exp()
        user_level = CompilerInfo.get_user_level()
        if 0 < user_level <= 25:
            CompilerInfo.show_basic_needed(remain_exp)
            CompilerInfo.show_advance_needed(remain_exp)
            CompilerInfo.show_expert_needed(remain_exp)
        elif 25 < user_level <= 40:
            CompilerInfo.show_advance_needed(remain_exp)
            CompilerInfo.show_expert_needed(remain_exp)
        elif 40 < user_level <= 45:
            CompilerInfo.show_expert_needed(remain_exp)
        else:
            print('Please enter an appropriate level: ')

    @staticmethod
    def show_advance_needed(remain_exp):
        advance = remain_exp/CompilerInfo.advance_comp_exp
        advance_corp_cost = advance * CompilerInfo.advance_corp_cost
        advance_isk_cost = advance_corp_cost * CompilerInfo.current_isk_to_corp
        advance_cp_purchases = round_up(advance_isk_cost/CompilerInfo.cp_purchase_conversion)
        print('You would need: %d, CP: %d, ISK: %d, CP purchase times: %d'%(advance, advance_corp_cost, advance_isk_cost, advance_cp_purchases))

    @staticmethod
    def show_expert_needed(remain_exp):
        expert = remain_exp/CompilerInfo.expert_comp_exp
        expert_corp_cost = expert * CompilerInfo.expert_corp_cost
        expert_isk_cost = expert_corp_cost * CompilerInfo.current_isk_to_corp
        expert_cp_purchases = round_up(expert_isk_cost/CompilerInfo.cp_purchase_conversion)
        print('You would need: %d, CP: %d, ISK: %d, CP purchase times: %d'%(expert, expert_corp_cost, expert_isk_cost, expert_cp_purchases))

    @staticmethod
    def show_basic_needed(remain_exp):
        basic = remain_exp/CompilerInfo.basic_comp_exp
        basic_corp_cost = basic * CompilerInfo.basic_corp_cost
        basic_isk_cost = basic_corp_cost * CompilerInfo.current_isk_to_corp
        basic_cp_purchases = round_up(basic_isk_cost/CompilerInfo.cp_purchase_conversion)
        print('You would need: %d, CP: %d, ISK: %d, CP purchase times: %d'%(basic, basic_corp_cost, basic_isk_cost, basic_cp_purchases))


def compiler_main():
    while True:
        CompilerInfo.get_user_info()
        let_loop_continue = loop_continue()
        if let_loop_continue == 'N' or let_loop_continue == 'n':
            print('Bye!')
            break
        else:
            print('OK!')

    