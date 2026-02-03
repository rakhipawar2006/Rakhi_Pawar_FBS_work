dict = {1: 1, 2: 2, 3: 4, 4: 6}

result = 1

for value in dict.values():
    result *= value

print(f'Multiplication of all values in dictionary is: {result}')