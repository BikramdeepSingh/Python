'''
Exceptions
 An exception is an event, which occurs during the execution of a program 
 that disrupts the normal flow of the program's instructions.
 When a Python script encounters a situation that it cannot cope with, it 
 raises an exception.
 An exception is a Python object that represents an error.
 Whenever a program finishes with exit code 0: It means success
 Whenever a program finishes with exit code 1: It means program crashed
 try except is used to handle exceptions in py
'''

try:
    age=int(input("Enter your age:"))
    #if user enters anything other than a no., code will not crash
    income=12000
    risk= income/age #eeror will occur if age is 0
    print(risk)
except ValueError: #defined tyope of error which might occur
    print('Invalid Value')
except ZeroDivisionError:
    print('Age can not be 0')