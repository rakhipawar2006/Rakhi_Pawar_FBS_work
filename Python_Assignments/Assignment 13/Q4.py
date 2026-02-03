n = int(input('Enter a number: '))

dict = { }

for i in range(1, n+1):
    dict[i] = i * i
    
print(f'The generated dictionary that contains numbers between 1 to {n}.')
print(dict)