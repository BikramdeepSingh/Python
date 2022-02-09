'''
Two dice are rolled and output is displayed on console
'''

import random


class Dice:
    def __init__(self):
        pass

    def roll(self):
        dice_1= (1, 2, 3, 4, 5, 6)
        dice_2= (1, 2, 3, 4, 5, 6)
        '''
        Or 
        first = random.randint(1,6)
        second = random.randint(1,6)
        
        '''
        first=random.choice(dice_1)
        second=random.choice(dice_2)
        return first,second #it returns a tuple of values



dice_1 = Dice()
print(dice_1.roll() )