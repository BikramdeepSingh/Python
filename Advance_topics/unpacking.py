'''
Unpacking in py is the concept with which a item  of a list or tuple etc
can be directly stored inside some variables 
Unpacking will be done using exact number of variables as in list or tuple
otherwise error of too many values to unpack will be generated
or not enough values to unpack (expected 4, got 3)
'''

num = (1,2,3)#tuple
name = ['Sam', 'Tom', 'Jessica'] #list

x,y,z=num
print(x*y*z)
print('*'*z)

n1,n2,n3=name
print(n1,n2)
