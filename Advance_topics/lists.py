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


'''
2D lists
list in list
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix) #prints the whole list in single line
print(matrix[0]) #returns inner list with index 0 i.e [1, 2, 3]
print(matrix[0][0]) #returns elements at 0th index i.e. 1

for row in matrix:
    for column in row:
        print(column, end =' ')
    print()


'''
list methods
'''

number=[5,4,3,2,6]
number.append(13) #appends at the end of the list
print(number)

number.insert(1,20) #passes index and value to be added
number.append(5) #appends at the end of the list
print(number)

print(number.index(5)) #returns index of 1st occurence of this item otherwise error
print(50 in number) #returns True or False 

print(number.count(5)) #returns the number of occurence of 5 in list

number.sort() #sorts the list in asc
number.reverse() #reverses the list
print(number)

num2=number.copy();
print(num2)

number.remove(5) #removes 5 found at the very 1st occurence
print(number)

number.pop() #deletes last item from the list
print(number)
number.clear() #removes every item in the list
print(number)


