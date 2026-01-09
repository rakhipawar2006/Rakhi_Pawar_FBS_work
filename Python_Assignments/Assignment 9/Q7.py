def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return  n % 10 + sumOfDigits(n // 10)
   
num = int(input('Enter the Number: '))
 
res = sumOfDigits(num)
print(f'Sum of Digits of {num} = {res}')