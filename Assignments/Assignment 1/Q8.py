days = int(input('Enter number of days: '))

years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

print(f'Years = {years}')
print(f'weeks = {weeks}')
print(f'Days = {days}')