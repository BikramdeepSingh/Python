'''
Modules
 Modules are files with some py code.
 Modules are used to organise the code into multiple files.
 Code is better organised and structured.
 And we can reuse our code.
 A module should contain all the related functions and classes.
 If code is outside functions or classes. whole code of the module
 will be executed first and then the called code will get executed
'''

#import file_name , now we can acces the methods and classes using . operator
#from file_name import method_name, here we can directly acces the method without . operator

#import functions
from functions import greetings

greetings('John','Smith')