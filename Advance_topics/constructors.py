'''
Constructors
 Construcotr is a function that gets called at the time of the creation of 
 the object.
 Constructos are defined with __init__
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
p1.x=11
print(f'(x,y)= ({p1.x},{p1.y})')

p1.draw() 
p1.move()

