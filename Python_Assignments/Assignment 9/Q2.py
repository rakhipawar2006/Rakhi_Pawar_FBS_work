def digitCnt(n):
    if n == 0:
        return 0
    else:
        return 1 + digitCnt(n // 10)

def armstrongNum(n, digits):
    if n == 0:
        return 0
    else:
        return (n % 10)**digits + armstrongNum(n // 10, digits)
    
    
num = int(input('Enter the Number: '))
d = digitCnt(num)

result = armstrongNum(num, d)

if result == num:
    print(f'{num} is an Armstrong Number.')
else:
    print(f'{num} not an Armstrong Number.')    