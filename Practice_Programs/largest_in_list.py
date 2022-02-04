'''
Largest number in the list
'''

num=[3, 6, 9, 24, 3, 11, 23, 1]
large=num[0]

for if_large in num:
    if large<if_large:
        large=if_large

print(f'Largest number is: {large}')