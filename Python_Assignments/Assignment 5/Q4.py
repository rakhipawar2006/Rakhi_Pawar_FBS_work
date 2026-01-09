m = int(input('Enter the value of start : '))
n = int(input('Enter the value of stop: '))

print(f'Armstrong Numbers between {m} to {n} are : ')

for i in range(m, n+1):
    temp = i
    count = 0
    sum = 0
    temp1 = i
    while(temp1 > 0):
        digit = temp1 % 10
        count += 1
        temp1 = temp1 // 10
        
    while(temp > 0):
        rem = temp % 10
        sum = sum + (rem ** count)
        temp = temp // 10
        
    if(sum == i):
        print(i, end = ' ')

        
        
        
        
    