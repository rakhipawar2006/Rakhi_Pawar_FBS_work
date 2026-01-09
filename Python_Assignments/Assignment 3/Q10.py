gender = input('Enter gender(M/F): ')
age = int(input('Enter age: '))

if(gender == 'M'):
    if(age > 20):
        print('Eligible for Marriage.')
    else:
        print('Not eligible for Marriage.')
else:
    if(age > 17):
        print('Eligible for Marriage.')
    else:
        print('Not eligible for Marriage.')