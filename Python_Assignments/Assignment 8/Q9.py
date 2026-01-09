def chkPalindrome(num):
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev

num = int(input('Enter the Number : '))

reverse = chkPalindrome(num)

if(reverse == num):
    print(f'The given number {num} is a Palindrome.')
else:
    print(f'The given number {num} is not a Palindrome.')     