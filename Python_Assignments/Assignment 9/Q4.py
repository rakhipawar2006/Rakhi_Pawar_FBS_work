def sumOfNum(n):
    if n == 0:
        return 0
    else:
        return n + sumOfNum(n - 1)
    
num = int(input('Enter the Number: '))

res = sumOfNum(num)
print(f'Sum of Series 1 to {num} = {res}')