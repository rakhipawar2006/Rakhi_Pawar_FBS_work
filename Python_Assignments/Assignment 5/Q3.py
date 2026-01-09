n = int(input('Enter the no. of Passenger: '))
total = 0

for i in range(1, n+1):
    ticket = int(input(f'Enter the cost of ticket of passenger {i} : '))
    age = int(input(f'Enter the age of passenger {i}: '))
    
    if(age < 12):
        ticket = ticket * 0.30
    elif(age > 59):
        ticket = ticket * 0.50
    else:
        ticket = ticket
        
    total += ticket
print(f'Total amount to ticket to travel for all passengers: Rs. {total}')
        