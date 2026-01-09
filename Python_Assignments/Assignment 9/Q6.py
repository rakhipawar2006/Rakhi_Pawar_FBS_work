def fibonacciSeries(n,a=0,b=1):
    if n == 0:
        return 0
    else:
        print(a, end = ' ')
        return fibonacciSeries(n-1, b, a + b)
        
num = int(input('Enter the Number: '))

print('Fibonacci Series are: ')
fibonacciSeries(num)
