'''
Tuples 
these are similar to lists
we can store items but unlike lists we cannot modify tuples (add, remove, etc)
Tuples are immutable(cannot be changed)
tuples are enclosed in ()
'''

num = (1,2,3,4,5,1)
print(num)
print(num.__len__()) #returns the length of num
print(num[3])
print(num.index(4)) #returns the index of 4
print(num.count(3)) #counts the number of occurences of 3
print(4 in num)