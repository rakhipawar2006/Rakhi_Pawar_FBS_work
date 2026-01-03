n = int(input('Enter the value of n: ')) 
sum = 0
term = 1

for i in range(1, n+1):
    sum += term
    term = term * 2

print(f'Sum of Geometric Series from 1 to {n} where the common ratio is 2 = {sum}.')