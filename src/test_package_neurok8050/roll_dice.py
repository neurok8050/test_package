# Author : Clauderic DeRoy
# goals : roll any number of any type of dice (d4, d6, d8, d10, d12, d20, d100)
#         and add the result of all the dice throw.
# last date of modification : 18 jully 2022


import random

def roll_dice(nb_dice, dice_type):

    sum = 0

    for i in range(0, nb_dice):
        sum += random.randint(1,int(dice_type[1:]))

    return sum
