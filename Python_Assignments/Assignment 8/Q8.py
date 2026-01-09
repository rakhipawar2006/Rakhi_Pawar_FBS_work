def reverseNum(num):
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev

num = int(input('Enter the Number : '))

reverse = reverseNum(num)
print(f'Reverse of {num} is = {reverse}')        