'''
Functions
 functions are better way of organising the code
 Breaking the code smaller, managable and maintable chunks known as functions
 Functions contains lines of code that perform a specific task
 def is used to define a function
 functions are called after defining them
'''

'''
Built in functions: already defined functions like input(), print()
User defined functions: lines of code written by the coder
'''

def greetings(uname): #here greetings is fn name and uname is argument
    print(f'''Hi {name}! 
Welcome aboard''') #formatted string

name=input('Please enter your name:')
greetings(name)

