'''
List comprehensions let us create new list based on sequences or ranges
'''

'''
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)
'''

multiples = [ x*7 for x in range(1,11)] #same output as above code
print(multiples)