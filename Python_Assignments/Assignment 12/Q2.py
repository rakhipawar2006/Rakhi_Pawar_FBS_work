str = input('Enter the String: ')
n = int(input('Enter the index to remove: '))

res = ''

print('Original String: ',str)

for ch in range(0, len(str)):
    if ch != n:
        res = res + str[ch]
        
str = res
print(f'String after removing {n}th index: {str}')


# str = input('Enter the String: ')
# n = int(input('Enter the index to remove: '))  

#print(f'String after removing {n}th index:)
# print(str[ : n] + str[n+1 : ])        