'''
Guess the number program
In python, a while loop can also have else block
'''

secret_num=9
guess_count=1
guess_limit=4

print('---------------------------Guess the number---------------------------')
print('You will be given 3 chances to guess the correct number between 1 to 9')

while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count +=1
    if secret_num==guess:
        print('You guessed it right!')
        break
else:
    print('Out of attempts :(')


