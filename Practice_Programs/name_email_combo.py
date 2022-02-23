'''
We have a list of tuples containing two values each 
one is name and other is their email
print the name along with email
'''

def full_emails(person):
    result = []
    for name,email in person:
        result.append('{name} <{email}>'.format(name=name, email=email))
    return result


print(full_emails([('Sam', 'sam@gmail.com'), ('Tim', 'tim443@gmail.com'), ('Ken', 'ken123@gmail.com')]))
