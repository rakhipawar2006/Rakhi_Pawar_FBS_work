n = int(input('Enter the value of n : '))

num = 2
count = 0

print(f'First {n} Prime Numbers are: ')

while count < n:
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end = ' ')
        count += 1
    num += 1