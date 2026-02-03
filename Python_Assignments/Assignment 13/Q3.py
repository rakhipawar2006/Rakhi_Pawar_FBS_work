key = (input('Enter the Key: '))

dict = {1:"Red", 2:"Purple", 3:"Pink"}

if key in dict:
    print(f'The given key {key} exits in dictionary.')
else:
    print(f'The given key {key} does not exits in dictionary.')