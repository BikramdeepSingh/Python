'''
Logical operators in python

and : logical and operator , both conditions must be true
or : logical or operator , at least one must be true
not : inverses the inputted boolean value
'''

has_high_income= True
has_good_credit= True

if has_high_income and has_good_credit: #both conditions must be True
    print("Eligible for loan")


'''
Comparison operators

>
<
==
<=
>=
!=

'''
temperature = 30

if temperature >= 30:
    print("It's a hot day")
elif temperature <=5:
    print("It's a cold day")
elif temperature == 20:
    print("Neither too hot nor too cold")
else:
    print("Have a nice day!")