'''
Phone number translator 
It will tanslate a user entered number to words
'''

phone_no= input("Enter your phone number:")
num_dict={
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

for digit in range(phone_no.__len__()): #or for digit in phone_no
    print(num_dict.get(phone_no[digit], "!"), end=' ')
