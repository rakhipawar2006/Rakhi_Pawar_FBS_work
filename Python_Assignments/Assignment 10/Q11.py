li = [10, 12, 15, 20, 30, 60]

m = int(input('Enter the value of m: '))
n = int(input('Enter the value of n: '))

print(f'Elements in list divisible by {m} and {n} are: ')

for i in range(0, len(li)):
    if(li[i] % m == 0 and li[i] % n == 0):
        print(li[i])
    