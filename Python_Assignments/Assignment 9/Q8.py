def isPrimeNum(n, i = 2):
    if n <= 1:
        return False
    if n == i:
        return True
    if n % i == 0:
        return False
    return isPrimeNum(n, i+1)
 
num = int(input('Enter the Number: '))
res = isPrimeNum(num)

if(res):
    print(f'{num} is a Prime Number.')
else:
    print(f'{num} is not a Prime Number.')
        