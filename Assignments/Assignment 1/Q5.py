P = int(input('Enter Principal Amount: '))
R = int(input('Enter Rate: '))
T = int(input('Enter Time: '))

C_I = (P * (1 + (R/100))**T ) - P

print(f'Compound Interest = {C_I}')