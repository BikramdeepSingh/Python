'''
For loop in python
for loop can be used for multiple iterations according to our condition
'''

for item in 'Python': #for variable in condition or string
    print(item,end=' ')# end will help to enter a space after every character

print()
#In python, we can define a list using []. It simply contains a list of items
for name in ['Joseph','John','James']:
    print(name)


'''
If we want to iterate through a long list of items, we use built in range function
range function creates an object that can be iterated.
'''

for num in range(5): 
    print(num, end=" ") # 0 1 2 3 4

print()
for num in range(1,5): #it will start from 1 till 4 
    print(num, end=" ") # 1 2 3 4

print()
for num in range(1,5,2): #3rd arguments is the increment the 1st argument
    print(num, end=" ") # 1 3 