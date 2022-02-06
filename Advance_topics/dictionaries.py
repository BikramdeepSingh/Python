'''
Dictonaries 
used to store info in key value pair
defined with {}
key must be unique and are case sensitive in a dictonary and value can be anything
keys can be string or numbers
If  a key doesn't exists, a KeyError will be generated
'''

customer ={
    "name": "John Smith",
    "age" : 30,
    "is verified": True,
    12: 'this is unique ID',
    'purchase_history': ['1st Jan 2019', '3rd Jun 2019', '6th April 2020']
}
customer['name']='Sam Billings' #updates the value
customer['height']="160 cm" #adding a new key value pair

print(customer["name"])
#or we can use get method to pass a key
print(customer.get("age")) #returns none if key not present

print(customer.get("birth_date","Jan 1 1989")) #if key not presents, it returns a default value in the 2nd arg
print(customer["height"])
print(customer[12])

print(customer) #returns whole dictonary

print(customer.get('purchase_history')) #returns all the items in list