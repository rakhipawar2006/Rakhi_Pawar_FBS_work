def reverseNum(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverseNum(n // 10 , (rev * 10) + n % 10)
    
num = int(input('Enter the Number: '))

res = reverseNum(num)
print(f'Reverse of a {num} = {res}')