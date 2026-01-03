def fibonacci(n,a,b):
    for i in range(1, n+1):
        c = a + b
        print(c, end = ' ')
        a = b
        b = c

n = int(input('Enter the value of n : '))
fibonacci(n,1,0)