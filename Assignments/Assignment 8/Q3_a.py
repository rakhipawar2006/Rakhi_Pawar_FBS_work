def sumSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
        
n = int(input('Enter the value of n: '))
 
total = sumSeries(n)
print(f'Sum of First {n} numbers is = {total}.')
