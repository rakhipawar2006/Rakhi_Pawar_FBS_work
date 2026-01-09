x = int(input('Enter the value of x : '))
n = int(input('How many terms you want: '))

sum = 0
sign = 1
denominator = 1

for i in range(1, n+1):
    sum += sign * (x ** i) / denominator
    sign = sign * -1
    denominator = denominator + 2

print(f'Sum of Sries = {sum}.')
    