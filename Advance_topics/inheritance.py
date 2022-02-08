'''
Inheritance
 It is a mechanism of reusing code.
 In prgramming the DRY(Don't Repeat Yourself) priciple is follwed.
 All the methods can be inhertied of the parent class in the child class

Single Inheritance: 
 Single inheritance enables a derived class to inherit properties 
 from a single parent class, thus enabling code reusability and the 
 addition of new features to existing code.

 Multiple Inheritance: 
  When a class can be derived from more than one base class this type of 
  inheritance is called multiple inheritance. In multiple inheritance, 
  all the features of the base classes are inherited into the derived 
  class.

Multilevel Inheritance 
 Features of the base class and the derived class are further inherited 
 into the new derived class. This is similar to a relationship representing
  a child and grandfather. 

Hierarchical Inheritance: 
 When more than one derived classes are created from a single base this 
 type of inheritance is called hierarchical inheritance. In this program, 
 we have a parent (base) class and two child (derived) classes.

Hybrid Inheritance: 
 Inheritance consisting of multiple types of inheritance is called 
 hybrid inheritance. 
'''

from xml.dom.pulldom import parseString


class Mammal:
    def walk(self):
        print('Can Walk')


class Dog(Mammal):
    def bark(self):
        print('Dog barks')


class Cat(Mammal):
    #Py will show an error if class is empty, we need to write a piece of code
    #or wtire pass 
    pass


dog1= Dog()
dog1.walk()
dog1.bark()
cat1= Cat()
cat1.walk()