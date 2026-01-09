def sumofDigit(num):
    sum = 0
    while(num > 0):
        rem = num % 10
        sum += rem
        num //= 10
    return sum

num = int(input('Enter the Number : '))

total = sumofDigit(num)
print(f'Sum of Digit of {num} is = {total}')        