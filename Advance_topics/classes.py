'''
In object-oriented programming, concepts are modeled as classes and objects.
An idea is defined using a class, and an instance of this class is called 
an object. Almost everything in Python is an object, including strings, 
lists, dictionaries, and numbers. When we create a list in Python, we're 
creating an object which is an instance of the list class, which represents 
the concept of a list. Classes also have attributes and methods associated 
with them. Attributes are the characteristics of the class, while methods 
are functions that are part of the class.

Classes
 class defines a blueprint or template for creating objects.
 Classes are used to define new types to model real concepts.
 First letter of every word in a class is capitalized
 Every method in a class will have a self parameter which is very first parameter


Object
 Object is an instance of a class

 We can use the type() function to figure out what class a variable or value belongs to.
 We can use the dir() function to print all the attributes and methods of an object.
 We can also use the help() function on an object, which will return the documentation 
 for the corresponding class.
'''

class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


p1= Point() #Object of class Point
#now with . operator we can access the methods of the class
p1.x=10 #htese are attributes which act like variables of class Point
p1.y=20

print(f'(x,y)= ({p1.x},{p1.y})')

p1.draw() 
p1.move()