# Author : Claudéric DeRoy
# goal : make an attack so throw a d20 dice add your attack modifier and the the
#        target AC the function will tell if you hit the target.
# last date of modification : 18 jully 2022

import roll_dice as rd

def make_attack(advantage, attack_bonus, targetAC):
    roll = 0 + attack_bonus
    if advantage:
        roll1 = rd.roll_dice(1, "d20")
        roll2 = rd.roll_dice(1, "d20")

        if roll1 > roll2:
            roll += roll1
        else:
            roll += roll2
    else:
        roll += rd.roll_dice(1, "d20")

    if roll >= targetAC:
        print(str(roll-attack_bonus)+" + "+str(attack_bonus)+" = "+str(roll)+
              " Target AC "+str(targetAC)+" -> Target hit!")
    else:
        print(str(roll-attack_bonus)+" + "+str(attack_bonus)+" = "+str(roll)+
              " Target AC "+str(targetAC)+" -> Missing Target...")
