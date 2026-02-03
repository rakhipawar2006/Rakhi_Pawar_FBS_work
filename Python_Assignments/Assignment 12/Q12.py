str = input('Enter the String: ')

count = 0

for ch in str:
    if(ch.islower()):
        count += 1
        
print(f'Total number of lowercase characters in a string is = {count}')