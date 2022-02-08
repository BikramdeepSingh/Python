'''
Classes
 class defines a blueprint or template for creating objects.
 Classes are used to define new types to model real concepts.
 First letter of every word in a class is capitalized
 Every method in a class will have a self parameter which is very first parameter


Object
 Object is an instance of a class
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