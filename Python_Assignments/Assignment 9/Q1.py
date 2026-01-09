def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

def sumFactorial(n):
    if n == 0:
        return 0
    else:
        return factorial(n) + sumFactorial(n -1)
num = int(input('Enter the Number: '))

res = sumFactorial(num)
print(f'Sum of Factorial Series 1 to {num} = {res}')