def sumFactSeries(n):
    sum = 0
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        sum += fact
    return sum

n = int(input('Enter the value of n: ')) 

total = sumFactSeries(n)
print(f'Sum of Factorial Series upto {n} = {total}.')