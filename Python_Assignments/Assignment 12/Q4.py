str = input('Enter the String: ')

print(f'Original String: {str}.')

str1 = str[-1] + str[1: -1] + str[0]

print(f'String after exchanging first & last character: {str1}')
