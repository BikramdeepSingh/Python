'''
Weigth converter

Take a user input of weight and convert that weight in kg or pound as 
directed by the user.
'''


raw_wt=int(input("Enter your weight:"))
wt_unit=input("Enter the weight unit: \nType L for lbs or K for kg:")

if wt_unit=="L" or wt_unit=="l":
    print(f"Your weight in kilograms is: {raw_wt/2.2}")
elif wt_unit=="K" or wt_unit=="k":
    print(f"Your weight in pounds is: {raw_wt*2.2}")
else:
    print("Something went wrong!")

