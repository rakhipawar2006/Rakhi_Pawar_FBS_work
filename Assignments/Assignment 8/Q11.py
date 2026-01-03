def cnt_digit(num):
    cnt = 0
    while(num > 0):
        rem = num % 10
        num = num // 10
        cnt += 1
    return cnt
        
def armstrongSum(num,count):
    total = 0
    while(num > 0):
        digit = num % 10
        total = total + digit ** count
        num = num // 10
    return total

def isArmstrong(num):
    count = cnt_digit(num)
    sum = armstrongSum(num,count)
    if(num == sum):
        return('Number is an Armstrong.')
    else:
        return('Number is not an Armstrong.')

num = int(input('Enter the Number: '))
print(isArmstrong(num))
