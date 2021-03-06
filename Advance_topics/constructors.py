'''
Constructors
 Construcotr is a function that gets called at the time of the creation of 
 the object.
 Constructos are defined with __init__

Magic or Dunder Methods 
 Magic methods in Python are the special methods that start and end with 
 the double underscores.
 Magic methods are not meant to be invoked directly by you, but the 
 invocation happens internally from the class on a certain action.
 For example, when you add two numbers using the + operator, internally, 
 the __add__() method will be called.
'''

class Point:
    def __init__(self,x,y): # constructor
        self.x = x
        self.y = y
        #self is reference to the current object
    def move(self):
        print(f'move the coordinates ({self.x}, {self.y})')

    def draw(self):
        print(f'draw the coordinates ({self.x}, {self.y})')


p1= Point(10,20) #Object of class Point

print(f'(x,y)= ({p1.x},{p1.y})')
p1.x=11 #updated value of x attribute
p1.draw() 
p1.move()

