#Person 1
age1 = int(input('Enter age of person 1: '))
ticket1 = float(input('Enter ticket amount of person 1: '))

if(age1 < 12):
    ticket1 = ticket1 * 0.7
elif(age1 > 59):
    ticket1 = ticket1 * 0.5
else:
    ticket1 = ticket1

#Person 2
age2 = int(input('Enter age of person 2: '))
ticket2 = float(input('Enter ticket amount of person 2: '))

if(age2 < 12):
    ticket2 = ticket2 * 0.7
elif(age2 > 59):
    ticket2 = ticket2 * 0.5
else:
    ticket2 = ticket2

# Person 3
age3 = int(input('Enter age of person 3: '))
ticket3 = float(input('Enter ticket amount of person 3: '))

if(age3 < 12):
    ticket3 = ticket3 * 0.7
elif(age3 > 59):
    ticket3 = ticket3 * 0.5
else:
    ticket3 = ticket3

#Person 4
age4 = int(input('Enter age of person 4: '))
ticket4 = float(input('Enter ticket amount of person 4: '))

if(age4 < 12):
    ticket4 = ticket4 * 0.7
elif(age4 > 59):
    ticket4 = ticket4 * 0.5
else:
    ticket4 = ticket4

#Person 5
age5 = int(input('Enter age of person 5: '))
ticket5 = float(input('Enter ticket amount of person 5: '))

if(age5 < 12):
    ticket5 = ticket5 * 0.7
elif(age5 > 59):
    ticket5 = ticket5 * 0.5
else:
    ticket5 = ticket5

total_amount = ticket1 + ticket2 + ticket3 + ticket4 + ticket5

print(f'Total ticket amount for all 5 people: {total_amount} Rs.')