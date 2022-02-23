'''
List comprehensions let us create new list based on sequences or ranges
List comprehensions can be really powerful, but they can also be super complex, resulting in code that's hard to read.
'''

'''
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)
'''

multiples = [ x*7 for x in range(1,11)] #same output as above code
print(multiples)

languages = ['Python', 'Java', 'Ruby', 'C++', 'C']
length = [len(language) for language in languages]
print(length)

multiples_of_3 = [x for x in range(0,101) if x%3==0]
print(multiples_of_3)



