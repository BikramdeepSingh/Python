numbers = [5,2,5,2,2]

#with python special functionality
for ch in numbers:
    print('*'*ch)

print()
#or with inner loop
for ch in numbers:
    for i in range(ch):
        print('*',end='')
    print()

print()
#another way
for ch in numbers:
    output=''
    for i in range(ch):
        output +='*'
    print(output)