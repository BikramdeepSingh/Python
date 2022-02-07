'''
Functions
 functions are better way of organising the code
 Breaking the code smaller, managable and maintable chunks known as functions
 Functions contains lines of code that perform a specific task
 def is used to define a function
 we can define a function with multiple arguments
 Position of arguments matter otherwise the will be a bug in the code
 functions are called after defining them
'''

'''
Built in functions: already defined functions like input(), print()
User defined functions: lines of code written by the coder
'''

def greetings(fname,lname): #here greetings is fn name and uname is parameter
    print(f'''Hi {fname} {lname}! 
Welcome aboard''') #formatted string

f_name=input('Please enter your first name:')
l_name=input('Please enter your last name:')
greetings(f_name,l_name) #it takes positional arguments
greetings(lname='Kom', fname='Mary') #it takes keyword arguments
'''
Keyword arguments can be written in any order
 It improves the readability of the code and can be used while working 
 with numeric values.
 Keyword arguments should always come after positional arguments.
'''

greetings('Sam', lname='Billings')
# greetings('Billings', fname='Sam') It will give an error for multiple values for fname
# greetings(fname='Sam', 'Billings') It will give an error for keyword argument before positional