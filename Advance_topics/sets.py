'''
It is one type of data type in python
Output is any order whenever we run the script
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
'''

thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

thisset.add('pineapple')
print(thisset)
print(f'length of the set is : {len(thisset)}')

thisset.remove('banana')
print(thisset)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

