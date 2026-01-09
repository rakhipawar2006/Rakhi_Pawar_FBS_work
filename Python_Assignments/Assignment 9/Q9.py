def power(m,n):
    if n == 0:
        return 1
    else:
        return m * power(m , n - 1)
    
m = int(input('Enter the value of base (m): '))
n = int(input('Enter the value of power (n): '))

res = power(m,n)
print(f'{m} to the power {n} = {res}')