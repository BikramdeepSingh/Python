'''
lists in python are defined by [] 
'''

names = ['John', 'Sarah', 'Mary', 'Joseph', 'Sam', 'Tom']

print(names) #prints the whole list
print(names[0]) #prints the first item in the list at index 0
print(names[-1]) #prints the last item in the list at last index
print(names[2:]) #prints from 2nd index till last i.e. from Mary to Tom
print(names[:]) #prints the whole list
print(names[1:-1]) #prints from 1st index till second last i.e. from Sarah to Sam 
print(names[0:6:2]) #prints every 2nd element from 0 till 5th index

names[0]='Jon' #updated the name at index 0
print(names)