'''
Removing duplicates from a list
'''
numbers = [1, 3, 2, 3, 1, 5, 11]

uniques = []

for unique in numbers:
    if unique not in uniques:
        uniques.append(unique)

print(uniques)