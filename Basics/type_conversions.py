"""
a user input is stored in the form of a string of characters.
to work with other variables, we need to convert them to their respective 
forms in order to form calculations.
"""

dob=input("Enter your birth year:") #by default input treats user as a string value
print(type(dob)) # type returns the type of variable
age=2022-int(dob) # conversion of dob to integer
print(type(age))
print("Your age is",age)