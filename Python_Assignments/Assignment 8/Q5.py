def sumPrime(n):
    sum = 0
    for num in range(2, n+1):
        for i in range(2, num // 2 + 1):
            if(num % i  == 0):
                break
        else:
            sum += num
            
    return sum

n = int(input('Enter the value of n: ')) 

total = sumPrime(n)
print(f'Sum of Prime Numbers upto {n} = {total}.')
    