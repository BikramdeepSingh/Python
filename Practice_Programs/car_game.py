'''
Car game
'''

print('''
---------------Menu----------------
1. Start: to start the engine
2. Stop : to stop the car
3. Help : to read the instructions
4. Quit : to exit
''')
user_choice = ''
car_started=False

while True:
    user_choice=input('Enter you choice:').upper()
    if user_choice=='START':
        if car_started==True:
            print('Car already started. PLease stop the car first!')
        else:
            print('Car started')
            car_started=True
    elif user_choice=='STOP':
        if not car_started:
            print('Car is stopped. Please start the car first!')
        else:
            print('Car stopped')
            car_started=False
    elif user_choice=='HELP':
        print('''
---------------Menu----------------
1. Start: to start the engine
2. Stop : to stop the car
3. Help : to read the instructions
4. Quit : to exit
''')
    elif user_choice=='QUIT':
        break
    else:
        print('Invalid input!\nPlease try again')
