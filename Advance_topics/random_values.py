'''
Python already has built in modules
random is one of that module
'''

import random

for i in range(3):
    random_value=random.random() #generates random values between 0 to 1
    print(f'{random_value}')
    random_intval=random.randint(10,20)
    #randint generates random values between two arguments inclusive
    print(f'{random_intval}')