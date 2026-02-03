str = input('Enter the String: ')
n = len(str)
s = ' '

for ch in str:
    if str.index(ch) % 2 == 0:
        s = s + ch
    
str = s
print('String after removing characters of odd index: ',str) 

# str = input('Enter the String: ')
# print('Original String: ',str)

# print('String after removing characters of odd index: ')
# print(str[: : 2])