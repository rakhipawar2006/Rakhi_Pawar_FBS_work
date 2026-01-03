def sumOdd(n):
    sum = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            sum += i
    return sum

n = int(input('Enter the value of n: ')) 

total = sumOdd(n)
print(f'Sum of Odd Numbers upto {n} = {total}.')   