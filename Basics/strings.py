"""
Strings are sequence of characters written in quotes.
Strings can be enclosed in single or double inverted commas
"""
ques = 'What are strings'
body = """
Strings:
1. Strings are sequence of characters written in quotes.
2. Strings can be enclosed in single or double inverted commas
"""

print(ques)
print(body)

print(ques[0])#prints the character at index 0 in the string
print(ques[-1])#prints the last character of the string
print(ques[:6])#prints from starting index i.e. 0 till the 5th index
print(ques[4:])#prints from index 4 till the last index
print(ques[5:-2])#prints from index 5 till the third last index
print(ques[:])#0 is assumed as starting index and length of the string as the ending index

cloned_str= ques[:]
print(cloned_str)


#formatted strings
first_name="John"
last_name="Smith"
message=f'{first_name} ({last_name}) is a coder'
'''
here first_name and last_name are placeholders which will get replaced 
by the values in those variables.
f here stands for formatted strings 
'''
print(message)


'''
String functions
'''

user_name="Steve Smith"
print(len(user_name)) #returns the length of the string
#len is a general purpose function
print(user_name.upper())#function specific to strings for uppercase
print(user_name.lower())#function specific to strings for lowercase
print(user_name.find('e')) #returns index of 1st occurrence of the character 
# and it is case sensitive and if not found, it will return -1

print(user_name.find('Smith')) #returns starting index of the string
print(user_name.replace('Smith', 'Warner')) #replaces Smith with Warner
print(user_name.replace('e', 'i')) #replaces all e with i
print('Steve' in user_name) #retruns boolean value for string in the variable
print('Stivi' in user_name)

uname="harman singh"
print(uname.title()) #converts 1st character of each word to uppercase