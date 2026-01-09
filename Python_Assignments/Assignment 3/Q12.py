num = int(input('Enter a 3 digit number: '))
temp = num

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

reverse = d1 * 100 + d2 * 10 + d3

if(temp == reverse):
    print(f'The given number {temp} is a Palindrome.')
else:
    print(f'The given number {temp} is not a Palindrome.')