''' 
Enumerate is used to iterate in a list
It returns a tuple for each element in the list.
1st value in tuple is the index of the value in the sequence and 2nd value is the element in the sequence
It returns the item along with the index of that item.
'''


l1 = ['Kelly', 'Sam', 'Tim', 'John']

for name in enumerate(l1):
    print(name)

l2 = ('Tom', 'Samules', 'Chadwick')

for index,winner in enumerate(l2):
    print('{} - {}'.format(index+1,winner)) 