def powerSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** i
    return sum

n = int(input('Enter the value of n: ')) 

total = powerSeries(n)
print(f'Sum of Power Series upto {n} = {total}.')